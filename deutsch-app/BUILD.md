# Building the Deutsch APK

Two paths — pick one. **CI is recommended: zero local tooling.**

---

## Path A — GitHub Actions (recommended, no local Android tools)

The workflow at `.github/workflows/build-apk.yml` (repo root, one level up
from this folder) builds the APK on Google's servers whenever you push
changes under `verben/` or `deutsch-app/`.

### First push

From the repo root `App alemão/`:

```bash
git init
git add .
git commit -m "Initial commit: PWA + Capacitor Android wrapper"
gh repo create deutsch-app --private --source=. --remote=origin --push
```

(or use the GitHub website to create an empty repo and follow its
`git remote add origin ... && git push` snippet if you don't have `gh`.)

### Every rebuild after that

```bash
git add -A
git commit -m "whatever changed"
git push
```

Then on GitHub → **Actions** tab → click the latest run → scroll down to
**Artifacts** → download `Deutsch-debug-apk.zip` → unzip → sideload the
APK to your phone.

You can also trigger a build manually: **Actions → Build Deutsch APK → Run workflow**.

---

## Path B — Build locally (only if you want to iterate offline)

One-time: install Node 18+, Android Studio (or the SDK command-line tools),
and JDK 17.

```bash
npm install
npm run cap:sync
npm run cap:open   # opens Android Studio
```

In Android Studio: **Build → Build Bundle(s) / APK(s) → Build APK(s)**.
Output at `android/app/build/outputs/apk/debug/app-debug.apk`.

Or headless:

```bash
cd android
./gradlew assembleDebug    # macOS/Linux
gradlew.bat assembleDebug  # Windows
```

---

## Release (signed) APK

Only needed when you want to publish or install a stable version that
Android won't overwrite on the next debug build.

1. Generate a keystore once and keep it safe:
   ```bash
   keytool -genkey -v -keystore deutsch-release.keystore \
     -alias deutsch -keyalg RSA -keysize 2048 -validity 10000
   ```
2. In Android Studio: **Build → Generate Signed Bundle / APK → APK**,
   pick the keystore, choose **release**, tick V1 + V2 signatures, finish.
   Output: `android/app/release/app-release.apk`.

---

## When to re-run `npm run cap:sync`

Any time `../verben/` changes (new words, CSS tweak, icon swap). Path A
does this automatically inside the workflow. Path B needs it before you
click Build.

## Icons / splash

Regenerate from `deutsch-app/resources/icon.png` and
`icon-foreground.png`:

```bash
npx capacitor-assets generate --android
```

## Colors

Dark theme `#131420` lives in
`android/app/src/main/res/values/colors.xml` and `styles.xml`. Change
both files to rebrand.

## Package id

`com.pedro31f.deutsch` — set in `capacitor.config.json` and mirrored in
`android/app/build.gradle` (applicationId) and `strings.xml`. Change all
three and re-sync.
