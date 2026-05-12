# Flask Authentication Web App

A beginner-friendly Flask web application with user registration, login, sessions, protected routes, SQLite storage, and a small JSON API.

## Project Structure

```text
.
├── app.py
├── config.py
├── extensions.py
├── requirements.txt
├── routes/
├── models/
├── templates/
└── static/
```

## Run Locally

1. Create a virtual environment:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Install dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

3. Create your local environment file:

   ```powershell
   Copy-Item .env.example .env
   ```

4. Start the app:

   ```powershell
   python -m flask --app app run --debug
   ```

   On Windows, you can also use the included runner:

   ```powershell
   .\run.bat
   ```

5. Open the app in your browser:

   ```text
   http://127.0.0.1:5000
   ```

The SQLite database is created automatically at `instance/app.db` the first time the app starts.

## Common VS Code Fix

If you see `ModuleNotFoundError: No module named 'dotenv'`, VS Code is using a Python interpreter that does not have this project's packages installed.

Use one of these fixes:

```powershell
.\.venv\Scripts\python.exe -m flask --app app run --debug
```

or install the dependencies into your selected Python:

```powershell
python -m pip install -r requirements.txt
```

## Useful Routes

- `/` - home page
- `/register` - create an account
- `/login` - log in
- `/logout` - log out
- `/dashboard` - protected dashboard
- `/api/user` - JSON endpoint for the logged-in user
