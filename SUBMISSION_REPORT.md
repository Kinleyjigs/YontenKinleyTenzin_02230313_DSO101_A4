# DSO101 Assignment IV - Submission Report

**Student**: YontenKinleyTenzin_02230313
**Date**: 14 May 2026
**Repository**: https://github.com/Kinleyjigs/YontenKinleyTenzin_02230313_DSO101_A4
**Live App URL**: *PASTE_YOUR_RENDER_URL_HERE*

---

## Summary
This repository contains a Flask backend, unit tests (pytest), a GitHub Actions CI workflow, and automatic deployment to Render.

## What I implemented
- `app.py`: Flask app with endpoints `/`, `/health`, `/api/add`
- `test_app.py`: pytest unit tests (11 tests)
- `requirements.txt`: pinned dependencies including `Flask==2.3.3` and `Werkzeug<3.0`
- `.github/workflows/ci.yml`: CI that installs dependencies and runs `pytest`
- `Procfile`: `web: gunicorn app:app` for Render

## Evidence & Screenshots (attach these files to your submission)
Please capture and include these screenshots. Name them exactly as below.

- `screenshot_1_tests_local.png` — Local `pytest` output showing "11 passed" (run `pytest test_app.py -v`).
- `screenshot_2_flask_running.png` — Terminal showing `* Running on http://127.0.0.1:5000` (after `python app.py`).
- `screenshot_3_github_repo.png` — GitHub repo page showing files (README, app.py, test_app.py, .github/workflows/ci.yml).
- `screenshot_4_github_actions_running.png` — GitHub Actions view when workflow is running.
- `screenshot_5_github_actions_passed.png` — GitHub Actions workflow run page showing all steps passed.
- `screenshot_6_render_deploy_started.png` — Render deploy logs during build.
- `screenshot_7_render_deploy_success.png` — Render dashboard showing deployment succeeded and service URL.
- `screenshot_8_live_app_response.png` — Browser showing JSON response from `https://<your-service>.onrender.com/`.

## How to reproduce (short commands)

```bash
# clone repository
git clone https://github.com/Kinleyjigs/YontenKinleyTenzin_02230313_DSO101_A4.git
cd DSO_assign4

# create venv and install
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# run tests
pytest test_app.py -v

# run app locally
python app.py
```

## Notes on secrets
This assignment does NOT require you to commit any secret keys. If you later need secrets (API keys, DB credentials), do NOT add them to the repository. Use:

- GitHub Actions: `Settings -> Secrets and variables -> Actions` to add repository secrets
- Render: Service -> Environment -> Add environment variables

## Checklist for submission
- [ ] Repository URL submitted
- [ ] `.github/workflows/ci.yml` included in repo
- [ ] `screenshot_1_tests_local.png` attached
- [ ] `screenshot_5_github_actions_passed.png` attached
- [ ] `screenshot_7_render_deploy_success.png` attached
- [ ] Live app URL included in this file

---

## Final remarks
Paste your Render URL into the `Live App URL` field at the top of this document, attach the screenshots listed above, then commit and push this report. Once pushed, your repository will contain all required evidence for the assignment submission.

Good job — let me know if you want me to commit and push this file for you, or if you want me to prepare a zip of the repo ready for upload.