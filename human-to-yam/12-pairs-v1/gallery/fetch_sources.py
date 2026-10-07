"""Fetch original human clips from the publisher; never republish source media."""

import argparse
import hashlib
import io
import subprocess
import json
from pathlib import Path
import urllib.request
import zipfile

URL = "https://ml-site.cdn-apple.com/datasets/egodex/test.zip"


class RemoteArchive(io.RawIOBase):
    def __init__(self):
        with urllib.request.urlopen(
            urllib.request.Request(URL, method="HEAD"), timeout=30
        ) as r:
            self.size = int(r.headers["Content-Length"])
        self.pos = 0

    def seekable(self):
        return True

    def readable(self):
        return True

    def tell(self):
        return self.pos

    def seek(self, offset, whence=0):
        self.pos = (
            offset
            if whence == 0
            else self.pos + offset
            if whence == 1
            else self.size + offset
        )
        return self.pos

    def read(self, size=-1):
        if size < 0:
            size = self.size - self.pos
        if size == 0:
            return b""
        if size > 80_000_000:
            raise ValueError("Oversized archive request")
        request = urllib.request.Request(
            URL,
            headers={
                "Range": f"bytes={self.pos}-{min(self.size, self.pos + size) - 1}"
            },
        )
        with urllib.request.urlopen(request, timeout=60) as r:
            if r.status != 206 or not r.headers["Content-Range"].startswith(
                f"bytes {self.pos}-"
            ):
                raise ValueError("Invalid range response")
            data = r.read(size + 1)
        if len(data) > size:
            raise ValueError("Oversized response")
        self.pos += len(data)
        return data


def fetch(output, manifest, local_source_dir=None):
    output.mkdir(parents=True, exist_ok=True)
    originals = output / "original"
    originals.mkdir(exist_ok=True)
    archive = None
    try:
        for e in manifest:
            path = originals / f"{e['episode']:02d}.mp4"
            if (
                not path.exists()
                or hashlib.sha256(path.read_bytes()).hexdigest() != e["source_sha256"]
            ):
                if local_source_dir:
                    member = e["source_member"].split("/")
                    data = (
                        local_source_dir / (member[1] + "-" + member[-1])
                    ).read_bytes()
                else:
                    if archive is None:
                        archive = zipfile.ZipFile(RemoteArchive())
                    data = archive.read(e["source_member"])
                if hashlib.sha256(data).hexdigest() != e["source_sha256"]:
                    raise ValueError("Publisher file changed")
                path.write_bytes(data)
            # Publisher videos use MPEG-4 Part 2, unsupported in Chromium.
            # Preserve the original and make a browser-compatible playback copy.
            playback = output / f"{e['episode']:02d}.mp4"
            temporary = output / f"{e['episode']:02d}.tmp.mp4"
            subprocess.run(
                [
                    "ffmpeg",
                    "-v",
                    "error",
                    "-y",
                    "-i",
                    str(path),
                    "-map",
                    "0:v:0",
                    "-vf",
                    "scale=960:-2",
                    "-c:v",
                    "libx264",
                    "-threads",
                    "2",
                    "-preset",
                    "fast",
                    "-crf",
                    "19",
                    "-pix_fmt",
                    "yuv420p",
                    "-an",
                    "-movflags",
                    "+faststart",
                    str(temporary),
                ],
                check=True,
            )
            temporary.replace(playback)
            print(playback, flush=True)
    finally:
        if archive is not None:
            archive.close()


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("output", type=Path)
    p.add_argument(
        "--manifest", type=Path, default=Path(__file__).with_name("sources.json")
    )
    p.add_argument("--local-source-dir", type=Path)
    a = p.parse_args()
    fetch(a.output, json.loads(a.manifest.read_text()), a.local_source_dir)
