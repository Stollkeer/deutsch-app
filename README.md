# Deutsch — German Verbs & Nouns Trainer

A small PWA / Android app for learning **120 core German verbs** and **1000 core German nouns** (everyday words plus a heavier-than-usual dose of philosophy and humanities vocabulary — *Sein*, *Dasein*, *Aufklärung*, *Dialektik*, *Warenfetisch*…).

Everything is translated into **English, French and Portuguese**, so you can drill in whichever language you think best.

> **Live app:** https://stollkeer.github.io/deutsch-app/
> Add it to your home screen (iOS/Android → Share → *Add to Home Screen*) and it behaves like a real installed app, works offline.

## What's inside

- **Flashcards** — flip cards with conjugations / articles / plurals + translations
- **Learn mode** — cycle through a track at your own pace
- **Drill** — timed quiz over any scope (starting level, single level, or everything)
- **Article mode** — pure der/die/das training on the noun track
- **Ultimate mode** — boss run across the whole catalogue
- **Catalogue** — searchable word list with translations
- **XP + rank system** — from *Anfänger* up to *Philosoph* at 1120 mastered items, stored locally per browser

No accounts, no server, no tracking. Progress lives in `localStorage`.

## Two ways to use it

| I want to… | Do this |
|---|---|
| **Just use it in a browser / phone** | Open https://stollkeer.github.io/deutsch-app/ — install as a PWA if you want it on your home screen. |
| **Have it as a real Android app (APK)** | Grab the latest `Deutsch-debug-apk` artifact from [Actions](https://github.com/Stollkeer/deutsch-app/actions), unzip, sideload. |

## Repo layout

```
verben/         Static PWA — HTML/CSS/JS + word data. This is what gets deployed to Pages.
deutsch-app/    Capacitor wrapper that turns verben/ into an Android APK.
.github/        CI workflows — one builds the APK, one deploys the PWA to Pages.
```

## Building the APK

See [`deutsch-app/BUILD.md`](deutsch-app/BUILD.md). Short version: any push to `main` under `verben/` or `deutsch-app/` triggers a GitHub Actions build; the debug APK lands in the run's artifacts. No local Android tooling required.

## Regenerating the noun list

The 1000 nouns are curated per level in `verben/_build_nouns.py` and finalized (de-duplicated, padded) by `verben/_finalize_nouns.py`, which writes `verben/noun-data.js`. Run those two scripts if you edit the source pools.

## License

Personal project. No warranty. Use for learning.
