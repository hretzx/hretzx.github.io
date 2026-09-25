"""Turns the Flask site into plain HTML files for GitHub Pages.

Run it with:  python freeze.py
The finished site lands in build/. You rarely need to run this yourself:
the GitHub Action in .github/workflows/pages.yml runs it on every push.
"""

import os

from flask_frozen import Freezer

from app import PROJECTS, app

# Where the site will live, e.g. https://hritvi.github.io/portfolio/
# The GitHub Action fills this in. Only the link-preview image (base.html) uses
# it, because that one address has to be complete for WhatsApp, LinkedIn and co.
app.config["SITE_URL"] = os.environ.get("SITE_URL", "")
# Links between pages are written as relative paths ("../works/"), so the site
# works in a sub-folder like /portfolio/ as well as at the root of a domain.
app.config["FREEZER_RELATIVE_URLS"] = True
app.config["FREEZER_DESTINATION"] = "build"

freezer = Freezer(app)


@freezer.register_generator
def project():
    for item in PROJECTS:
        yield {"slug": item["slug"]}


if __name__ == "__main__":
    freezer.freeze()
    print("Done: the site is in build/")
