#!/usr/bin/env python3
"""Build a local preview of the update page without Jekyll.

Usage:  python3 updates/preview.py [update-c13aa85e.html]
Writes updates/_preview.html (git-ignored) and opens it in your browser.
"""
import os, re, sys, webbrowser
here = os.path.dirname(os.path.abspath(__file__))
name = sys.argv[1] if len(sys.argv) > 1 else "update-c13aa85e.html"
src = open(os.path.join(here, name)).read()
src = re.sub(r"\A---\n.*?---\n", "", src, flags=re.S)  # strip front matter
def inc(m):
    return open(os.path.join(here, m.group(1))).read()
out = re.sub(r"\{%\s*include_relative\s+(\S+)\s*%\}", inc, src)
dest = os.path.join(here, "_preview.html")
open(dest, "w").write(out)
print("wrote", dest)
webbrowser.open("file://" + dest)
