# ATM Simulation System (Flask + HTML + CSS)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Framework-lightgrey.svg)](https://flask.palletsprojects.com/)
[![HTML5](https://img.shields.io/badge/HTML5-orange.svg)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-blue.svg)](https://developer.mozilla.org/en-US/docs/Web/CSS)

A simple, educational web-based ATM simulation built with Flask (Python) on the backend and HTML/CSS on the frontend. It demonstrates basic OOP concepts, secure 4-digit PIN handling, and typical ATM operations like deposit, withdraw, and balance enquiry.

---

## Live Demo
Live demo: Coming soon — you can run locally (instructions below).

---

## Features

- ✔️ Set and validate a secure 4-digit PIN  
- ✔️ Deposit funds  
- ✔️ Withdraw funds with validation (insufficient funds prevented)  
- ✔️ View current balance  
- ✔️ Clean, responsive HTML/CSS UI  
- ✔️ Simple Flask backend with in-memory storage (easy to extend to DB)

---

## Project Structure

```
Atm-Simulation-menu/
│
├── app.py                 # Main Flask app (backend)
├── requirements.txt       # Dependencies file
│
├── static/
│   └── style.css          # Custom CSS styling
│
├── templates/
│   ├── index.html         # Home page (PIN setup)
│   ├── menu.html          # ATM operations page
│
└── README.md              # Project documentation
```

---

## Tech Stack

- Frontend: HTML5, CSS3  
- Backend: Python + Flask  
- (Optional) DB: SQLite / MySQL (future improvement)  
- Deployment: GitHub + Render / Vercel or local Flask server

---

## Quick Start (Local)

1. Clone the repository
```bash
git clone https://github.com/Vivek-ML001/Atm-Simulation-menu.git
cd Atm-Simulation-menu
```

2. Create & activate a virtual environment (recommended)
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the app
```bash
python app.py
```

5. Open your browser at
http://127.0.0.1:5000/

---

## How It Works (flow)

1. User sets a 4-digit PIN on the home page.  
2. After PIN setup, the user accesses the ATM menu (deposit, withdraw, check balance).  
3. Each operation validates the PIN and updates the in-memory balance.  
4. All state is stored in memory (non-persistent) — intended for learning/demo use.

---

## Screenshots / Preview

Add screenshots in a `/screenshots` folder and reference them here:

![Preview placeholder](screenshots/preview.png)

Example:
```
/screenshots/
  ├── homepage.png
  ├── menu.png
  └── deposit.png
```

---

## Future Improvements

- Persist data with a database (SQLite / MySQL)  
- Add user accounts (login / signup)  
- Transaction history / receipt generation  
- Input validation & stronger security for production  
- CI/CD and deployment to Render/Vercel

---

## Development tips

- To enable debugging while developing:
```bash
export FLASK_ENV=development
python app.py
```
(Windows PowerShell: `setx FLASK_ENV "development"` or use environment settings.)

- Consider adding `python-dotenv` to manage environment variables.

---

## Author

Vivek Kumar  
Machine Learning Student | Tech & Web Enthusiast  


---

## License

This project is released under the MIT License. See LICENSE for details.
