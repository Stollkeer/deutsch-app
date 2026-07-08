// Copies the PWA in ../verben/ into ./www/ minus dev-only files.
// Runs on every `npm run cap:sync` so the Android build always has the latest.

const fs = require("fs");
const path = require("path");

const SRC = path.resolve(__dirname, "..", "..", "verben");
const DST = path.resolve(__dirname, "..", "www");

const SKIP = new Set([
  "__pycache__",
  "_build_nouns.py",
  "_finalize_nouns.py",
  "sw.js",
]);

function rmrf(p) {
  if (!fs.existsSync(p)) return;
  for (const name of fs.readdirSync(p)) {
    const full = path.join(p, name);
    if (fs.statSync(full).isDirectory()) {
      rmrf(full);
      fs.rmdirSync(full);
    } else {
      fs.unlinkSync(full);
    }
  }
}

function cpr(src, dst) {
  fs.mkdirSync(dst, { recursive: true });
  for (const name of fs.readdirSync(src)) {
    if (SKIP.has(name)) continue;
    const s = path.join(src, name);
    const d = path.join(dst, name);
    if (fs.statSync(s).isDirectory()) {
      cpr(s, d);
    } else {
      fs.copyFileSync(s, d);
    }
  }
}

function patchIndexForCapacitor(indexPath) {
  if (!fs.existsSync(indexPath)) return;
  let html = fs.readFileSync(indexPath, "utf8");
  const before = html;
  // Match the whole SW registration block including its inner call.
  html = html.replace(
    /if\s*\(\s*"serviceWorker"\s+in\s+navigator\s*\)\s*\{[\s\S]*?\}\s*/g,
    "/* service worker stripped for Android build */\n"
  );
  if (html !== before) {
    fs.writeFileSync(indexPath, html);
    console.log("  patched index.html (stripped service worker registration)");
  }
}

console.log(`sync: ${SRC} → ${DST}`);
rmrf(DST);
cpr(SRC, DST);
patchIndexForCapacitor(path.join(DST, "index.html"));

// count files
let n = 0;
(function walk(p) {
  for (const f of fs.readdirSync(p)) {
    const full = path.join(p, f);
    if (fs.statSync(full).isDirectory()) walk(full);
    else n++;
  }
})(DST);
console.log(`  ${n} files in www/`);
