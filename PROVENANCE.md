# Provenance

Everything in a release comes from one ac1999 commit, read as committed files and listed with their
SHA-256s in the source ZIP's `source.json`. Nothing of ac1999's is run while converting it. Every row the
conversion changed or left out is named, with its reason, in `changes.json` and `empyrean-changes.json`
inside the world ZIP.

## What the conversion changes

ac1999 decides what the world holds, including what it places or starts that a dated source puts after
launch. Most rows pass through as ac1999 wrote them. The rest are what the files and formats force:

- **The data files.** ac1999's world was placed against later data files than the ones it plays on here.
  - Three Yanshi rows move into the rooms the CD's `cell.dat` numbers differently.
  - Five placements, their 17 linked spawns, four generators left with nothing to spawn and one portal
    destination name rooms the 1999 files don't have. They are left out, never patched in from later files.
  - Four placements of the snowman, whose art isn't in the October 31, 1999 `portal.dat`, are left out.
- **References.**
  - Three practice dummies' death treasure is written as a create list, the way ac1999's server reads it.
  - Six creatures name wielded treasure ac1999 doesn't define, and two emotes cast spells it doesn't
    define. Those rows are left out, as are the other rows that name something ac1999 doesn't define.
  - Any other dangling reference stops the conversion.
- **Schema.** ACE's world schema at commit `47edade3bd3f6044b676d4eb877c4965c7eda62b`. ac1999's own loot
  tables and recipe costs, which ACE's schema can't hold, go in `empyrean.sql`. Quests whose cooldown is
  written as a negative number, meaning none, are written as zero.

Every model, picture, palette, sound and effect that something placed, generated, created, given, crafted,
looted or started with can reach is present in the two 1999 files.

## Credit

ac1999 is the work of Adam Plumb and its contributors, building on Seedsow, ClassicDereth, GDL and GDLE,
under the GNU AGPL version 3. ACE's schema is the ACEmulator project's. Asheron's Call and its data files
belong to their owners and are not part of this repository or its releases.
