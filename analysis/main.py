import pandas as pd
import sqlite3
import random
import os

# Step 1: Ensure the data folder exists
data_folder = "../data"
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

# Step 2: Simulate dataset
random.seed(42)
services = ["EC2", "S3", "Lambda", "RDS", "DynamoDB"]
usage_types = ["Compute", "Storage", "Networking", "Database"]
regions = ["us-east-1", "us-west-1", "eu-west-1", "ap-southeast-1"]
projects = ["Project A", "Project B", "Project C", "Project D"]

data = []
for _ in range(500):  # Create 500 rows of data
    service = random.choice(services)
    usage_type = random.choice(usage_types)
    region = random.choice(regions)
    project = random.choice(projects)
    usage_metric = round(random.uniform(10, 1000), 2)  # Simulated usage
    cost = round(usage_metric * random.uniform(0.1, 0.5), 2)  # Simulated cost
    billing_period = f"2024-{random.randint(1, 12):02d}-01"  # Random month in 2024
    data.append([service, usage_type, region, project, usage_metric, cost, billing_period])

df = pd.DataFrame(data, columns=["Service", "UsageType", "Region", "Project", "UsageMetric", "Cost", "BillingPeriod"])

# Step 3: Save to CSV
csv_path = "../data/cloud_usage_data.csv"
df.to_csv(csv_path, index=False)
print(f"Simulated dataset saved to '{csv_path}'")

# Step 4: Create SQLite Database and Import Data
db_path = "../data/cloud_usage_data.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create the table
cursor.execute("""
CREATE TABLE IF NOT EXISTS cloud_usage (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    service TEXT,
    usage_type TEXT,
    region TEXT,
    project TEXT,
    usage_metric REAL,
    cost REAL,
    billing_period TEXT
)
""")
print("Table 'cloud_usage' created successfully!")

# Insert data from the DataFrame into the database
for _, row in df.iterrows():
    cursor.execute("""
    INSERT INTO cloud_usage (service, usage_type, region, project, usage_metric, cost, billing_period)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (row['Service'], row['UsageType'], row['Region'], row['Project'], row['UsageMetric'], row['Cost'], row['BillingPeriod']))

# Commit and close the database connection
conn.commit()
conn.close()
print(f"Data successfully imported into SQLite database '{db_path}'")

import matplotlib.pyplot as plt

# Reconnect to the database
conn = sqlite3.connect("../data/cloud_usage_data.db")

# Query 1: Total usage by region
query1 = """
SELECT region, SUM(usage_metric) AS total_usage
FROM cloud_usage
GROUP BY region
ORDER BY total_usage DESC
"""
df_usage = pd.read_sql_query(query1, conn)

# Plot Total Usage by Region
plt.figure(figsize=(8, 6))
plt.bar(df_usage['region'], df_usage['total_usage'], color='skyblue')
plt.title("Total Usage by Region")
plt.xlabel("Region")
plt.ylabel("Total Usage")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../data/total_usage_by_region.png")
print("Saved 'total_usage_by_region.png'")

# Query 2: Total cost by service
query2 = """
SELECT service, SUM(cost) AS total_cost
FROM cloud_usage
GROUP BY service
ORDER BY total_cost DESC
"""
df_cost = pd.read_sql_query(query2, conn)

# Plot Total Cost by Service
plt.figure(figsize=(8, 6))
plt.bar(df_cost['service'], df_cost['total_cost'], color='orange')
plt.title("Total Cost by Service")
plt.xlabel("Service")
plt.ylabel("Total Cost")
plt.tight_layout()
plt.savefig("../data/total_cost_by_service.png")
print("Saved 'total_cost_by_service.png'")

# Query 3: Top 5 most expensive projects
query3 = """
SELECT project, SUM(cost) AS total_cost
FROM cloud_usage
GROUP BY project
ORDER BY total_cost DESC
LIMIT 5
"""
df_projects = pd.read_sql_query(query3, conn)

# Plot Top 5 Most Expensive Projects
plt.figure(figsize=(8, 6))
plt.barh(df_projects['project'], df_projects['total_cost'], color='green')
plt.title("Top 5 Most Expensive Projects")
plt.xlabel("Total Cost")
plt.ylabel("Project")
plt.tight_layout()
plt.savefig("../data/top_projects_by_cost.png")
print("Saved 'top_projects_by_cost.png'")

# Close the connection
conn.close()
