#!/bin/sh
# venture: the judge may use Bash only to hash kill-criteria.md (rule 2).
# Reads the PreToolUse payload on stdin. Calls from anyone other than the
# venture judge pass through untouched (exit 0, no output = no decision).

payload=$(cat)

# Only act on the venture judge subagent.
printf '%s' "$payload" | grep -Eq '"agent_type"[[:space:]]*:[[:space:]]*"(venture:)?judge"' || exit 0

# Pull out tool_input.command (a JSON string) and undo the escaped quotes.
cmd=$(printf '%s' "$payload" | tr '\n' ' ' \
  | sed -nE 's/.*"command"[[:space:]]*:[[:space:]]*"(([^"\\]|\\.)*)".*/\1/p' \
  | sed -e 's/\\"/"/g' -e 's/\\\\/\\/g')

deny() {
  echo "venture judge: Bash is limited to hashing kill-criteria.md (sha256sum or shasum -a 256 on one file). Blocked: $cmd" >&2
  exit 2
}

[ -n "$cmd" ] || deny
# No chaining, substitution, redirection, globbing or escapes of any kind.
case "$cmd" in
  *';'*|*'&'*|*'|'*|*'`'*|*'$'*|*'<'*|*'>'*|*'*'*|*'?'*|*'\'*|*'('*|*')'*) deny ;;
esac
# Exactly one hashing command on one kill-criteria.md path.
printf '%s' "$cmd" | grep -Eq '^[[:space:]]*(sha256sum|shasum -a 256)[[:space:]]+("[^"]*kill-criteria\.md"|[^"[:space:]]*kill-criteria\.md)[[:space:]]*$' || deny
exit 0
