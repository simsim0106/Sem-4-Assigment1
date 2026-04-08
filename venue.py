# Find the top three venues which hosted the greatest number of matches
import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv('International_T20_Data.csv')

# Rename columns to remove dots
df.columns = df.columns.str.replace('.', '_')

# Rename venue column for easier use
df.rename(columns={'info_venue': 'venue'}, inplace=True)

# Find top 3 venues
top_venues = df['venue'].value_counts().head(3)

print("Top three venues with the greatest number of matches:")
print(top_venues)