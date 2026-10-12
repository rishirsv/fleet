#!/usr/bin/env node
/**
 * generate-theme.mjs — compile assets/design-tokens.yaml into assets/theme.css.
 *
 * Usage:   node scripts/generate-theme.mjs [--check]
 * Inputs:  assets/design-tokens.yaml (restricted YAML subset — nested maps,
 *          scalars, and flat arrays only; no anchors or multi-line strings).
 * Output:  assets/theme.css (tokens + alpha ladder + base styles + motion).
 *          --check exits 1 if the committed theme.css is stale.
 *
 * design-tokens.yaml is the source; never edit theme.css by hand. The x-dark,
 * x-alpha-steps, x-motion, x-chart, and x-tones keys are generator-owned
 * extensions beyond the design.md alpha spec. references/DESIGN.md holds the
 * prose rules for using these tokens.
 *
 * The CSS header keeps its "GENERATED from DESIGN.md" marker: catalog.mjs and
 * the copies embedded in sample pages match that exact text.
 */

import { readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const tokensPath = join(root, "assets", "design-tokens.yaml");
const outPath = join(root, "assets", "theme.css");

// ---------- minimal YAML subset parser (indentation maps + inline arrays) ----------

function parseYaml(text) {
  const lines = text.split("\n").filter((l) => l.trim() && !l.trim().startsWith("#"));
  const rootObj = {};
  const stack = [{ indent: -1, obj: rootObj }];
  for (const line of lines) {
    const indent = line.length - line.trimStart().length;
    const trimmed = line.trim();
    const colon = trimmed.indexOf(":");
    if (colon === -1) throw new Error(`Unparseable line: ${line}`);
    const key = trimmed.slice(0, colon).trim();
    let value = trimmed.slice(colon + 1).trim();
    while (stack.length > 1 && indent <= stack[stack.length - 1].indent) stack.pop();
    const parent = stack[stack.length - 1].obj;
    if (value === "") {
      const child = {};
      parent[key] = child;
      stack.push({ indent, obj: child });
    } else if (value.startsWith("[")) {
      parent[key] = value
        .slice(1, -1)
        .split(",")
        .map((v) => v.trim())
        .filter(Boolean)
        .map((v) => (isNaN(Number(v)) ? stripQuotes(v) : Number(v)));
    } else {
      parent[key] = stripQuotes(value);
    }
  }
  return rootObj;
}

function stripQuotes(v) {
  return v.replace(/^["']|["']$/g, "");
}


// ---------- alpha ladder ----------

function hexToRgb(hex) {
  const h = hex.replace("#", "");
  const full = h.length === 3 ? h.split("").map((c) => c + c).join("") : h;
  return [0, 2, 4].map((i) => parseInt(full.slice(i, i + 2), 16));
}

function alphaLadder(foreground, steps) {
  const [r, g, b] = hexToRgb(foreground);
  return steps
    .map((s) => `  --a${s}: rgba(${r}, ${g}, ${b}, ${(s / 100).toFixed(2)});`)
    .join("\n");
}

function colorVars(colors) {
  return Object.entries(colors)
    .map(([k, v]) => `  --${k}: ${v};`)
    .join("\n");
}

// ---------- emit ----------

const design = parseYaml(readFileSync(tokensPath, "utf8"));
const { colors, typography, spacing, rounded } = design;
const dark = design["x-dark"];
const steps = design["x-alpha-steps"];
const motion = design["x-motion"];
const chart = design["x-chart"];
const tones = design["x-tones"] ?? {};
const t = (role, prop) => typography[role][prop];

// x-chart values are var() references into base tokens, so one :root block
// suffices — they follow the dark override of whatever they point at.
const chartVars = Object.entries(chart)
  .map(([k, v]) => `  --chart-${k}: ${v};`)
  .join("\n");

// A tone overrides only the tokens it lists. Its dark block uses a compound
// selector so it outranks the base [data-theme="dark"] block regardless of order.
const indent = (text) => text.replace(/^ {2}/gm, "    ");
function toneVars(tone, palette, light) {
  const lines = [colorVars(palette), alphaLadder(palette.foreground, steps)];
  if (light) {
    if (tone["display-font"]) lines.push(`  --font-display: ${tone["display-font"]};`);
    if (tone["display-tracking"] != null) lines.push(`  --display-tracking: ${tone["display-tracking"]};`);
    if (tone["card-radius"]) lines.push(`  --r-card: ${tone["card-radius"]};`);
    if (tone["text-muted-step"] != null) {
      if (!steps.includes(Number(tone["text-muted-step"]))) throw new Error(`text-muted-step must be one of ${steps.join(", ")}`);
      lines.push(`  --text-muted: var(--a${tone["text-muted-step"]});`);
    }
  }
  return lines.join("\n");
}
const toneCss = Object.entries(tones).map(([name, tone]) => {
  if (!tone.colors?.foreground || !tone.dark?.foreground) throw new Error(`x-tones.${name} needs colors.foreground and dark.foreground`);
  const light = { ...colors, ...tone.colors };
  const darkPalette = { ...dark, ...tone.dark };
  return `/* tone: ${name} */
[data-tone="${name}"] {
${toneVars(tone, light, true)}
}

[data-tone="${name}"][data-theme="dark"] {
${toneVars(tone, darkPalette, false)}
}

@media (prefers-color-scheme: dark) {
  :root[data-tone="${name}"]:not([data-theme]) {
${indent(toneVars(tone, darkPalette, false))}
  }
}`;
}).join("\n\n");

const css = `/* GENERATED from DESIGN.md by scripts/generate-theme.mjs — do not edit.
 * Tokens + base document styles for dots HTML artifacts. Inline this file
 * verbatim inside <style> in every artifact. */

:root {
${colorVars(colors)}
${alphaLadder(colors.foreground, steps)}
  --text-muted: var(--a60);
  --font-sans: ${t("body", "fontFamily")};
  --font-mono: ${t("mono", "fontFamily")};
  --font-display: ${t("display", "fontFamily")};
  --display-tracking: ${t("display", "tracking")};
  --article: ${spacing.article};
  --wide: ${spacing.wide};
  --canvas: ${spacing.canvas};
  --section: ${spacing.section};
  --block: ${spacing.block};
  --r-card: ${rounded.card};
  --r-code: ${rounded.code};
  --r-inline: ${rounded.inline};
  --r-pill: ${rounded.pill};
  --r-bubble: ${rounded.bubble};
  --dur-fast: ${motion["duration-fast"]};
  --dur-reveal: ${motion["duration-reveal"]};
  --ease: ${motion["ease"]};
  --stagger: ${motion["stagger-step"]};
${chartVars}
}

[data-theme="dark"] {
${colorVars(dark)}
${alphaLadder(dark.foreground, steps)}
}

@media (prefers-color-scheme: dark) {
  :root:not([data-theme]) {
${colorVars(dark).replace(/^ {2}/gm, "    ")}
${alphaLadder(dark.foreground, steps).replace(/^ {2}/gm, "    ")}
  }
}
${toneCss ? `\n${toneCss}\n` : ""}
/* ---------- base ---------- */

* { box-sizing: border-box; }

html, body { margin: 0; padding: 0; overflow-x: clip; }

html { -webkit-text-size-adjust: 100%; text-size-adjust: 100%; }

body {
  background: var(--background);
  color: var(--foreground);
  font-family: var(--font-sans);
  font-size: ${t("body", "fontSize")};
  line-height: ${t("body", "lineHeight")};
  font-optical-sizing: auto;
  font-kerning: normal;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

a {
  color: var(--accent);
  text-decoration: underline;
  text-decoration-thickness: 1px;
  text-underline-offset: 0.22em;
  text-decoration-color: transparent;
}
a:hover { text-decoration-color: currentColor; }

:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
  border-radius: var(--r-inline);
}

::selection { background: var(--accent-soft); background: color-mix(in srgb, var(--accent) 22%, transparent); }

h1 {
  font-family: var(--font-display);
  font-size: ${t("h1", "fontSize")};
  line-height: ${t("h1", "lineHeight")};
  letter-spacing: calc(${t("h1", "letterSpacing")} * var(--display-tracking));
  font-weight: ${t("h1", "fontWeight")};
  margin: 0;
  text-wrap: balance;
}

@media (max-width: 380px) {
  h1 {
    font-size: ${t("h1", "mobileFontSize")};
    line-height: ${t("h1", "mobileLineHeight")};
    letter-spacing: calc(${t("h1", "mobileLetterSpacing")} * var(--display-tracking));
  }
}

h2 {
  font-family: var(--font-display);
  font-size: ${t("h2", "fontSize")};
  line-height: ${t("h2", "lineHeight")};
  letter-spacing: calc(${t("h2", "letterSpacing")} * var(--display-tracking));
  font-weight: ${t("h2", "fontWeight")};
  margin: 0 0 14px;
  text-wrap: balance;
}

h3 {
  font-family: var(--font-display);
  font-size: ${t("h3", "fontSize")};
  line-height: ${t("h3", "lineHeight")};
  letter-spacing: calc(${t("h3", "letterSpacing")} * var(--display-tracking));
  font-weight: ${t("h3", "fontWeight")};
  margin: 0 0 10px;
  text-wrap: balance;
}

p { margin: 0 0 var(--block); text-wrap: pretty; }
p:last-child { margin-bottom: 0; }

strong, b { font-weight: 620; }

section { margin-bottom: var(--section); scroll-margin-top: 24px; }

code {
  font-family: var(--font-mono);
  font-size: 0.87em;
  background: var(--a4);
  box-shadow: inset 0 0 0 1px var(--a8);
  border-radius: var(--r-inline);
  padding: 0.1em 0.38em;
}

kbd {
  font-family: var(--font-mono);
  font-size: 0.82em;
  padding: 0.08em 0.42em;
  border-radius: var(--r-inline);
  background: var(--surface);
  box-shadow: inset 0 -1px 0 var(--a20), 0 0 0 1px var(--a12);
}

pre { white-space: pre-wrap; overflow-wrap: anywhere; max-width: 100%; }
pre code { background: none; box-shadow: none; padding: 0; font-size: inherit; white-space: inherit; overflow-wrap: inherit; }

hr { border: 0; border-top: 1px solid var(--a12); margin: var(--section) 0; }

table {
  width: 100%;
  border-collapse: collapse;
  font-size: 14px;
  font-variant-numeric: tabular-nums;
}

th, td {
  text-align: left;
  padding: 11px 12px;
  border-bottom: 1px solid var(--a8);
  vertical-align: top;
}

th:first-child, td:first-child { padding-left: 4px; }
th:last-child, td:last-child { padding-right: 4px; }

thead th {
  font-size: 12px;
  letter-spacing: 0.01em;
  color: var(--text-muted);
  font-weight: 560;
  border-bottom: 1px solid var(--a20);
  white-space: nowrap;
}

tbody tr { transition: background-color var(--dur-fast) var(--ease); }
tbody tr:hover { background: var(--a4); }
tbody tr:last-child td { border-bottom: 1px solid var(--a12); }

.num { font-variant-numeric: tabular-nums; }

/* ---------- motion: choreographed moments only ---------- */
/* One-time load stagger + one-time scroll reveals. Elements render complete
 * and static by default; page-behavior opts them in only when JS
 * runs and reduced-motion is off. Nothing loops; nothing is ambient. */

@media (prefers-reduced-motion: no-preference) {
  html.js-motion .stagger > * {
    opacity: 0;
    transform: translateY(10px);
    filter: blur(4px);
    animation: rise var(--dur-reveal) var(--ease) forwards;
  }
  html.js-motion .stagger > *:nth-child(2) { animation-delay: var(--stagger); }
  html.js-motion .stagger > *:nth-child(3) { animation-delay: calc(var(--stagger) * 2); }
  html.js-motion .stagger > *:nth-child(4) { animation-delay: calc(var(--stagger) * 3); }
  html.js-motion .stagger > *:nth-child(5) { animation-delay: calc(var(--stagger) * 4); }
  html.js-motion .stagger > *:nth-child(6) { animation-delay: calc(var(--stagger) * 5); }
  html.js-motion .stagger > *:nth-child(n+7) { animation-delay: calc(var(--stagger) * 6); }

  html.js-motion .reveal {
    opacity: 0;
    transform: translateY(12px);
    filter: blur(4px);
    transition: opacity var(--dur-reveal) var(--ease), transform var(--dur-reveal) var(--ease), filter var(--dur-reveal) var(--ease);
  }
  html.js-motion .reveal.is-in { opacity: 1; transform: none; filter: none; }

  html.js-motion .reveal .bar-fill {
    transform: scaleX(0);
    transform-origin: left;
    transition: transform calc(var(--dur-reveal) * 1.6) var(--ease) 140ms;
  }
  html.js-motion .reveal.is-in .bar-fill { transform: scaleX(1); }

  a, summary, button, select, input, textarea {
    transition: color var(--dur-fast) var(--ease), background-color var(--dur-fast) var(--ease),
      border-color var(--dur-fast) var(--ease), box-shadow var(--dur-fast) var(--ease),
      text-decoration-color var(--dur-fast) var(--ease), transform var(--dur-fast) var(--ease);
  }
  button:active:not(:disabled) { transform: scale(0.97); }

  /* Smoothly open native disclosures where the browser supports it. */
  :root { interpolate-size: allow-keywords; }
  details::details-content {
    block-size: 0;
    overflow: clip;
    transition: block-size var(--dur-reveal) var(--ease), content-visibility var(--dur-reveal) allow-discrete;
  }
  details[open]::details-content { block-size: auto; }

  ::view-transition-old(root), ::view-transition-new(root) { animation-duration: 320ms; }
}

@keyframes rise {
  to { opacity: 1; transform: none; filter: none; }
}
`;

const args = process.argv.slice(2);
if (args.includes("--check")) {
  const current = readFileSync(outPath, "utf8");
  if (current !== css) {
    console.error("theme.css is stale — run: node scripts/generate-theme.mjs");
    process.exit(1);
  }
  console.log("theme.css is up to date with design-tokens.yaml");
} else {
  writeFileSync(outPath, css);
  console.log(`Wrote ${outPath} (${css.length} bytes)`);
}
