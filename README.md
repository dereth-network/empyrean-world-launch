# Empyrean world: Launch

The world of Asheron's Call as it launched in November 1999, for [Empyrean](https://github.com/dereth-network/dereth)
to serve on its Launch era and [Dereth](https://github.com/dereth-network/dereth) to play.

It is a conversion of [ac1999](https://gitlab.com/adamplumb/ac1999)'s world database and treasure tables, by
Adam Plumb and ac1999's contributors, built reproducibly from one exact ac1999 commit. The conversion and
the changes it makes are ours; the world is theirs. See [NOTICE](NOTICE) and [PROVENANCE.md](PROVENANCE.md).

## What you need

- **Empyrean 0.3.9 and Dereth 0.4.13, or later.** Earlier servers refuse this world, and earlier clients
  play the wrong era over the wrong files.
- **The 1999 data files, which this repository never carries:** the `portal.dat` of October 31, 1999
  (iteration 105) and the retail CD's `cell.dat` of October 9, 1999 (iteration 67). `release.json` lists
  each file's SHA-256 so you can check yours.

## Using a release

The server's importer fetches the newest release, checks its SHA-256 and writes its `world.pack`:

```text
empyrean-import fetch --era launch --pack --out world.pack
```

The Dereth Network launcher does the same when you host a Launch world. Each release has two files:

| File | What |
|---|---|
| `empyrean-world-launch-<commit>.zip` | `world.pack`, the ACE-schema `world.sql`, the Empyrean extension `empyrean.sql`, the manifest and the change ledgers |
| `empyrean-world-launch-<commit>-source.zip` | The exact ac1999 files it was built from, with their SHA-256s |

Point the server at the pack:

```toml
[server]
world_pack_path = "world.pack"
dat_files_directory = "<the folder holding portal.dat and cell.dat>"
[era]
profile = "launch"
```

Dereth plays them beside a modern install's `client_*.dat` files, which draw its interface:
`--dat-dir <modern folder> --classic-dat-dir <1999 folder>`. The launcher does this for you.

## Building it yourself

With the pinned converter (`release.toml`) built, either fetch the source:

```text
empyrean-import ac1999 --revision 3c564fdf96ce49b661597ef0326c05cf5c25e00d --allow-incomplete --out <new-directory>
```

or rebuild from a release's source ZIP, offline:

```text
empyrean-import ac1999 --revision 3c564fdf96ce49b661597ef0326c05cf5c25e00d --source empyrean-world-launch-3c564fdf-source.zip --allow-incomplete --out <new-directory>
empyrean-import ac1999 package --bundle <new-directory> --out <release-directory>
```

The same inputs give the same bytes: compare your `SHA256SUMS` with the release's, kept in
[`releases/`](releases/).

## Following ac1999

ac1999 decides what this world holds. The conversion changes only what the 1999 files and the formats force
([PROVENANCE.md](PROVENANCE.md)), so a new ac1999 commit is normally a new world.

Any commit can be tried, with the command above or with the **Try an ac1999 commit** workflow, which converts
it and reports what changed or why it was refused. A row the conversion reviewed that has since changed
upstream refuses the conversion until someone reviews it again.

Making a release stays a person's decision, and no workflow does it. They bump `release.toml`, run
`ac1999 package`, check the world against the 1999 files, play it, and publish.

## Status

**Alpha.** The world converts, its references and art check out against the 1999 files, and character
creation, travel, combat and loot, vendors, crafting, a quest chain and saving are tested on it. It has
not had real players yet. `--allow-incomplete` is still required because some of ac1999's content has no
Empyrean equivalent yet; the ledgers list every row the conversion changed or left out.

## License

GNU Affero General Public License, version 3 ([LICENSE](LICENSE)), as ac1999's server and data are.
