"""Verify the immutable release before GitHub Pages publishes it."""
import hashlib
import json
import sys
import zipfile
from pathlib import Path, PurePosixPath

archive, destination = Path(sys.argv[1]), Path(sys.argv[2])
release = json.loads(Path(__file__).with_name('release.json').read_text())
with archive.open('rb') as f:
    assert hashlib.file_digest(f, 'sha256').hexdigest() == release['archive_sha256'], 'Archive checksum differs'
destination.mkdir(parents=True, exist_ok=True)
with zipfile.ZipFile(archive) as z:
    assert set(z.namelist()) == set(release['files']), 'Unexpected or missing files'
    for name in z.namelist():
        path = PurePosixPath(name)
        assert not path.is_absolute() and '..' not in path.parts and '\\' not in name
        data = z.read(name)
        assert hashlib.sha256(data).hexdigest() == release['files'][name]['sha256'], name
        out = destination.joinpath(*path.parts)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(data)
print('Verified and unpacked', len(release['files']), 'files for', release['tag'])
