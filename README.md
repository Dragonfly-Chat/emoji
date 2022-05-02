# emoji
Emoji set for Dragonfly

To quickly get started, run:
```bash
git clone https://github.com/Dragonfly-Chat/emoji.git
cd emoji
python build.py
```
This will create a `build` folder, which will contain all emojis.

To add emojis to the website, link `build/dragonfly-emoji-version.js` inside of your website.
The function `$_emoji.text` can then be run with the text containing emojis. It returns a
reformatted string containing the emojis, now formatted as images. 

## Configuration
The `emoji-build.json` file contains all of the building configuration.

> `path` (`path`) - The path used for fetching emojis from the server.
> `size` (`32px`) - The size of each emoji, in pixels.
