# Empyrean world base: 1999

The world of Asheron's Call as it launched in November 1999, for [Empyrean](https://github.com/dereth-network/dereth)
to serve on its Launch era and [Dereth](https://github.com/dereth-network/dereth) to play.

It is a conversion of [ac1999](https://gitlab.com/adamplumb/ac1999)'s world database and treasure tables, by
Adam Plumb and ac1999's contributors, built reproducibly from one exact ac1999 commit. The conversion and
the changes it makes are ours; the world is theirs. See [NOTICE](NOTICE) and [PROVENANCE.md](PROVENANCE.md).

## What you need

- **Empyrean and Dereth with the Launch era.** It is not in a released version yet. Earlier servers refuse
  this world, and earlier clients play the wrong era over the wrong files.
- **The 1999 data files, which this repository never carries:** the `portal.dat` of October 31, 1999
  (iteration 105) and the retail CD's `cell.dat` of October 9, 1999 (iteration 67). `release.json` lists
  each file's SHA-256 so you can check yours.

## Using a release

Each release has two files:

| File | What |
|---|---|
| `ac1999-launch-world-<commit>.zip` | `world.pack`, the ACE-schema `world.sql`, the Empyrean extension `empyrean.sql`, the manifest and the change ledgers |
| `ac1999-launch-world-<commit>-source.zip` | The exact ac1999 files it was built from, with their SHA-256s |

Unzip the world and point the server at it:

```toml
[server]
world_pack_path = "world.pack"
dat_files_directory = "<the folder holding portal.dat and cell.dat>"
[era]
profile = "launch"
```

Point Dereth at the same `portal.dat` and `cell.dat`.

## Building it yourself

With the pinned converter (`release.toml`) built, either fetch the source:

```text
empyrean-import ac1999 --revision 5fe910e7a3e549d955117920a1bd30b4ee646938 --allow-incomplete --out <new-directory>
```

or rebuild from a release's source ZIP, offline:

```text
empyrean-import ac1999 --revision 5fe910e7a3e549d955117920a1bd30b4ee646938 --source ac1999-launch-world-5fe910e7-source.zip --allow-incomplete --out <new-directory>
empyrean-import ac1999 package --bundle <new-directory> --out <release-directory>
```

The same inputs give the same bytes: compare your `SHA256SUMS` with the release's, kept in
[`releases/`](releases/).

## Status

**Alpha.** The world converts, its references and art check out against the 1999 files, and character
creation, travel, combat and loot, vendors, crafting, a quest chain and saving are tested on it. It has
not had real players yet. `--allow-incomplete` is still required because some of ac1999's content has no
Empyrean equivalent yet; the ledgers list every row the conversion changed or left out.

## License

GNU Affero General Public License, version 3 ([LICENSE](LICENSE)), as ac1999's server and data are.
