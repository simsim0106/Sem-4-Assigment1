import pandas as pd
import ast

print("Program started")

df = pd.read_csv("International_T20_Data.csv")

print("Columns:", df.columns)

# convert innings string to python object
innings = ast.literal_eval(df.loc[0,'innings_data'])

def get_scorecard(innings):

    first = innings[0]['1st innings']
    second = innings[1]['2nd innings']

    first_del = []
    for d in first['deliveries']:
        for k,v in d.items():
            first_del.append(v)

    second_del = []
    for d in second['deliveries']:
        for k,v in d.items():
            second_del.append(v)

    first_df = pd.json_normalize(first_del)
    second_df = pd.json_normalize(second_del)

    top_batters1 = first_df.groupby('batsman')['runs.batsman'].sum().sort_values(ascending=False).head(4)
    top_bowlers2 = first_df.groupby('bowler')['runs.total'].sum().sort_values().head(4)

    top_batters2 = second_df.groupby('batsman')['runs.batsman'].sum().sort_values(ascending=False).head(4)
    top_bowlers1 = second_df.groupby('bowler')['runs.total'].sum().sort_values().head(4)

    score1 = pd.DataFrame(top_batters1)
    score2 = pd.DataFrame(top_batters2)

    return score1, score2


score1, score2 = get_scorecard(innings)

print("\nScorecard - First Innings")
print(score1)

print("\nScorecard - Second Innings")
print(score2)