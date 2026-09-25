# Hritvi Narvekar — portfolio

The Framer site (hretz.framer.website) rebuilt as a small Flask app: plain HTML, one CSS file, a little JavaScript.

## Run it

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000.

## Where things live

```
app.py                  all the content: projects, skills, contact rows, About text
freeze.py               turns the site into plain HTML files (for GitHub Pages)
.github/workflows/      the GitHub Action that runs freeze.py and publishes the site
templates/
  base.html             the frame of every page: tab title, favicon, fonts, nav, footer
  index.html            home page
  works.html            /works
  project.html          /works/<project>
  about.html            /about
  _projects.html        filter buttons + project cards (used by home and /works)
  _contact.html         "Ready to build something amazing?" + contact rows
static/
  css/style.css         every style, colors at the top
  js/main.js            the filter buttons, fade-in on scroll, the counting numbers
  images/               photos, screenshots, favicon, the two drawings
  icons/                the skill logos and the button arrow
```

## Put it online (GitHub Pages)

GitHub Pages only serves plain files, so `freeze.py` renders every page into
`build/` as HTML. A GitHub Action does this for you on every push:

1. Push this folder to a GitHub repo (branch `main`).
2. In the repo: **Settings → Pages → Source: GitHub Actions**.
3. Push again (or run the action by hand under the **Actions** tab).

The site appears at `https://<username>.github.io/<repo>/`. After that, every
push to `main` updates it. To look at the frozen files yourself:
`python freeze.py`, then open `build/index.html`.

## Common changes

- **Add a project:** copy one of the dicts in `PROJECTS` in `app.py`, change the text, put its screenshots in `static/images/projects/`. The card, the filter and its own page appear by themselves.
- **Change a color:** edit the variables at the top of `static/css/style.css` (`--pink`, `--green`, ...).
- **Change the contact rows or the About text:** `CONTACTS`, `ABOUT_INTRO`, `HIGHLIGHTS`, `STATS` and `SKILLS` in `app.py`.
