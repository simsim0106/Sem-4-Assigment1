import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv('International_T20_Data.csv')

# Replace '.' with '_'
df.columns = df.columns.str.replace('.', '_')

# Rename columns
df.rename(columns={
    'meta_data_version':'data_version',
    'meta_created':'created_date',
    'meta_revision':'revision',
    'info_dates':'match_date',
    'info_gender':'gender',
    'info_match_type':'match_type',
    'info_match_type_number':'match_number',
    'info_overs':'overs',
    'info_teams':'teams',
    'info_venue':'venue',
    'info_city':'city',
    'info_umpires':'umpires',
    'info_player_of_match':'player_of_match',
    'info_toss_winner':'toss_winner',
    'info_toss_decision':'toss_decision',
    'info_outcome_winner':'match_winner',
    'info_outcome_by_runs':'win_by_runs',
    'info_outcome_by_wickets':'win_by_wickets',
    'info_outcome_method':'result_method',
    'info_outcome_result':'match_result',
    'info_outcome_eliminator':'eliminator',
    'info_outcome_bowl_out':'bowl_out',
    'info_neutral_venue':'neutral_venue'
}, inplace=True)

# Save file
df.to_csv('International_T20_Data.csv', index=False)

print("Changes have been permanently saved to the CSV file.")