import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import openpyxl

features_winner = pd.read_excel("NBA Referee Assignments 2023-2024.xlsx", sheet_name="Automated")
features_winner['Date'] = pd.to_numeric(pd.to_datetime(features_winner['Date']))
features_winner.drop(columns=['Away Score','Home Score','Away Turnover Differential','Away Offensive Rebounds','Away free throw','Away Assists on field goal','Home Turnover Differential','Home Offensive Rebounds','Home free throw','Home Assists on field goal'], inplace=True)
features_winner = pd.get_dummies(features_winner)

# Labels_Winner are the values we want to predict
labels_winner = np.array(features_winner['Winner'])
# Remove the labels from the features
# axis 1 refers to the columns
features_winner= features_winner.drop(['Winner'], axis = 1)
features_w=features_winner
# Saving feature names for later use
feature_list_winner = list(features_winner.columns)
# Convert to numpy array
features_winner = np.array(features_winner)
# Split the data into training and testing sets
train_features_winner, test_features_winner, train_labels_winner, test_labels_winner = train_test_split(features_winner, labels_winner, test_size = 0.25, random_state = 42)

#print('Training Features Shape:', train_features.shape)
#print('Training Labels Shape:', train_labels.shape)
#print('Testing Features Shape:', test_features.shape)
#print('Testing Labels Shape:', test_labels.shape)


# Instantiate model with 1000 decision trees
rf_winner = RandomForestRegressor(n_estimators = 1000, random_state = 42)
# Train the model on training data
rf_winner.fit(train_features_winner, train_labels_winner);

#Repeat for Home score
features_homescore = pd.read_excel("NBA Referee Assignments 2023-2024.xlsx", sheet_name="Automated")
features_homescore['Date'] = pd.to_numeric(pd.to_datetime(features_homescore['Date']))
features_homescore.drop(columns=["Winner","Away Score","Away Turnover Differential","Away Offensive Rebounds","Away free throw","Away Assists on field goal","Home Turnover Differential","Home Offensive Rebounds","Home free throw","Home Assists on field goal"], inplace=True)
features_homescore = pd.get_dummies(features_homescore)
labels_homescore = np.array(features_homescore['Home Score'])
features_homescore= features_homescore.drop(['Home Score'], axis = 1)
features_h=features_homescore
feature_list_homescore = list(features_homescore.columns)
features_homescore = np.array(features_homescore)
train_features_homescore, test_features_homescore, train_labels_homescore, test_labels_homescore = train_test_split(features_homescore, labels_homescore, test_size = 0.25, random_state = 42)
rf_homescore = RandomForestRegressor(n_estimators = 1000, random_state = 42)
rf_homescore.fit(train_features_homescore, train_labels_homescore);

#Repeat for Away score
features_awayscore = pd.read_excel("NBA Referee Assignments 2023-2024.xlsx", sheet_name="Automated")
features_awayscore['Date'] = pd.to_numeric(pd.to_datetime(features_awayscore['Date']))
features_awayscore.drop(columns=["Winner","Home Score","Away Turnover Differential","Away Offensive Rebounds","Away free throw","Away Assists on field goal","Home Turnover Differential","Home Offensive Rebounds","Home free throw","Home Assists on field goal"], inplace=True)
features_awayscore = pd.get_dummies(features_awayscore)
labels_awayscore = np.array(features_awayscore['Away Score'])

features_awayscore= features_awayscore.drop(['Away Score'], axis = 1)
features_a=features_awayscore
feature_list_awayscore = list(features_awayscore.columns)
features_awayscore = np.array(features_awayscore)
train_features_awayscore, test_features_awayscore, train_labels_awayscore, test_labels_awayscore = train_test_split(features_awayscore, labels_awayscore, test_size = 0.25, random_state = 42)
rf_awayscore = RandomForestRegressor(n_estimators = 1000, random_state = 42)
rf_awayscore.fit(train_features_awayscore, train_labels_awayscore);

# Use the forest's predict method on the test data
##predictions = rf.predict(test_features)
# Calculate the absolute errors
##errors = abs(predictions - test_labels)
# Print out the mean absolute error (mae)
##print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')

# Calculate mean absolute percentage error (MAPE)
##mape = 100 * (errors / test_labels)
# Calculate and display accuracy
##accuracy = 100 - np.mean(mape)
##print('Accuracy:', round(accuracy, 2), '%.')

input_winner = pd.read_excel("NBA prediction.xlsx", sheet_name="One hot encode")
input_winner.drop(columns=["Away Score","Home Score","Away Turnover Differential","Away Offensive Rebounds","Away free throw","Away Assists on field goal","Home Turnover Differential","Home Offensive Rebounds","Home free throw","Home Assists on field goal"], inplace=True)
input_winner['Date'] = pd.to_numeric(pd.to_datetime(input_winner['Date']))
row_winner = input_winner.iloc[0].to_dict()
cols_winner = list(row_winner.keys())
temp=cols_winner.pop(1)

input_awayscore = pd.read_excel("NBA prediction.xlsx", sheet_name="One hot encode")
input_awayscore.drop(columns=["Winner","Away Score","Away Turnover Differential","Away Offensive Rebounds","Away free throw","Away Assists on field goal","Home Turnover Differential","Home Offensive Rebounds","Home free throw","Home Assists on field goal"], inplace=True)
input_awayscore['Date'] = pd.to_numeric(pd.to_datetime(input_awayscore['Date']))
row_awayscore = input_awayscore.iloc[0].to_dict()
cols_awayscore = list(row_awayscore.keys())
temp=cols_awayscore.pop(1)

input_homescore = pd.read_excel("NBA prediction.xlsx", sheet_name="One hot encode")
input_homescore.drop(columns=["Winner","Home Score","Away Turnover Differential","Away Offensive Rebounds","Away free throw","Away Assists on field goal","Home Turnover Differential","Home Offensive Rebounds","Home free throw","Home Assists on field goal"], inplace=True)
input_homescore['Date'] = pd.to_numeric(pd.to_datetime(input_homescore['Date']))
row_homescore = input_homescore.iloc[0].to_dict()
cols_homescore = list(row_homescore.keys())
temp=cols_homescore.pop(1)


data_winner = input_winner[cols_winner]
newdata_winner =data_winner.values
data_awayscore = input_awayscore[cols_awayscore]
newdata_awayscore =data_awayscore.values
data_homescore = input_homescore[cols_homescore]
newdata_homescore =data_homescore.values

# make a prediction
result_winner = rf_winner.predict(newdata_winner)
result_homescore = rf_homescore.predict(newdata_homescore)
result_awayscore = rf_awayscore.predict(newdata_awayscore)

zipped_lists = zip(result_winner, result_homescore,result_awayscore)
for items in zipped_lists:
    print(items[0],items[1],items[2])

#input = pd.read_excel("NBA prediction.xlsx", sheet_name="One hot encode")
#input['Date'] = pd.to_numeric(pd.to_datetime(input['Date']))
#data = input[[]]
#new_data = data.values
# make a prediction
#result = rf.predict(new_data)
#print(result)