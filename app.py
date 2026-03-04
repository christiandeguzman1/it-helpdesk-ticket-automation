from flask import Flask, render_template, request, redirect, url_for
from database import HelpdeskDB
from datetime import datetime

app = Flask(__name__)
db = HelpdeskDB()
db.create_table()

def get_category(description):
    desc = description.lower()
    if "password" in desc:
        return "Account Issues"
    elif "network" in desc or "wifi" in desc:
        return "Network"
    elif "error" in desc:
        return "Software"
    else:
        return "General"

def get_priority(description):
    desc = description.lower()
    if "urgent" in desc or "down" in desc:
        return "High"
    elif "slow" in desc:
        return "Medium"
    else:
        return "Low"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit_ticket():
    name = request.form.get("name", "").strip()
    description = request.form.get("description", "").strip()
    category = get_category(description)
    priority = get_priority(description)
    status = "Open"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    db.insert_ticket(name, description, category, priority, status, timestamp)
    return redirect(url_for("index"))

@app.route("/admin")
def admin():
    tickets = db.fetch_all_tickets()
    return render_template("admin.html", tickets=tickets)

@app.route("/update/<int:ticket_id>", methods=["POST"])
def update_ticket(ticket_id):
    new_status = request.form.get("status", "Open")
    db.update_ticket_status(ticket_id, new_status)
    return redirect(url_for("admin"))

if __name__ == "__main__":
    app.run(debug=True)