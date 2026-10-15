#!/bin/sh
# End-to-end test: one full headless /venture:run for the fictional Pune user, then the
# blindness check on its transcript. Needs an authenticated `claude` CLI with this plugin
# installed (claude plugin marketplace add <repo> && claude plugin install venture@venture).
#
#   sh tests/e2e.sh [quick|standard|deep] [workdir]
#   sh tests/e2e.sh check "<idea>" [workdir]        # /venture:check on your own idea
#
# Real web research: costs roughly $3-4 per carried idea. Results land in <workdir>/ventures.
set -e
mode=${1:-quick}
repo=$(cd "$(dirname "$0")/.." && pwd)
idea=""
if [ "$mode" = check ]; then idea=${2:?usage: sh tests/e2e.sh check "<idea>" [workdir]}; shift; fi
work=${2:-$(mktemp -d)}
mkdir -p "$work"
cd "$work"

echo "network check (the auditor needs to fetch sources):"
for u in https://en.wikipedia.org/wiki/Pune https://www.reddit.com/ https://techcrunch.com/; do
  code=$(curl -s -o /dev/null -m 15 -w '%{http_code}' "$u" 2>/dev/null) || true; code=${code:-000}
  printf '  %s %s\n' "${code%"${code#???}"}" "$u"
done

answers="Fictional test user, all answers given here and confirmed (non-interactive). Starting point: $( [ "$mode" = check ] && echo '(a) the idea above; how they plan to charge: as stated in the idea' || echo '(c) nothing yet'). Lives in: Pune, India. Target market: local (Pune). Constraints: K1 capital ₹1,00,000 HARD; K2 10 hours/week HARD; K3 skills they have: spreadsheets, social media marketing, English/Hindi/Marathi; K4 can learn: no-code tools (FLEXIBLE, can hire freelancers within the capital limit); K5 risk appetite low — cannot lose more than the ₹1,00,000; K6 time to first revenue 3 months HARD; K7 B2C only HARD; K8 off-limits: alcohol, gambling, crypto, MLM, anything needing a food-safety or medical licence they do not have; K9 other: keeps a full-time job. Unfair advantages: none."
if [ "$mode" = check ]; then
  prompt="/venture:check \"$idea\" $answers"
else
  prompt="/venture:run $answers Depth mode: $mode."
fi

claude -p "$prompt" \
  --allowedTools "Read Write Edit Glob Grep Agent Task WebSearch WebFetch Bash(chmod *) Bash(sha256sum *) Bash(shasum *) Bash(mkdir *) Bash(date *) Bash(ls *)" \
  --output-format stream-json --verbose > run.log 2>&1

python3 "$repo/tests/check_blindness.py" run.log
ls ventures/runs/*/9*-*.md
echo "run folder: $work/ventures"
