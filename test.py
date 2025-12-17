import pandas as pd
from src.sheets import push_to_sheets

df = pd.read_csv("data/qualified_leads.csv")
push_to_sheets(df, "3D In-Vitro Lead Scoring Output")
