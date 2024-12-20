﻿# Cloud Cost Optimization: An Analytical Project
Overview
This project focuses on simulating and analyzing cloud service usage and costs. By generating a realistic dataset and importing it into an SQLite database, we perform SQL-based analysis and Python-powered visualizations to derive insights that can help optimize cloud spending.

Key Features

Dataset Simulation:
Generates a dataset with 500 records of simulated cloud usage.
Includes fields such as service type, usage type, region, project, usage metrics, and cost.
Saved as cloud_usage_data.csv.

SQL Database Integration:
Creates an SQLite database (cloud_usage_data.db) and imports the dataset into a table (cloud_usage).
Enables efficient querying and analysis of cloud usage data.

Data Analysis and Insights:
SQL queries to extract actionable insights:
Total cost by cloud service.
Top 5 most expensive projects.
Total usage by region.
Results stored in .csv and .db formats for further use.

Visualizations:
Python visualizations generated using Matplotlib:
Total Usage by Region (total_usage_by_region.png).
Total Cost by Service (total_cost_by_service.png).
Top 5 Most Expensive Projects (top_projects_by_cost.png).

Technologies Used
Python:
Data generation and analysis with pandas and sqlite3.
Visualization with matplotlib.

SQLite:
Database for storing and querying data.

PowerShell/Command Line:
For setting up project structure and running scripts.


cloud-cost-optimization/
├── analysis/
│   ├── main.py                # Main script for dataset generation, database creation, and analysis
├── data/
│   ├── cloud_usage_data.csv   # Simulated dataset
│   ├── cloud_usage_data.db    # SQLite database
│   ├── total_usage_by_region.png        # Visualization: Usage by region
│   ├── total_cost_by_service.png        # Visualization: Cost by service
│   ├── top_projects_by_cost.png         # Visualization: Top expensive projects


How to Run the Project:

Clone the repository:
git clone https://github.com/tanzimozer/cloud-cost-optimization.git
cd cloud-cost-optimization

Set up a virtual environment and install dependencies: 
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
pip install pandas matplotlib

Run the main script:
python analysis/main.py


Outputs:

Data: cloud_usage_data.csv and cloud_usage_data.db in the data folder.
Visualizations: Saved as PNG files in the data folder.
