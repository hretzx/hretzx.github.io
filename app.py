"""Hritvi Narvekar's portfolio.

Run it with:  python app.py   then open http://127.0.0.1:5000

All the words and pictures on the site live in the lists below, so adding a
project or a skill means editing this file only. The HTML is in templates/,
the look is in static/css/style.css.

Every page address ends in "/", so freeze.py can save each page as its own
folder with an index.html inside, which is what GitHub Pages serves.
"""

from flask import Flask, abort, render_template

app = Flask(__name__)


# ---------------------------------------------------------------------------
# Projects: one dict per project. The order here is the order on the page.
# "slug" is the last part of the project's address: /works/<slug>
# "images" are the screenshots on the project page, with the width to show
# them at (half the real image width, so they stay sharp on retina screens).
# ---------------------------------------------------------------------------
PROJECTS = [
    {
        "slug": "printease",
        "name": "PrintEase",
        "summary": (
            "A web application for managing printer queues where users can "
            "upload files for printing, choose print preferences, and track "
            "print status through an admin dashboard."
        ),
        "tags": ["next.js", "Tailwind CSS", "TypeScript", "JavaScript"],
        "cover": "images/projects/printease-1.png",
        "client": "PrintEase",
        "industry": "EdTech, Productivity Tools",
        "timeline": "3 weeks (2024)",
        "role": "Full-Stack Developer",
        "about": [
            "PrintEase is a printer queue management web application designed "
            "for students and faculty to submit documents for printing. Users "
            "can upload files, select print options (black & white or color), "
            "add instructions, and choose a payment method. Submissions appear "
            "on an admin dashboard where requests are processed in a "
            "first-come-first-serve order and marked complete once printed.",
        ],
        "images": [
            ("images/projects/printease-1.png", 787),
            ("images/projects/printease-2.png", 787),
            ("images/projects/printease-3.png", 787),
        ],
    },
    {
        "slug": "kuro-cli",
        "name": "Kuro-Cli",
        "summary": (
            "A command-line developer tool that streamlines project setup by "
            "instantly scaffolding modern React and Tailwind applications "
            "using a modular plug-and-play architecture."
        ),
        "tags": ["react.js", "next.js", "Tailwind CSS", "JavaScript", "api"],
        "cover": "images/projects/kuro-cli-cover.png",
        "client": "Kuro-CLI",
        "industry": "Developer Tools, AI",
        "timeline": "4 weeks (2025)",
        "role": "Developer",
        "about": [
            "Kuro-CLI is a voice-controlled terminal assistant that converts "
            "speech into executable system commands using Google’s Gemini AI. "
            "It integrates speech recognition, intent parsing, and automated "
            "command execution to streamline developer workflows through "
            "natural language interaction.",
        ],
        "images": [
            ("images/projects/kuro-cli-1.png", 936),
            ("images/projects/kuro-cli-2.png", 943),
            ("images/projects/kuro-cli-3.png", 944),
            ("images/projects/kuro-cli-4.png", 943),
        ],
    },
    {
        "slug": "shoresafe",
        "name": "ShoreSafe",
        "summary": (
            "ShoreSafe is a crowdsourced ocean hazard reporting platform "
            "developed for Smart India Hackathon. It enables citizens to submit "
            "geotagged hazard reports while integrating social media data to "
            "analyze real-time trends during coastal emergencies. I worked on "
            "building frontend components and automating YouTube and Twitter "
            "data scraping using n8n."
        ),
        "tags": ["next.js", "react.js", "Tailwind CSS", "n8n", "api"],
        "cover": "images/projects/shoresafe-cover.png",
        "client": "ShoreSafe",
        "industry": "Disaster Management, Civic Tech",
        "timeline": "2 weeks (2025)",
        "role": "Developer",
        "about": [
            "ShoreSafe is an integrated ocean hazard reporting platform built "
            "for INCOIS under SIH. The platform enables citizens to submit "
            "geotagged hazard reports while aggregating social media signals "
            "to improve real-time situational awareness during coastal "
            "emergencies.",
            "I contributed by building core frontend components using Next.js "
            "and implementing automated social media data scraping workflows "
            "(YouTube, Twitter) via n8n to support hazard trend analysis.",
        ],
        "images": [
            ("images/projects/shoresafe-1.jpg", 536),
            ("images/projects/shoresafe-2.jpg", 539),
            ("images/projects/shoresafe-3.jpg", 544),
            ("images/projects/shoresafe-4.jpg", 548),
        ],
    },
]

# The filter buttons above the project cards, in this order.
PROJECT_FILTERS = [
    "JavaScript", "TypeScript", "api", "n8n",
    "Tailwind CSS", "next.js", "react.js",
]

