# International Football Results Analysis

## Dataset
- **Source:** Kaggle - International Football Results (1872-2024)
- **Link:** https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017
- **File:** `data/results.csv`

---

## Project Structure

```
football_analysis/
├── data/
│   └── results.csv              # Dataset from Kaggle
├── notebooks/
│   └── Football_Analysis.ipynb  # Jupyter notebook with all analysis
├── scripts/
│   ├── data_exploration.py      # Questions 1-4: Basic Exploration
│   ├── goals_analysis.py        # Questions 5-8: Goals Analysis
│   ├── match_results.py         # Questions 9-11: Match Results
│   └── visualizations.py        # Charts and graphs
├── README.md
├── requirements.txt
└── football_visualizations.png  # Output charts
```

---

## How to Run

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Download Dataset
- Go to https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017
- Download `results.csv`
- Place in `data/` folder

### 3. Run Scripts (Command Line)
```bash
# Basic exploration (Q1-Q4)
python scripts/data_exploration.py

# Goals analysis (Q5-Q8)
python scripts/goals_analysis.py

# Match results (Q9-Q11)
python scripts/match_results.py

# Generate visualizations
python scripts/visualizations.py
```

### 4. Jupyter Notebook
```bash
jupyter notebook
# Open: notebooks/Football_Analysis.ipynb
# Run cells with Shift + Enter
```

---

## Results Summary

| Question | Answer |
|----------|--------|
| **1. Total matches** | 49,287 |
| **2. Date range** | 1872 to 2026 |
| **3. Unique countries** | 333 |
| **4. Most frequent home team** | Brazil (614 matches) |
| **5. Average goals per match** | 2.94 |
| **6. Highest scoring match** | Australia 31-0 American Samoa |
| **7. Home vs Away goals** | Home: 1.76, Away: 1.18 |
| **8. Most common total goals** | 2 goals |
| **9. Home win percentage** | 48.91% |
| **10. Home advantage exists?** | YES |
| **11. Most wins historically** | Brazil (670 wins) |

---

## Key Findings

1. **Home Advantage is Real:** Home teams win 48.91% vs away teams 28.23%
2. **Goals Distribution:** Most matches have 2-3 goals (right-skewed)
3. **Brazil Dominates:** Most frequent home team and most wins overall
4. **High Scoring Outliers:** Australia 31-0 American Samoa is the highest
5. **Consistent Pattern:** Home teams score 0.58 more goals per match on average

---

## Visualizations Produced

- **Histogram:** Distribution of total goals per match
- **Bar Chart:** Match outcomes (Home Win / Away Win / Draw)
- **Horizontal Bar Chart:** Top 10 teams by total wins
- **Comparison Chart:** Home vs Away average goals

---

## Technologies Used

- Python 3.12
- pandas 2.0+
- numpy 1.24+
- matplotlib 3.7+
- scipy 1.10+
- Jupyter Notebook

---

## Assignment Requirements Met

✅ **Step 1:** Load CSV and explore data  
✅ **Basic Exploration:** Questions 1-4 answered with code  
✅ **Goals Analysis:** Questions 5-8 answered with code  
✅ **Match Results:** Questions 9-11 answered with code  
✅ **Visualizations:** Histogram, bar charts, and team rankings  
✅ **GitHub Submission:** Clean repo structure with README  

---

## Author

[Your Name]  
[Your Student ID]  
[Course Name]  
April 2025
