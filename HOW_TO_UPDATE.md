# How to update the site

The site is `index.html`. It is generated from `tools/build.py`, which holds all the text (tools, roles, clients, projects). Edit the text there and rebuild, so the HTML stays consistent.

## Change text or add a project

1. Open `tools/build.py`. The lists `tools`, `roles`, `clients` and `projects` are near the top.
2. Edit the text. For a finished project, change its status to `"Live"` and add its live report link in the last field.
3. Rebuild from the repo root, passing your Web3Forms key:
   ```bash
   python tools/build.py YOUR_WEB3FORMS_KEY
   ```
   This rewrites `index.html`.
4. Commit and push:
   ```bash
   git add -A && git commit -m "Update site" && git push
   ```
5. GitHub Pages updates within a minute or two.

## Contact form

- The form sends to your inbox through Web3Forms (free). The access key is passed to `tools/build.py` as shown above.
- Until a key is set, the form falls back to opening the visitor's email app addressed to you, so messages are never lost.
- The email address, WhatsApp number and social links are at the top of `tools/build.py`.

## Resume

Replace `Shivam-Agarwal-Resume.pdf` with the new file, keeping the same name, and push.

## Turn on GitHub Pages (one time)

1. Open the repo on GitHub, then Settings, then Pages.
2. Source: **Deploy from a branch**. Branch: `main`, folder `/ (root)`. Save.
3. Wait a minute, then open https://agshivam.github.io.

## Check before sharing

- Open the site on your phone.
- Click the resume, WhatsApp and email links.
- Send yourself one test message through the form.
