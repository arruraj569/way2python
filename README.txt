WAY2PYTHON — LOCAL PYTHON LEARNING LIBRARY

173 original lessons, 35 collections, ten tracks, and all 54 user-supplied
Python video chapters. Every topic includes a complete program, a separate
tricky program with an explained output, and interview answers. There is a
Start from zero guide, a searchable interview index, 378 downloadable lesson
programs, browser practice, and a runnable example kit.

DESIGN PATTERNS
32 lessons: all 23 GoF patterns, seven Python/Selenium approaches, a chooser
and a daily framework capstone. Each has daily usage and tradeoffs, a Python
rehearsal, a tricky program, interview answers, and a standalone Selenium
companion. Download the 96-program kit with a modular pytest framework from:
  http://localhost:8080/way2python/design-patterns.html

VERIFICATION
All 64 new Python/tricky programs were executed and their outputs checked.
Failure propagation, cleanup, independent data, URL rejection and rule-parser
contracts were also checked. Selenium companions and the modular framework
were compiled; the local lab was checked through the supported browser. The
Python Selenium browser suites remain a user-run practice step.

READ THE LIBRARY
Existing local Tomcat:
  http://localhost:8080/way2python/index.html
  http://localhost:8080/way2python/index.html#topic-index

Alternative: from the parent directory containing the way2python folder:
  python3 -m http.server 8081 --bind 127.0.0.1
Then open http://localhost:8081/way2python/index.html.
Stop the alternate server with Ctrl+C.

No dependency, database or build process is required to serve the HTML.
JavaScript enables searching, bookmarks, progress, and the practice controls.
External documentation and YouTube links require the internet.

TOMCAT
Deploy the supplied way2python.war to Tomcat's webapps directory as a separate
application. It does not need to replace or modify Way2Java.

PROGRESS
Saved and completed lesson IDs are stored under way2python:learning:v1 in
localStorage. Progress belongs to the current browser and origin. Export it
from Learning path to move it to another browser or address. Import merges
your export with existing progress rather than erasing it.

SOURCE AND CONTENT
tools/content.py defines shared metadata. The *_lessons.py files contain
original explanations, examples, practice tasks, pitfalls, and reference IDs.
tools/build_site.py generates the HTML from these files.
  python3 tools/build_site.py
  python3 tools/package_site.py

The reference directory preserves every URL supplied by the user and adds
official documentation. The video chapter list is user-supplied; no transcript
was independently retrieved. The supplied book PDF mirror was not retrievable;
the author website is linked as the readable alternative.

PRACTICE KIT
Download downloads/way2python-practice-kit.zip or read examples/README.txt.
It contains complete Playwright, Selenium and API tests plus data analysis.
Adaptation-only snippets are explicitly labeled inside their lessons.

Layout inspired by the user's local Way2Java learning library.
Original Way2Python explanations and examples, created 12 October 2026.