# The floating green chips around "What I bring to the table".
# x and y say where each chip sits, measured from the middle of the heading's
# top edge. "turn" is how many degrees it is tilted.
STRENGTHS = [
    {"text": "Full-Stack", "x": -32, "y": -218, "turn": -10},
    {"text": "C++", "x": 215, "y": -154, "turn": -9},
    {"text": "User Interface Design", "x": 425, "y": 26, "turn": 7},
    {"text": "Debugging", "x": -339, "y": -121, "turn": 8},
    {"text": "Optimization", "x": -432, "y": 35, "turn": -7},
    {"text": "Algorithm Design", "x": 422, "y": 212, "turn": 9},
    {"text": "Systems Design", "x": 233, "y": 337, "turn": -15},
    {"text": "Math Modeling", "x": -392, "y": 242, "turn": 3},
    {"text": "SQL", "x": -173, "y": 359, "turn": -4},
]

# The contact rows at the bottom of most pages. "link" can be None for a row
# that is just text.
CONTACTS = [
    {"label": "Email", "value": "hritvinarvekar@outlook.com",
     "link": "mailto:hritvinarvekar@outlook.com"},
    {"label": "LinkedIn", "value": "hritvinarvekar",
     "link": "https://www.linkedin.com/in/hritvinarvekar/"},
    {"label": "Website", "value": "https://aware-journey-936880.framer.app/",
     "link": "https://aware-journey-936880.framer.app/"},
    {"label": "Phone number", "value": "+91 83908 51961", "link": None},
]

# About me page.
ABOUT_INTRO = (
    "Second-year Computer Engineering student at Vidyalankar Institute of "
    "Technology with a CGPA of 9.81 and a perfect 10 SGPI in Semester 3. I "
    "specialize in Data Structures, Algorithms, and building efficient backend "
    "systems with a focus on performance optimization and scalable architecture."
)

HIGHLIGHTS = [
    "Top 1% in NPTEL Java Programming (IIT Kharagpur) with 94% score",
    "Subject Topper in Data Structures & Algorithms",
    "2nd Runner-up in C++ Competitive Programming Contest",
    "Completed AI Certification from University of Helsinki",
    "Building scalable backends with Node.js, Express & Prisma",
    "Active problem solver on Codeforces, HackerRank & CodeChef",
]

STATS = [
    {"number": 500, "suffix": "+", "label": "Problems Solved"},
    {"number": 15, "suffix": "+", "label": "Projects Built"},
    {"number": 94, "suffix": "%", "label": "NPTEL Score"},
]

# "icon" is a file name in static/icons/.
# "group" decides which filter button shows the skill.
SKILLS = [
    {"name": "C++", "icon": "cpp.svg", "group": "Languages"},
    {"name": "C", "icon": "c.svg", "group": "Languages"},
    {"name": "Java", "icon": "java.svg", "group": "Languages"},
    {"name": "Python", "icon": "python.svg", "group": "Languages"},
    {"name": "JavaScript", "icon": "javascript.svg", "group": "Languages"},
    {"name": "TypeScript", "icon": "typescript.svg", "group": "Languages"},
    {"name": "Node.js", "icon": "nodejs.svg", "group": "Tools & Frameworks"},
    {"name": "Express.js", "icon": "express.svg", "group": "Tools & Frameworks"},
    {"name": "React", "icon": "react.svg", "group": "Tools & Frameworks"},
    {"name": "Next.js", "icon": "nextjs.svg", "group": "Tools & Frameworks"},
    {"name": "Prisma", "icon": "prisma.svg", "group": "Tools & Frameworks"},
    {"name": "PostgreSQL", "icon": "postgresql.svg", "group": "Tools & Frameworks"},
    {"name": "Data Structures", "icon": "data-structures.svg", "group": "Tools & Frameworks"},
    {"name": "Algorithms", "icon": "algorithms.svg", "group": "Tools & Frameworks"},
    {"name": "System Design", "icon": "system-design.svg", "group": "Tools & Frameworks"},
    {"name": "Git", "icon": "git.svg", "group": "Tools & Frameworks"},
]
SKILL_GROUPS = ["Languages", "Tools & Frameworks"]


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------
@app.context_processor
def shared_data():
    """Gives every template the contact rows, since most pages show them."""
    return {"contacts": CONTACTS}


@app.route("/")
def home():
    return render_template(
        "index.html",
        projects=PROJECTS,
        filters=PROJECT_FILTERS,
        strengths=STRENGTHS,
    )


@app.route("/works/")
def works():
    return render_template("works.html", projects=PROJECTS, filters=PROJECT_FILTERS)


@app.route("/works/<slug>/")
def project(slug):
    for index, item in enumerate(PROJECTS):
        if item["slug"] == slug:
            # The "next project" link at the bottom; the last one has none.
            next_project = PROJECTS[index + 1] if index + 1 < len(PROJECTS) else None
            return render_template("project.html", project=item, next_project=next_project)
    abort(404)


@app.route("/about/")
def about():
    return render_template(
        "about.html",
        intro=ABOUT_INTRO,
        highlights=HIGHLIGHTS,
        stats=STATS,
        skills=SKILLS,
        skill_groups=SKILL_GROUPS,
    )


if __name__ == "__main__":
    app.run(debug=True)
