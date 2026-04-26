import pandas as pd
import sys
sys.path.append('..')
from data_exploration import load_data

def analyze_goals(df):
    print("=" * 60)
    print("GOALS ANALYSIS")
    print("=" * 60)
    
    df['total_goals'] = df['home_score'] + df['away_score']
    
    # Q5: Average goals
    print(f"\n5. Average goals per match: {df['total_goals'].mean():.2f}")
    
    # Q6: Highest scoring match
    max_goals = df['total_goals'].max()
    match = df[df['total_goals'] == max_goals].iloc[0]
    print(f"\n6. Highest scoring: {match['home_team']} {match['home_score']}-{match['away_score']} {match['away_team']} ({max_goals} goals)")
    
    # Q7: Home vs Away
    home_avg = df['home_score'].mean()
    away_avg = df['away_score'].mean()
    print(f"\n7. Home avg: {home_avg:.2f}, Away avg: {away_avg:.2f}")
    print(f"   More goals scored at: {'HOME' if home_avg > away_avg else 'AWAY'}")
    
    # Q8: Most common total
    common = df['total_goals'].value_counts().idxmax()
    print(f"\n8. Most common total goals: {common}")
    
    return df

if __name__ == "__main__":
    df = load_data()
    analyze_goals(df)