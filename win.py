import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv('International_T20_Data.csv')

# Remove dots from column names
df.columns = df.columns.str.replace('.', '_')

# Rename columns if needed
df.rename(columns={
    'info_teams': 'teams',
    'info_outcome_winner': 'match_winner'
}, inplace=True)

# Split teams column into team1 and team2
teams_split = df['teams'].str.strip('[]').str.replace("'", "").str.split(',', expand=True)

df['team1'] = teams_split[0].str.strip()
df['team2'] = teams_split[1].str.strip()

# Calculate matches played
matches_played = pd.concat([df['team1'], df['team2']]).value_counts()

# Calculate matches won
matches_won = df['match_winner'].value_counts()

# Create dataframe
team_stats = pd.DataFrame({
    'matches_played': matches_played,
    'matches_won': matches_won
}).fillna(0)

# Calculate win percentage
team_stats['win_percentage'] = (team_stats['matches_won'] / team_stats['matches_played']) * 100

# Top 5 teams
top5 = team_stats.sort_values(by='win_percentage', ascending=False).head(5)

print("Top five teams by win percentage:")
print(top5)