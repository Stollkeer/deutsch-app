# Merged app — storage schema

## Key: `polyglot_v1`

Distinct from the legacy `verben_v1`, `deutsch_app_v2`, and `francais_app_v1` keys so the migration hook can read the old data and translate it, then leave the old keys alone (as a safety net) until the user hits Reset.

## Shape

```js
{
  _schema: 1,
  active_lang: "de",       // "de" | "fr" — persists user's language choice
  langs: {
    de: {
      verbs: {
        mastered: { "sein": 1, "haben": 1 },      // KEY = headword STRING, not index
        conjMastered: { "sein|prasens|ich": 1 },  // conjugation drills — key = "verb|tense|person"
        bestStreak: 0,
        ultimate: null                              // {acc, sec, ts} or null
      },
      nouns: {
        mastered: { "Zeit": 1 },
        bestStreak: 0,
        ultimate: null,
        articleBest: 0
      }
    },
    fr: { verbs: {...}, nouns: {...} }
  },
  rank: 0,                 // global rank index (aggregates both langs)
  _migrations: {           // idempotent flags — never re-run a migration
    from_verben_v1: 0,
    from_deutsch_app_v2: 0,
    from_francais_app_v1: 0
  }
}
```

## Why headword-keyed instead of index-keyed

Old apps stored `mastered = {0: 1, 42: 1}` where `0` was the array index of the corresponding verb. Appending, inserting, or reordering verbs shifted those indices and silently corrupted saves.

Headword-keyed (`mastered = {"sein": 1}`) is stable forever. Adding verbs, reordering levels, splitting/merging levels — none of it touches existing progress. Only *removing* a headword drops that entry, which is the correct behavior anyway.

## Migration chain

On first load after upgrading:

1. Read `verben_v1` (Deutsch original verbs-only build). If present + `_migrations.from_verben_v1 === 0`:
   - For each numeric index `k` in `old.mastered`: look up the current `LANG_DATA.de.verbs[k].de` → headword → set `polyglot_v1.langs.de.verbs.mastered[headword] = 1`.
   - Also copy `bestStreak`, `ultimate`.
   - Set `_migrations.from_verben_v1 = 1`.
2. Read `deutsch_app_v2` (Deutsch verbs+nouns build). Same pattern for both verbs and nouns tracks.
3. Read `francais_app_v1` (French app). Same pattern under `langs.fr`.
4. Save. Legacy keys are left in place as recovery.

Migration is idempotent — flags prevent double-running. Safe across multiple app updates.

## Future updates without progress loss

Because keys are stable strings:

- **Adding a verb**: no impact. `mastered` map unaffected.
- **Renaming a verb (e.g. spelling fix)**: existing progress on the old spelling silently drops. Add a `rename_map` in the migration hook if needed: `if (old_headword in mastered) mastered[new_headword] = mastered[old_headword]; delete mastered[old_headword]`.
- **Reordering levels**: no impact.
- **Removing a verb**: mastered entry orphaned; harmless (never read again). Optionally purged on migration.
- **Adding a new tense to the conjugation game**: no impact on existing `conjMastered` (keys are `verb|tense|person`, so new tenses just start empty).
- **Schema evolution**: bump `_schema`, add another migration.

## APK update path

- Keep appId `com.pedro31f.deutsch` on the merged APK.
- Bump `versionCode` on each release (Android's update mechanism keys on this).
- Android preserves the WebView `localStorage` sandbox across app updates for the same appId — the migration hook runs on first launch of the new version, translates old data, and the user keeps their progress.

## PWA update path

- Same origin (`stollkeer.github.io/deutsch-app/`) → same `localStorage` jar. Old DE users get the migration on their next visit.
- Old `stollkeer.github.io/francais-app/` origin is separate — FR PWA users don't auto-migrate. If needed, add a small link on the FR app pointing to the merged deploy.
