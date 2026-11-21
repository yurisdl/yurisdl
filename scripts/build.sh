#!/usr/bin/env sh
# Regera todos os SVGs de assets/ a partir dos scripts Python (sem dependências externas).
set -e
cd "$(dirname "$0")"
for f in hero about inventory arch quests extras buttons; do python3 -B "$f.py" ../assets; done
echo "SVGs gerados em assets/"
