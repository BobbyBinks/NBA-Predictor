import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import openpyxl


features= pd.read_excel("NBA Referee Assignments 2023-2024.xlsx", sheet_name="Automated")
features['Date'] = pd.to_numeric(pd.to_datetime(features['Date']))
features = pd.get_dummies(features)


book = openpyxl.load_workbook("NBA Prediction.xlsx")
sheet = book['One hot encode']
headers_df = pd.DataFrame(features)
for col in range(1, headers_df.shape[1]+1):
    sheet.cell(row=1, column=col).value = headers_df.columns[col-1]
book.save("NBA Prediction.xlsx")