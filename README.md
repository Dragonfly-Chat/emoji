# emoji
Emoji set for Dragonfly

To quickly get started, run:
```bash
python build.py
```
This will create a `build` folder, which will contain all emojis.

To load the emoji script into the website, add the `build/dragonfly-emoji-version.js` to the website.
Then call `$_emoji.text` with the text to replace with the emojis.

## Configuration
The `emoji-build.json` file contains all of the building configuration.

> `path` (`path`) - The path used for fetching emojis from the server.
> `size` (`32px`) - The size of each emoji, in pixels.