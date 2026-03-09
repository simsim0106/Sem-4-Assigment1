import ast

import pandas as pd
import numpy as np

df=pd.read_csv('International_T20_Data.csv')
df.head()

#for renaming columns
df.columns = df.columns.str.replace(".", "_")

df=df.rename(columns={
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
})
df.to_csv('International_T20_Data.csv', index=False)
print("Changes have been permanently saved to the CSV file.")

#The top three venues which hosted the greatest number of matches
top_venues = df['venue'].value_counts().head(3)
print(top_venues)


#the pair of cricket teams who played the most number of T20 matches against each other.
df['teams'] = df['teams'].apply(lambda x: x.strip("[]").replace("'", "").split(", ") if isinstance(x, str) else x)
df['team_pair'] = df['teams'].apply(lambda x: tuple(sorted(x)))
most_matches = df['team_pair'].value_counts().head(1)
print(most_matches)
df['teams'] = df['teams'].apply(lambda x: x.strip("[]").replace("'", "").split(", ") if isinstance(x,str) else x)
matches_played = df['teams'].explode().value_counts()
matches_won = df['match_winner'].value_counts()
win_percentage = (matches_won / matches_played) * 100
top_teams = win_percentage.sort_values(ascending=False).head(5)
print(top_teams)


#score card
df['innings'] = df['innings'].apply(ast.literal_eval)
def get_scorecard(innings):

    batsman_runs = {}
    bowler_wickets = {}

    for inning in innings:
        inning_data = list(inning.values())[0]

        for delivery in inning_data['deliveries']:

            ball = list(delivery.values())[0]

            batsman = ball['batsman']
            bowler = ball['bowler']
            runs = ball['runs']['batsman']

            batsman_runs[batsman] = batsman_runs.get(batsman, 0) + runs

            if 'wicket' in ball:
                bowler_wickets[bowler] = bowler_wickets.get(bowler, 0) + 1

    batsman_df = pd.DataFrame(
        batsman_runs.items(),
        columns=['Batsman','Runs']
    ).sort_values(by='Runs', ascending=False).head(4)

    bowler_df = pd.DataFrame(
        bowler_wickets.items(),
        columns=['Bowler','Wickets']
    ).sort_values(by='Wickets', ascending=False).head(4)

    return batsman_df, bowler_df

scorecard1, scorecard2 = get_scorecard(df['innings'][0])

print("Top 4 Batsmen")
print(scorecard1)

print("\nTop 4 Bowlers")
print(scorecard2)