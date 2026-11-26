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

## Releases

| Release | ac1999 commit | Converter commit | `world.pack` SHA-256 |
|---|---|---|---|
| 0.1.0 | `80adf514` | `cd2eecd6c` | `b7316cba19d3a7e2fd8365a0f1b421525ecbf10f879cab6e25c0d994ccff5195` |
| 0.2.0 | `e4eb0378` | `db116d575` | `29cd02c921cf2aebc13e6ddaa2ef82718c65eed106ee6ac90b1abc309a9e6902` |
| 0.3.0 | `3c564fdf` | `5ffc4b620` | `797412f688bb63fbae3c198febe3bdadacf052d7f6ae5a6abe686377bdd547ae` |
| 0.5.0 | `183e74f8` | `dcbf0c30f` | `448afe18a077a531c3648d329350ae919b33da0c6fee472876bc56c97707a60b` |
| 0.6.0 | `b25a9e0a` | `dcbf0c30f` | `cdc44e3e7e298ab555c504a31963417b068d390085b160df66ad80906345f240` |

The conversion made the same changes for each, in the same counts. What differs between them is ac1999's:
its commits `e89544d6` (Lich's Place) and `a7c2bd76` (Shadows off the landscape). 0.2.0 no longer holds the
eleven generator classes those removed: 6050, 6054, 22733, 22736, 25908, 61052, 61064, 61476, 61477, 61478
and 61517.

0.3.0 differs from 0.2.0 only by ac1999's `8a570d06`: 28 door weenies take their heritage names again
("Aluvian-Door", "Sho-Door", "Gharun'dim-Door"), as they had before January 2001.

0.5.0 differs from 0.3.0 first by ac1999's loot work of November 16, 2026 (`ee3a6833`, prepared as 0.4.0
and never released). Its loot tables and generator moved together, so this release needs the converter and the Empyrean that port its loot again: a new material
color table (`01f8540c`, `f07ca20b`), creature treasure tuned down (`5201b6e5`: 186 treasure rows and the
lower tiers' spell chances), Quilted Drawers out of the loot (`79fae425`), and dinnerware as valuables loot
in materials instead of a thrown weapon (`f5739f26`, `ba42d77b`: 12 weenies, the loot pools, and Rushiya
bint Anruq's shop). Four weenies, the Heaume, Quilted Drawers, Leggings and Boots, now take a material and
its colors.

Then by ac1999's world work of November 17 to 23, 2026, all of it content; the loot generator is
unchanged there. Twenty portals are "Arwic Portal" again rather than "Portal to Arwic", with
their descriptions gone and five of them pink (`3d99d140`). The landscape's spawns move: Shadow Wisps back
(`7b165ef4`, generator 61517 returns), Drudge Robbers only where they stand placed (`ec883290`, generators
61106 and 61408 gone), Mire Phyntos Wasps over more tiers (`4fd5fae8`), Virindi and Obsidian Golems to the
Obsidian Plains and a swampier ring round them (`1230c305`: 336 region encounter tables, generator 61067
gone). Creatures drop about a fifth more (`7561a498`: 192 treasure rows), and Scrolls of Regenerate Stamina
leave the loot (`183e74f8`). The Auroch Horn Spear has its release stats (`fef57a8b`), the Phyntos Wasps their
spells (`c63746a4`), Fort Tethana's three vendors their stock (`785354e6`, `06a08f6a`), the Sho armorers
their Pauldrons (`d655fa8f`); Ximi Nu and Kan Chi Gai stand in Wai Jhou again (`2423c66d`) and Arwic's pens
hold cow generators (`33a2f18e`, `df03fd47`).

0.6.0 differs from 0.5.0 by ac1999's world work of November 23 to 26, 2026, all of it content, with the same
converter; the loot generator and its tables are unchanged. The landscape's encounter tables are redrawn
across 18,172 landblocks: rows moved to the spots the 1999 land's scenes can spawn on (`78cfbf3e`), harmless
creatures only around the towns that aren't starter towns (`32c1ce11`), and the biomes split into Northern
and Southern Mountains and Freshwater and Shore (`e5d2e6f5`, `b25a9e0a`: 9 new mix generators, 17 old ones
gone over the range, 61041 reused). Creatures move with them, by biome and tier: Phyntos Wasps, Silver Rats, Mosswarts,
Wild Monougas, Tuskers, Skeletons, Wisps, Zofrit Zefirs, Gromnies and Golems (`afbb13a2` to `ec191094`, 53
mix generators retuned); Sewer Rat generators give way to Swamp Rats (`a6c17e34`, 7158 and 9271 gone),
Copper Golems take camps (`ec191094`, generator 4343), Fire Elemental generators spawn more (`b37acc79`).
Twenty-three casters, among them the Virindi Master and Director, the K'nath, the Fire Elementals and the
Tumerok, get spellbooks from the 2001 tables (`8628d423`). The post-release placements near Candeth Keep
leave (`f6472730`: six landblocks and generator 1969), and Asheron's and the Empyrean Jumpsuit return
(`26741c48`).

## Credit

ac1999 is the work of Adam Plumb and its contributors, building on Seedsow, ClassicDereth, GDL and GDLE,
under the GNU AGPL version 3. ACE's schema is the ACEmulator project's. Asheron's Call and its data files
belong to their owners and are not part of this repository or its releases.
