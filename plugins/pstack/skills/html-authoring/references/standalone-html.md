# Save as standalone HTML

Export the current design as a single self-contained HTML file that works
completely offline — no external dependencies.

### How it works

An HTML inliner may discover resources referenced directly in HTML attributes
or CSS but miss resources referenced only as strings in JavaScript or JSX.
Use an existing project bundler when available. A new file with inline styles,
scripts, and assets needs no copying, inlining, or bundling: skip to verification.

### Step 1: Make a copy of the HTML file and update code-referenced resources

Copy the current HTML file. Read it. Copy its dependencies. Look through ALL
the code (inline scripts, imported JSX files, styled-components, etc) for any
resource URL that is referenced as a string in code rather than as an HTML
attribute. This includes:

- Image URLs in React/JSX (`<img src={...} />`, `style={{ backgroundImage: ... }}`)
- URLs in CSS-in-JS (styled-components, inline styles set via JS)
- Script tags that import other scripts which themselves reference resources
- Any fetch() or XMLHttpRequest calls that load assets
- Audio/video sources set programmatically

If an API call is core to the artifact, explain that it requires a connection;
do not silently remove it or describe the output as fully offline.

### Step 2: Inline resources

Resolve HTML attributes, CSS `url()` and `@import`, fonts, scripts, and
code-referenced assets. Replace external references with embedded data or
bundled resources using the chosen tool's actual interface. Resolve relative
paths against their source files. Do not emit `ext-resource-dependency` tags
or `window.__resources` calls without an implementation that consumes them.

### Step 3: Run the bundler

If bundling is needed, run the project's existing tool and write the output
separately from the editable source. Give the output file a friendly human name.
A complete single-file document needs no synthetic build project.

### Step 4: Verify

Read the tool result first. Fix unresolved assets before opening the result.
Preview the exported file using the entrypoint's checks. Check offline behavior
when claiming it; a successful connected preview does not establish that.

### Step 5: Present for download

Follow the entrypoint's delivery instructions. Keep the editable source when it
contains information lost during bundling.
