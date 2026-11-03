"""Writes what converting an ac1999 commit gave, beside the newest release, as Markdown."""

import glob
import json
import os
import re

revision = os.environ["REVISION"]
print(f"# ac1999 `{revision}`\n")

if not os.path.exists("bundle/manifest.json"):
    print("**Not converted.** The end of the log:\n\n```text")
    if os.path.exists("convert.log"):
        print("".join(open("convert.log", encoding="utf-8").readlines()[-15:]).rstrip())
    print("```")
    raise SystemExit

manifest = json.load(open("bundle/manifest.json", encoding="utf-8"))


def version(path):
    return [int(n) for n in re.findall(r"\d+", path.replace("\\", "/").split("/")[-2])]


releases = sorted(glob.glob("releases/*/release.json"), key=version)
newest = json.load(open(releases[-1], encoding="utf-8")) if releases else None
pack = manifest["world_pack_sha256"]

print("| | |\n|---|---|")
print(f"| World pack | `{pack}` |")
if newest:
    same = pack == newest["world_pack_sha256"]
    world = "the same world" if same else "a different world"
    print(f"| Newest release | ac1999 `{newest['source']['revision'][:8]}`, {world} |")
print(f"| Rows adapted | {manifest['adapted_rows']} |")
print(f"| Rows left out | {manifest['quarantined_rows']} |")

gone = manifest["world_policy"]["reviewed_but_gone"]
print("\nConverting is not checking: the 1999 files and play come before any release.")
if gone:
    print("\nReviewed rows the source no longer has:\n")
    print("\n".join(f"- {row}" for row in gone))
