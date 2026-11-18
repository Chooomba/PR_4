#!/bin/sh
set -eu
python books.py --help
python books.py --data books.json.example search-author булгаков
