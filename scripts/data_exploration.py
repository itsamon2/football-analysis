import pandas as pd

def load_data(filepath='../data/results.csv'):
    df = pd.read_csv(filepath)
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    return df

def basic_exploration(df):
    print("=" * 60)
    print("BASIC EXPLORATION")
    print("=" * 60)
    
    # Q1: Total matches
    print(f"\n1. Total matches: {len(df)}")
    
    # Q2: Date range
    print(f"\n2. Date range: {df['year'].min()} to {df['year'].max()}")
    
    # Q3: Unique countries
    unique = pd.concat([df['home_team'], df['away_team']]).unique()
    print(f"\n3. Unique countries: {len(unique)}")
    
    # Q4: Most frequent home team
    top_home = df['home_team'].value_counts().head(1)
    print(f"\n4. Most frequent home team: {top_home.index[0]} ({top_home.iloc[0]} matches)")
    
    return df

if __name__ == "__main__":
    df = load_data()
    basic_exploration(df)