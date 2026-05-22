import pandas as pd
import mysql.connector

# -------------------------------
# 1. Connect to MySQL
# -------------------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="H@rekrishna47", 
    database="f1"
)

cursor = conn.cursor()

print("Connected to MySQL")

# -------------------------------
# 2. Load CSV files
# -------------------------------
ver_df = pd.read_csv('../data/ver_tel.csv')
lec_df = pd.read_csv('../data/lec_tel.csv')

# -------------------------------
# 3. Add driver code column
# -------------------------------
ver_df['driver_code'] = 'VER'
lec_df['driver_code'] = 'LEC'

# -------------------------------
# 4. Select and reorder columns
# -------------------------------
ver_df = ver_df[['driver_code', 'Distance', 'Speed', 'Throttle', 'Brake', 'nGear']]
lec_df = lec_df[['driver_code', 'Distance', 'Speed', 'Throttle', 'Brake', 'nGear']]

# -------------------------------
# 5. Insert data into MySQL
# -------------------------------
insert_query = """
INSERT INTO telemetry (driver_code, distance, speed, throttle, brake, gear)
VALUES (%s, %s, %s, %s, %s, %s)
"""

# Insert VER data
for _, row in ver_df.iterrows():
    cursor.execute(insert_query, tuple(row))

# Insert LEC data
for _, row in lec_df.iterrows():
    cursor.execute(insert_query, tuple(row))

# -------------------------------
# 6. Commit and close
# -------------------------------
conn.commit()

print("Data inserted successfully")

cursor.close()
conn.close()