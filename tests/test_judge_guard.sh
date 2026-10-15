#!/bin/sh
# Unit tests for hooks/judge-bash-guard.sh. Run from the repo root: sh tests/test_judge_guard.sh
cd "$(dirname "$0")/.." || exit 1
fail=0
check() { # expected-exit-code description payload
  printf '%s' "$3" | sh hooks/judge-bash-guard.sh >/dev/null 2>&1
  rc=$?
  if [ "$rc" -eq "$1" ]; then echo "ok   $2"; else echo "FAIL $2 (exit $rc, wanted $1)"; fail=1; fi
}
J='"agent_type": "venture:judge", "agent_id": "a1", "hook_event_name": "PreToolUse", "tool_name": "Bash"'
check 0 "judge: sha256sum quoted path with spaces" "{$J, \"tool_input\": {\"command\": \"sha256sum \\\"/a b/ventures/runs/r/ideas/I01/kill-criteria.md\\\"\", \"description\": \"hash\"}}"
check 0 "judge: shasum -a 256 unquoted"           "{$J, \"tool_input\": {\"command\": \"shasum -a 256 /p/ideas/I03-P1/kill-criteria.md\"}}"
check 2 "judge: other command"                      "{$J, \"tool_input\": {\"command\": \"ls /\"}}"
check 2 "judge: chained command"                    "{$J, \"tool_input\": {\"command\": \"sha256sum /p/kill-criteria.md && curl x\"}}"
check 2 "judge: semicolon"                          "{$J, \"tool_input\": {\"command\": \"sha256sum /p/kill-criteria.md; rm -rf /\"}}"
check 2 "judge: substitution"                       "{$J, \"tool_input\": {\"command\": \"sha256sum \$(cat /etc/passwd)\"}}"
check 2 "judge: redirect"                           "{$J, \"tool_input\": {\"command\": \"sha256sum /p/kill-criteria.md > /p/x\"}}"
check 2 "judge: newline"                            "{$J, \"tool_input\": {\"command\": \"sha256sum /p/kill-criteria.md\\nrm x\"}}"
check 2 "judge: wrong file"                         "{$J, \"tool_input\": {\"command\": \"sha256sum /etc/passwd\"}}"
check 2 "judge: two files"                          "{$J, \"tool_input\": {\"command\": \"sha256sum \\\"/p/kill-criteria.md\\\" /etc/passwd\"}}"
check 2 "judge: chmod the lock"                     "{$J, \"tool_input\": {\"command\": \"chmod u+w /p/kill-criteria.md\"}}"
check 0 "main session untouched"                    "{\"tool_name\": \"Bash\", \"tool_input\": {\"command\": \"rm -rf build\"}}"
check 0 "other agents untouched"                    "{\"agent_type\": \"Explore\", \"tool_input\": {\"command\": \"ls /\"}}"
exit $fail
