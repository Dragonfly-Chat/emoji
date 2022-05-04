# emoji
Emoji set for Dragonfly

To quickly get started, run:
```bash
git clone https://github.com/Dragonfly-Chat/emoji.git
cd emoji
python build.py
```
This will create a `build` folder, which will contain all emojis
and a script to use them. To add emojis to your website, follow this
quick example.

```html
<!DOCTYPE html>
<html>
  <head>
    <script src="path/to/build/dragonfly-emoji-0.0.2.min.js"></script>
    <script>
      window.onload = function() {
        $_emoji.element_id('header');
        $_emoji.element_query_all('p');
      }
    </script>
  </head>
  <body>
    <h1 id="header">This is some header text! :blobcat_attention:</h1>
    <p>This is some text with multiple emojis. :misc_frogchamp::blobhaj_blobhaj:</p>
    <p>Here is some more text, demonstrating <code>$_emoji.element_query_all</code>. :blobfox_bread::emote_flonshed:</p>
    <p>
      You can also use colons in your text without worrying about it turning into an emoji:
      :blobfox_cat_snuggle:
    </p>
  </body>
</html>
```


## Advanced Options
To add emojis to the website, link `build/dragonfly-emoji-version.js`
inside of your website. The function `$_emoji.text` can then be run
with the text containing emojis. It returns a reformatted string
containing the emojis, now formatted as images.

There are also four other functions used for enabling emojis in elements.
The first is `element`. This method accepts a DOM object, and replaces it's
`innerHTML` property with one that has properly formatted emojis. The second
function is `element_query`. This accepts a standard `document.querySelector`
input to get elements, and runs it through `element`. The third is
`element_query_all`, which runs `document.querySelectorAll` on the provided
element query and moves each element through `element`. The final 
function is `element_id`, which selects an element with the given ID and
runs it through `element`. All of these functions are subobjects of `$_emoji`.

## Configuration
The `emoji-build.json` file contains all of the building configuration.

> `path` (`path`) - The path used for fetching emojis from the server.
>
> `size` (`32px`) - The size of each emoji, in pixels.
https://pool.jortage.com/voringme/misskey/175041de-7708-4d25-8843-43f5998e55bb