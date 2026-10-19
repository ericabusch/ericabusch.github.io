# Private update pages

This folder holds unlisted "life update" pages I share with friends/family
via direct link only. They are not linked from anywhere on the site, aren't
in the nav, and are excluded from search engines — but they are **not
password protected**. Anyone with the link (or anyone who digs through the
public GitHub repo) can view them. See the caveats at the bottom.

## To post a new update

1. Copy the template:

   ```
   cp templates/private-page-template.html updates/update-<slug>.html
   ```

2. Generate a random slug:

   ```
   python3 -c "import secrets; print(secrets.token_hex(4))"
   ```

3. Open the new file and edit the title/content. Add new dated sections
   (`<h2>Month Year</h2>`) at the top each time you update it (or, for the
   pupdates page, a new monthly file in `_sections/` — see below), so one page
   can grow over time instead of making a new one every time — or make a
   fresh `update-<slug>.html` for a new "issue," whichever you prefer.

4. Do **not** link this page from `index.html`, `pages/*.html`, or any nav
   menu.

5. Commit and push:

   ```
   git add updates/update-<slug>.html
   git commit -m "add update"
   git push
   ```

6. Share the URL directly:

   ```
   https://ericabusch.github.io/updates/update-<slug>.html
   ```

## How the main page is put together

`update-c13aa85e.html` is just a shell. Each month's content lives in its
own file in `_sections/`, named `YYYY-MM.html` (`2026-10.html` = October). Jekyll (which already builds this
site on GitHub Pages) stitches them into the page at build time via the
`{% include_relative %}` lines in the shell, newest first, so visitors see
one continuous scroll backwards in time. The leading underscore keeps the
`_sections/` folder itself out of the published site.

To add a month:

1. Create `_sections/YYYY-MM.html` (copy an existing one). It holds
   just the `<h2>`, a `<p>`, and a `.photo-grid` — no `<html>`/`<head>`.
2. Add `{% include_relative _sections/YYYY-MM.html %}` at the **top**
   of the include list in `update-c13aa85e.html`.
3. Fill in the blanks: the generated sections have `<!-- TODO ... -->`
   comments where text and captions go. Captions start with the photo's
   date (`10/2`); photos run newest to oldest within a month. Grep for `TODO` to find what's left.

To preview locally without installing Jekyll:

```
python3 updates/preview.py
```

This writes `updates/_preview.html` (git-ignored) and opens it.

## Adding photos and videos

Drop files into `updates/photos/` and reference them with a relative
path. Files are named `YYYY-MM-DD_HHMM_<original>.jpg` (Korea time) so
they sort chronologically.

Resize/compress phone photos before committing — GitHub Pages has no
server-side processing, and big files make the page slow and bloat the
repo. The recipe used so far (HEIC/PNG/JPG → JPG, max 1400px, quality 72;
`sips -r` bakes in the rotation for sideways HEICs):

```
sips -s format jpeg -s formatOptions 72 -Z 1400 IMG_1234.HEIC --out photos/2026-10-15_1403_IMG_1234.jpg
```

Videos play inline with a plain `<video>` tag inside a `<figure>`:

```html
<figure>
  <video controls playsinline preload="metadata" src="photos/2026-10-17_1215_IMG_0929.mp4#t=0.001"></video>
  <figcaption>...</figcaption>
</figure>
```

iPhone `.MOV` files are HEVC, which Chrome/Firefox/Android won't play, so
re-encode to H.264 MP4 first. With ffmpeg (`brew install ffmpeg`):

```
ffmpeg -i IMG_0929.MOV -vf scale=-2:960 -c:v libx264 -preset slow -crf 27 \
  -pix_fmt yuv420p -c:a aac -b:a 96k -movflags +faststart photos/2026-10-17_1215_IMG_0929.mp4
```

That gives roughly 1 MB per 10 seconds of vertical phone video.

## Caveats (read before posting anything sensitive)

- This is obscurity, not real access control — there's no login or
  password. Anyone with the link can view the page.
- The repo is public, so every page here is also visible forever in the
  git commit history on GitHub, even after you delete or rename it.
- `robots.txt` and the page's `<meta name="robots">` tag stop well-behaved
  search engines from indexing these pages, but don't stop a person who
  has the link from viewing or resharing it.
- If you ever need real password-protected privacy, GitHub Pages can't do
  it alone — you'd need a different host (e.g. Netlify or Cloudflare Pages
  with access rules).
