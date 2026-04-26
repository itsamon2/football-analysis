import pandas as pd
from scipy import stats
import sys
sys.path.append('..')
from data_exploration import load_data
from goals_analysis import analyze_goals

def match_result(row):
    if row["home_score"] > row["away_score"]:
        return "Home Win"
    elif row["home_score"] < row["away_score"]:
        return "Away Win"
    else:
        return "Draw"

def analyze_results(df):
    print("=" * 60)
    print("MATCH RESULTS")
    print("=" * 60)
    
    df['result'] = df.apply(match_result, axis=1)
    
    pct = df['result'].value_counts(normalize=True) * 100
    print(f"\n9. Home wins: {pct['Home Win']:.2f}%")
    print(f"   Away wins: {pct['Away Win']:.2f}%")
    print(f"   Draws: {pct['Draw']:.2f}%")
    
    print(f"\n10. Home advantage: {'YES' if pct['Home Win'] > pct['Away Win'] else 'NO'}")
    t, p = stats.ttest_rel(df['home_score'], df['away_score'])
    print(f"    Statistical significance (p < 0.05): {'YES' if p < 0.05 else 'NO'}")
    
    home_wins = df[df['result'] == 'Home Win']['home_team'].value_counts()
    away_wins = df[df['result'] == 'Away Win']['away_team'].value_counts()
    total_wins = home_wins.add(away_wins, fill_value=0).sort_values(ascending=False)
    print(f"\n11. Most wins: {total_wins.index[0]} ({int(total_wins.iloc[0])} wins)")
    
    return df, total_wins

if __name__ == "__main__":
    df = load_data()
    df = analyze_goals(df)
    analyze_results(df)