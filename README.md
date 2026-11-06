# Ammar Aikan — Cybersecurity Portfolio

Source for [ammaraikan.web.app](https://ammaraikan.web.app), a focused cybersecurity portfolio covering selected security engineering projects, penetration-testing training, evidence-linked skills, education, and professional contact links.

## Structure

- `public/index.html` — portfolio content and project case studies
- `public/assets/styles.css` — responsive visual system
- `firebase.json` — Firebase Hosting configuration
- `.firebaserc` — Firebase project alias

The public security reports are hosted from the companion [GitHub Pages CV repository](https://github.com/AmmarAikan/AmmarAikan.github.io) so the site does not maintain duplicate large files.

## Local preview and deployment

```powershell
firebase emulators:start --only hosting
firebase deploy --only hosting
```

The portfolio contains no production secrets or private assessment evidence. Only permanently sanitized report editions are linked publicly.
