# Ammar Aikan — main professional portfolio

Static portfolio hosted on Firebase at https://ammaraikan.web.app/. This is distinct from the CV website at https://ammaraikan.github.io/#profile.

The rebuild uses the selected paper/evergreen design, original portrait and73categorized collection entries including labs, research, archives and references. These are not73independently completed products. Team/fork/coursework attribution and evidence limits are retained.

`public/` is the Firebase output. Preview with `python -m http.server 8787 --directory public`. Run `python .github/scripts/check_site.py` for local asset/anchor/PDF checks. The Website checks workflow runs static validation; manual dispatch additionally verifies public HTML/PDF bytes against the checked-out commit.

Professional facts originate in the private Career Branding Workspace shared content source. Only approved public fields are exported to `public/assets/projects.json`; confidential discovery records, original assessment evidence and credentials are excluded. PDF and DOCX copies match the separate CV website. Source regeneration and evidence hashes are recorded in the workspace; update facts there before rebuilding both sites.

Deploy existing hosting with `firebase deploy --only hosting --project ammaraikan`. Do not change the hosting target or treat a successful deployment command as live verification. Public reports remain linked to the separately reviewed GitHub Pages editions. Official Bootstrap Icons and Manrope font licenses are shipped with their assets.
