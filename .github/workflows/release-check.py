"""What release.yml checks, in one place it can be tried without a run.

release-check.py pin
    Reads release.toml. Refuses a tag that doesn't name its version, or an unset pin. Writes the
    pins to GITHUB_OUTPUT when set, else prints them.

release-check.py verify <converter checkout> <release folder> <what rustc -V said> [<bundle>]
    Refuses unless the release's pack is the hash release.toml states (the bundle's world.pack itself,
    when the bundle is named, and what release.json says), and the converter, its Cargo.lock, the
    compiler and the source are the ones it pins. Writes release-notes.md into the release folder.
"""
import hashlib, json, os, re, subprocess, sys, tomllib
from pathlib import Path

EXPECTED_FILES = 4


def refuse(why):
    print(f"::error::{why}")
    sys.exit(1)


def pins():
    return tomllib.load(open("release.toml", "rb"))


def pin():
    t = pins()
    version = t.get("version", "")
    if not version:
        refuse("release.toml doesn't set version")
    tag = f"v{version}"
    if os.environ.get("GITHUB_REF_TYPE") == "tag" and os.environ["GITHUB_REF_NAME"] != tag:
        refuse(f"the tag {os.environ['GITHUB_REF_NAME']} doesn't name release.toml's version {version}")
    wanted = {
        "converter.commit": t["converter"]["commit"],
        "converter.cargo_lock_sha256": t["converter"]["cargo_lock_sha256"],
        "converter.toolchain": t["converter"]["toolchain"],
        "pack.sha256": t.get("pack", {}).get("sha256", ""),
        "source.revision": t["source"]["revision"],
    }
    for name, value in wanted.items():
        if not value:
            refuse(f"release.toml doesn't set {name}")
    out = {
        "tag": tag,
        "commit": t["converter"]["commit"],
        "toolchain": t["converter"]["toolchain"].split()[1],
        "revision": t["source"]["revision"],
    }
    text = "".join(f"{k}={v}\n" for k, v in out.items())
    if "GITHUB_OUTPUT" in os.environ:
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            f.write(text)
    else:
        print(text, end="")


def notes_for(version):
    """release.toml's version's section of CHANGES.md."""
    text = Path("CHANGES.md").read_text(encoding="utf-8")
    found = re.search(rf"^## {re.escape(version)}\b.*?\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    if not found or not found.group(1).strip():
        refuse(f"CHANGES.md has nothing under {version}")
    return found.group(1).strip()


def verify(converter, release, rustc_said, bundle=None):
    t, converter, release = pins(), Path(converter), Path(release)
    pinned = t["converter"]
    said = json.loads((release / "release.json").read_text(encoding="utf-8"))

    head = subprocess.run(
        ["git", "-C", str(converter), "rev-parse", "HEAD"], capture_output=True, text=True
    ).stdout.strip()
    if head != pinned["commit"]:
        refuse(f"the converter is at {head}, release.toml pins {pinned['commit']}")
    lock = hashlib.sha256((converter / "Cargo.lock").read_bytes()).hexdigest()
    if lock != pinned["cargo_lock_sha256"]:
        refuse(f"the converter's Cargo.lock is {lock}, release.toml pins {pinned['cargo_lock_sha256']}")
    if rustc_said.strip() != pinned["toolchain"]:
        refuse(f"built with {rustc_said.strip()}, release.toml pins {pinned['toolchain']}")

    for field in ("commit", "cargo_lock_sha256", "toolchain"):
        if said["converter"][field] != pinned[field]:
            refuse(f"release.json's converter {field} is {said['converter'][field]}, release.toml pins {pinned[field]}")
    if said["source"]["revision"] != t["source"]["revision"]:
        refuse(f"release.json's source is {said['source']['revision']}, release.toml pins {t['source']['revision']}")
    if bundle is not None:
        pack = Path(bundle) / "world.pack"
        if not pack.is_file():
            refuse(f"{pack} wasn't made")
        found = hashlib.sha256(pack.read_bytes()).hexdigest()
        if found != t["pack"]["sha256"]:
            refuse(f"the pack is {found}, release.toml states {t['pack']['sha256']}: nothing published")
    if said["world_pack_sha256"] != t["pack"]["sha256"]:
        refuse(f"the pack is {said['world_pack_sha256']}, release.toml states {t['pack']['sha256']}: nothing published")

    files = sorted(p.name for p in release.iterdir() if p.is_file())
    if len(files) != EXPECTED_FILES:
        refuse(f"the release folder holds {files}")

    # The same inputs are meant to give the same bytes, but only the pack's hash refuses: the record
    # kept here is of a build on another system, and it says nothing against a world that matches.
    record = Path("releases") / f"v{t['version']}" / "SHA256SUMS"
    if record.is_file() and record.read_bytes() != (release / "SHA256SUMS").read_bytes():
        print(f"::warning::SHA256SUMS differs from the one kept in {record}")

    (release / "release-notes.md").write_text(
        notes_for(t["version"]) + "\n\nSee `release.json` for what this was built from.\n",
        encoding="utf-8",
    )
    print(f"v{t['version']}: pack {said['world_pack_sha256']}, as release.toml states")


if __name__ == "__main__":
    if sys.argv[1:2] == ["pin"]:
        pin()
    elif sys.argv[1:2] == ["verify"] and len(sys.argv) in (5, 6):
        verify(*sys.argv[2:])
    else:
        sys.exit(__doc__)
