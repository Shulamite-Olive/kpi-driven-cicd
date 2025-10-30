import requests
import os
import csv
from datetime import datetime

# GitHub repository info
OWNER = "Shulamite-Olive"
REPO = "kpi-driven-cicd"
TOKEN = os.getenv("GITHUB_TOKEN")

# Headers for GitHub API authentication
headers = {"Authorization": f"token {TOKEN}"}

# Get the latest workflow run
url = f"https://api.github.com/repos/{OWNER}/{REPO}/actions/runs?per_page=1"
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    run = data["workflow_runs"][0]

    print(f"Workflow: {run['name']}")
    print(f"Status: {run['conclusion']}")
    print(f"Started at: {run['run_started_at']}")
    print(f"Updated at: {run['updated_at']}")

    # Calculate duration in seconds
    start_time = datetime.strptime(run['run_started_at'], "%Y-%m-%dT%H:%M:%SZ")
    end_time = datetime.strptime(run['updated_at'], "%Y-%m-%dT%H:%M:%SZ")
    duration_sec = (end_time - start_time).total_seconds()

    # Save metrics to CSV
    csv_file = "workflow_metrics.csv"
    file_exists = os.path.isfile(csv_file)

    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["run_id", "workflow_name", "status", "duration_sec", "started_at", "updated_at"])
        writer.writerow([run["id"], run["name"], run["conclusion"], duration_sec, run["run_started_at"], run["updated_at"]])

    print(f"Metrics saved to {csv_file}")

else:
    print("Failed to fetch workflow data:", response.status_code)
