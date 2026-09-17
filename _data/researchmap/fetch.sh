#!/bin/bash
# researchmap 公開API から白井暁彦(akihiko)の業績を取得して JSON で保存する。
# 使い方: bash _data/researchmap/fetch.sh   （リポジトリ直下から）
set -e
cd "$(dirname "$0")"
for t in published_papers awards research_projects presentations books_etc industrial_property_rights misc; do
  curl -s -m 60 -o "rm_$t.json" "https://api.researchmap.jp/akihiko/$t?limit=1000"
  echo "$t $(wc -c < "rm_$t.json") bytes"
done
date -u +%Y-%m-%dT%H:%M:%SZ > fetched_at.txt
