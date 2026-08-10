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
   (`<h2>Month Year</h2>`) at the top each time you update it, so one page
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

## Adding photos

Drop image files into `updates/photos/` and reference them from your page
with a relative path, e.g. `<img src="photos/whatever.jpg">`. See
`update-c13aa85e.html` for a working example gallery layout you can copy
from (grid of photos with captions).

Keep an eye on file size — resize/compress large phone photos before
committing them, since GitHub Pages has no server-side processing and big
images make the page slow to load and bloat the git repo.

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
