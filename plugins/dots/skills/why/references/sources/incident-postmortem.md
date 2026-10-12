# Incident and postmortem context

Defensive code is often added after an outage: "we added this check after the
X incident." When the target has null checks, retries, timeouts, rate limits,
or feature flags, look for that history in the sources you are already
searching:

- **Git:** commit messages such as "fix for incident" or "add defensive
  check", and a revert followed by "re-apply with…", are strong signals.
- **Pull requests and issues:** links to incident tickets, postmortems, or
  action items in the PR body or review thread.
- **Other records the user named:** search postmortems or incident tickets
  for the target file, feature, or error string around the date the code
  landed.

If you find an incident link, read the full postmortem; its action items often
point straight at the code change. Evidence is strongest when several records
reference each other and the target PR.

Skip this search when the code has no defensive behavior.
