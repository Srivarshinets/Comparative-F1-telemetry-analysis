import pandas as pd

# Load CSVs
ver = pd.read_csv('../data/ver_tel.csv')
lec = pd.read_csv('../data/lec_tel.csv')

# Select required columns
cols = ['Distance', 'Speed', 'Throttle', 'Brake', 'nGear']

ver = ver[cols]
lec = lec[cols]

# Rename columns to match SQL
ver.columns = ['distance', 'speed', 'throttle', 'brake', 'gear']
lec.columns = ['distance', 'speed', 'throttle', 'brake', 'gear']

# Add driver column
ver['driver_code'] = 'VER'
lec['driver_code'] = 'LEC'

# Combine
df = pd.concat([ver, lec])

# Save clean data
df.to_csv('../data/clean_telemetry.csv', index=False)

print("Transformed data saved.")