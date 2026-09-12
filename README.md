# Kori Pro Skater — community playtest

Play: **https://hyperkodi.github.io/kori-pro-skater-playtest/**

This is a standalone Home Turf playtest for the Kori community. It is separate from the GameSlop website. Five-minute runs are local practice in this edition; online tournament submissions are not enabled.

## Playing

- Desktop: WASD to skate, hold/release Space to ollie, Z flips, X grinds, C unlocked specials, G on/off board, N map, Escape pause. The in-game lesson explains trick sequences.
- Phone: open the link in Chrome or your device browser, turn landscape, and use the thumb joysticks and action buttons. Fullscreen is available from the header where supported.
- The first download is approximately 249 MB. Progress is stored in this browser on this device.

## Reporting a bug

Use **Report a bug** on the page, or share a screenshot/video and the **Copy debug info** text in the Telegram community. Include the map location, steps that caused the problem, device model, and what you expected. The game does not automatically upload debug information.

Try the three-level garage, mall roof gap, rooftop cable grind, waterslides, map, and five-minute timer. The latest source passed 261 native gameplay checks before this browser export; community browser/device testing is still needed.

## Publishing

The Unity browser build is stored as a GitHub release asset, keeping large binaries out of Git history. `release.json` records its tag and every published file's SHA-256. The manually triggered Pages workflow verifies the archive and files before publishing. It needs no external hosting credentials.

To update: package a new tested browser build, update `release.json`, commit it, upload `browser-build.zip` to its release tag, and run **Deploy community playtest** on main. Font license notices ship with the game. This repository grants no additional license to the game's artwork, music or compiled assets.
