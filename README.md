# Kori Pro Skater — community playtest

Play: **https://hyperkodi.github.io/kori-pro-skater-playtest/**

This is a standalone Home Turf playtest for the Kori community. It is separate from the GameSlop website. Five-minute runs are local practice in this edition; online tournament submissions are not enabled.

## Playing

- Desktop: arrow keys to skate, hold/release Space to ollie, A flips, S grinds, D shove-its, F unlocked specials, G on/off board, N map, Escape pause. The in-game lesson explains trick sequences.
- Aerials: tap left/right in the air for 180 degrees; hold to keep spinning and release to finish the current half-turn. For deliberate body flips, hold V (controller RB; touch OLLIE + TRICK) with up/down. Ollie alone never triggers body flips. Land upright, within 25 degrees of forward or backward alignment, to score.
- Phone: open the link (including from Telegram), turn landscape, and use the MOVE/LOOK joysticks with Ollie, Grind and Trick. Special appears after unlocking. Up + Trick is a shove-it; Down + Trick is a grab. Walking is in Menu. Fullscreen is available from the header where supported.
- Shove-its: tap D 1-6 times quickly for 180/360/540/720/900/1080 degrees. On controller use Y; on touch flick MOVE up then tap TRICK repeatedly. Keep taps within 0.30 seconds; higher rotations need more airtime.
- Phones automatically receive a lighter edition (about 170 MB); the desktop edition is about 263 MB. Phone browsers require WebGL 2 and ASTC texture support. Progress is stored in this browser on this device.

## Reporting a bug

Use **Report a bug** on the page, or share a screenshot/video and the **Copy debug info** text in the Telegram community. Include the map location, steps that caused the problem, device model, and what you expected. The game does not automatically upload debug information.

If the browser closes or reloads during play, reopen this same link and use **Copy debug info**. A short, bounded history of game state and memory is saved locally and included from the previous visit. Runtime errors now say the game stopped rather than incorrectly reporting a loading failure. This diagnostic update does not claim to fix an unconfirmed device crash.

Latest update: curb grinds follow the actual road bends and hillside heights, so Kori stays on the ledge instead of floating above it. Unsupported paths above changed props and rooftops were trimmed or removed. Grind and manual balance runs at twice the previous tempo: five seconds reaches the old ten-second difficulty, and hands-off balance fails around 4.3–4.4 seconds. Active corrections can sustain longer holds. The final audit passed 6,433 gameplay checks and found no unsupported sections across 11,448 static grind paths at the audit tolerances. Upright halfpipe spins, deliberate flips, the 25-degree landing rule, hill-surface repairs, rail recovery, garage fixes and mobile diagnostics remain included. Physical iPhone Telegram crash confirmation remains pending.

## Publishing

The Unity browser build is stored as a GitHub release asset, keeping large binaries out of Git history. `release.json` records its tag and every published file's SHA-256. The manually triggered Pages workflow verifies the archive and files before publishing. It needs no external hosting credentials.

To update: package a new tested browser build, update `release.json`, commit it, upload `browser-build.zip` to its release tag, and run **Deploy community playtest** on main. Font license notices ship with the game. This repository grants no additional license to the game's artwork, music or compiled assets.
