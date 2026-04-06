#!/bin/bash
cd /home/mikor/workspace/StaticSiteGenerator && python3 src/main.py
cd public && python3 -m http.server 8888