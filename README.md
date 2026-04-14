![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-2.3-green)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey)
![Reporting](https://img.shields.io/badge/Feature-Reporting-orange)
![Workflow](https://img.shields.io/badge/Workflow-Multi--Stage-blueviolet)
![Repo Size](https://img.shields.io/github/repo-size/christiandeguzman1/it-helpdesk-ticket-automation)
![Top Language](https://img.shields.io/github/languages/top/christiandeguzman1/it-helpdesk-ticket-automation)
![Issues](https://img.shields.io/github/issues/christiandeguzman1/it-helpdesk-ticket-automation)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![Last Commit](https://img.shields.io/github/last-commit/christiandeguzman1/it-helpdesk-ticket-automation)

## Internal IT Helpdesk Ticket Automation System

## Overview
This is a web-based IT helpdesk system built using Flask and SQLite. I created it to simulate how internal IT teams track and manage support tickets.

Users can submit tickets, and the system automatically assigns a category and priority based on the issue description. On the admin side, tickets can be tracked through different stages and analyzed using built-in reports.

---

## Features

### Ticket Submission
- Submit IT support tickets through a simple form
- Automatic categorization (e.g., network, account issues, software)
- Automatic priority assignment (Low, Medium, High)

### Workflow Management
- Tickets move through multiple stages:
  - Open
  - In Progress
  - Pending Approval
  - Approved
  - Closed
- Tracks when tickets are created and resolved

### Admin Dashboard
- View all submitted tickets
- Update ticket status
- Filter tickets by status

### Reporting
- Tickets by status
- Tickets by priority
- Tickets created per day
- Average resolution time based on created and closed timestamps

### Validation
- Basic form validation on both frontend and backend to prevent empty submissions

---

## Tech Stack
- Python
- Flask
- SQLite
- HTML/CSS

---

## What I Focused On
- Designing a simple but realistic ticket workflow
- Writing SQL queries for reporting (COUNT, GROUP BY, AVG)
- Tracking ticket lifecycle using timestamps
- Keeping the system easy to understand while still being practical

---

## How to Run

## How to Run

1. Clone the repository and navigate into it:
git clone https://github.com/christiandeguzman1/it-helpdesk-ticket-automation.git
cd it-helpdesk-ticket-automation

2. Create a virtual environment:
python3 -m venv venv

3. Activate the virtual environment:
- macOS/Linux: source venv/bin/activate
- Windows: venv\Scripts\activate

4. Install dependencies:
pip install -r requirements.txt

5. Run the application:
python app.py

6. Open your browser and go to:
http://127.0.0.1:5000
