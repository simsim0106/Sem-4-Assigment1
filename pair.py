import pandas as pd
import ast

# Load dataset
df = pd.read_csv("International_T20_Data.csv")

# Convert teams column from string to list
df['teams'] = df['teams'].apply(ast.literal_eval)

# Create a column containing sorted team pairs
df['team_pair'] = df['teams'].apply(lambda x: tuple(sorted(x)))

# Count matches for each pair
pair_counts = df['team_pair'].value_counts()

# Get the pair with the most matches
top_pair = pair_counts.head(1)

print("Pair of teams who played the most T20 matches:")
print(top_pair)