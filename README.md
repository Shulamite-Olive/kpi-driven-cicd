# KPI-Driven CI/CD Pipeline

This project demonstrates a continuous integration pipeline that:
- Runs automated tests using GitHub Actions
- Tracks Key Performance Indicators (KPIs) like build duration and success rate
- Uses a Python script (`tuner_github.py`) to fetch workflow metrics from GitHub’s API
- Saves metrics into `workflow_metrics.csv` for analysis
