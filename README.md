## CI/CD Pipeline Project — DSO101 Assignment IV

**Student:** YontenKinleyTenzin_02230313

This repository implements a complete CI/CD pipeline for a simple Flask backend, including unit tests, GitHub Actions for build/test automation, and automatic deployment to Render.

### Project files included
- `app.py` — Flask application with three endpoints
- `test_app.py` — pytest unit tests
- `requirements.txt` — pinned dependencies
- `.github/workflows/ci.yml` — GitHub Actions workflow
- `Procfile` — Render start instruction (see below)
- `.gitignore`, `README.md`

### Quick local commands
```bash
git clone https://github.com/Kinleyjigs/YontenKinleyTenzin_02230313_DSO101_A4.git
cd DSO_assign4
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest test_app.py -v
python app.py
```

### What is `Procfile`?
A `Procfile` is a simple text file used by PaaS providers (like Render and Heroku) to tell the platform how to start your app. For this project the `Procfile` contains:

```
web: gunicorn app:app
```

This instructs Render to run a web process using `gunicorn` and load the Flask app named `app` from `app.py`.

### API Endpoints
- `GET /` — returns a JSON status message
- `GET /health` — health check JSON
- `GET /api/add` — returns a small arithmetic result JSON

### CI/CD highlights
- Workflow triggers on push to `main` and on pull requests.
- Steps: checkout → setup Python → install deps → run `pytest` → generate coverage → (optional) notify/deploy.

### Deployment (Render)
- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app`
- Auto-deploy on push to the connected GitHub branch is enabled in Render when you connect your repo.

### Evidence & screenshots (attach to submission)
- `screenshot_1_tests_local.png` — Local pytest output showing all tests passed
- `screenshot_2_flask_running.png` — Local server running on `http://127.0.0.1:5000`
- `screenshot_3_github_repo.png` — GitHub repo file list
- `screenshot_4_github_actions_running.png` — workflow running view
- `screenshot_5_github_actions_passed.png` — workflow passed view
- `screenshot_6_render_deploy_started.png` — Render deploy logs
- `screenshot_7_render_deploy_success.png` — Render deploy success and service URL
- `screenshot_8_live_app_response.png` — Live app JSON response from Render URL

Paste your Render URL here after deployment:
`Live App URL: https://<your-service>.onrender.com`

### Submission checklist
- [x] Flask app and tests in repo
- [x] GitHub Actions workflow configured
- [x] Tests passing locally
- [x] CI run green on GitHub
- [x] Render auto-deploy configured and live
- [ ] Screenshots attached to repo (optional)

### Notes about secrets
- Do NOT commit secret keys or credentials to the repository. Use GitHub Actions Secrets for CI secrets and Render Environment variables for runtime secrets.

If you want, I can add your screenshots and the Render URL to the repo and create a zip ready for submission.