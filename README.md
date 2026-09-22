# Kori Pro Skater — community playtest

Play: **https://hyperkodi.github.io/kori-pro-skater-playtest/**

This is a standalone Home Turf playtest for the Kori community. It is separate from the GameSlop website. Five-minute runs are local practice in this edition; online tournament submissions are not enabled.

## Playing

- Desktop: arrow keys to skate, hold/release Space to ollie, A flips, S grinds, D shove-its, F unlocked specials, G on/off board, N map, Escape pause. The in-game lesson explains trick sequences.
- Classic aerials: tap left/right in the air for 180 degrees; hold to keep spinning and release to finish the current half-turn. For deliberate body flips, hold V (controller RB; touch OLLIE + TRICK) with up/down. Ollie alone never triggers body flips. Land upright, within 25 degrees of forward or backward alignment, to score.
- Phone: open the link (including from Telegram), turn landscape, and use the MOVE/LOOK joysticks with Ollie, Grind and Trick. Special appears after unlocking. In Classic mode, Up + Trick is a shove-it; Down + Trick is a grab. In Beginner mode, TRICK advances the sequence without directional input. Walking is in Menu. Fullscreen is available from the header where supported.
- Classic shove-its: tap D 1-6 times quickly for 180/360/540/720/900/1080 degrees. On controller use Y; on touch flick MOVE up then tap TRICK repeatedly. Keep taps within 0.30 seconds; higher rotations need more airtime.
- Phones automatically receive a lighter edition (about 182 MB); the desktop edition is about 275 MB. Phone browsers require WebGL 2 and ASTC texture support. Progress is stored in this browser on this device.

## Reporting a bug

Use **Report a bug** on the page, or share a screenshot/video and the **Copy debug info** text in the Telegram community. Include the map location, steps that caused the problem, device model, and what you expected. The game does not automatically upload debug information.

If the browser closes or reloads during play, reopen this same link and use **Copy debug info**. A short, bounded history of game state and memory is saved locally and included from the previous visit. Runtime errors now say the game stopped rather than incorrectly reporting a loading failure. This diagnostic update does not claim to fix an unconfirmed device crash.

Latest update: trick unlocks now announce themselves with an animated banner without pausing. Choose **TRICK MODE: BEGINNER** in the main/pause menu for a ten-trick sequence using only the Flip button (keyboard A, controller B, touch TRICK). Each press queues one animation while airborne; banking or losing the combo restarts at PUP FLIP. The trick book lists the full sequence. Classic retains directional tricks. Beginner five-minute practice has a separate personal best and does not submit to the Classic leaderboard; mode cannot change during a timed attempt.

Backward transition landings now give Kori a visible hop-turn on the rolling board, with the camera moving behind him and steering aligned during the camera orbit. Goal and combo-bank sounds are quieter. The release passed 241 feature checks and 6,543 movement/grind checks. It retains the 94 varied homes, eight vehicle families, 82 replaced parked cars, seven gardens, grounded curb grinds and twice-speed balance difficulty. Physical iPhone Telegram crash confirmation remains pending.

## Publishing

The Unity browser build is stored as a GitHub release asset, keeping large binaries out of Git history. `release.json` records its tag and every published file's SHA-256. The manually triggered Pages workflow verifies the archive and files before publishing. It needs no external hosting credentials.

To update: package a new tested browser build, update `release.json`, commit it, upload `browser-build.zip` to its release tag, and run **Deploy community playtest** on main. Font license notices ship with the game. This repository grants no additional license to the game's artwork, music or compiled assets.
