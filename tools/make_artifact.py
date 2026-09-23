#!/usr/bin/env python3
"""Strip the standalone wrapper off index.html so the page can be published as a
Claude artifact preview (artifacts supply their own <!doctype>/<head>/<body>)."""
import pathlib
root = pathlib.Path(__file__).resolve().parent.parent
html = (root / "index.html").read_text()
head = html[html.index("<title>"):html.index("</head>")]
body = html[html.index("<body>") + len("<body>"):html.rindex("</body>")]
out = root / "build" / "artifact.html"
out.parent.mkdir(exist_ok=True)
out.write_text(head.rstrip() + "\n\n" + body.strip() + "\n")
print(out)
