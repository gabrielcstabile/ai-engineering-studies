import sqlite3
import pandas as pd

conn = sqlite3.connect('web.db')

df = pd.read_csv('analysis-pandas-sql/data/bd_data.csv', index_col=0)
df.index.name = 'index_name'
df.to_sql('data', conn, index_label='index_name')

