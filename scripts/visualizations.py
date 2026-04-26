import matplotlib.pyplot as plt
import sys
sys.path.append('..')

from data_exploration import load_data
from goals_analysis import analyze_goals
from match_results import analyze_results

def create_visualizations(df, total_wins):
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    
    # 1. Goals histogram
    df['total_goals'].hist(bins=15, ax=axes[0,0], color='skyblue', edgecolor='black')
    axes[0,0].set_title('Distribution of Goals Per Match', fontsize=14, fontweight='bold')
    axes[0,0].set_xlabel('Total Goals')
    axes[0,0].set_ylabel('Number of Matches')
    
    # 2. Results bar chart
    result_counts = df['result'].value_counts()
    colors = ['#ff6b6b', '#4ecdc4', '#ffe66d']
    axes[0,1].bar(result_counts.index, result_counts.values, color=colors, edgecolor='black')
    axes[0,1].set_title('Match Outcomes', fontsize=14, fontweight='bold')
    axes[0,1].set_ylabel('Number of Matches')
    
    # 3. Top 10 wins - FIX LABELS
    top_10 = total_wins.head(10).sort_values(ascending=True)  # Sort for better display
    axes[1,0].barh(range(len(top_10)), top_10.values, color='lightgreen', edgecolor='black')
    axes[1,0].set_yticks(range(len(top_10)))
    axes[1,0].set_yticklabels(top_10.index)
    axes[1,0].set_title('Top 10 Teams by Total Wins', fontsize=14, fontweight='bold')
    axes[1,0].set_xlabel('Number of Wins')  # FIX: was showing 'home_team'
    
    # 4. Home vs Away
    axes[1,1].bar(['Home', 'Away'], [df['home_score'].mean(), df['away_score'].mean()], 
                  color=['coral', 'lightblue'], edgecolor='black')
    axes[1,1].set_title('Average Goals: Home vs Away', fontsize=14, fontweight='bold')
    axes[1,1].set_ylabel('Average Goals per Match')
    
    plt.tight_layout()
    plt.savefig('../football_visualizations.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("✅ Saved: football_visualizations.png")

if __name__ == "__main__":
    df = load_data()
    df = analyze_goals(df)
    df, total_wins = analyze_results(df)
    create_visualizations(df, total_wins)