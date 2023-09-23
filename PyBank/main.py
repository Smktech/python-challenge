#Import modules

import os

import csv

import pandas as pd

#capture path in variable

budget_csv=os.path.join('PyBank','Resources','budget_data.csv')

#use pandas to read data

df=pd.read_csv(budget_csv)

# Calculate the total number of months
total_months = df.shape[0]

# Calculate the net total amount of "Profit/Losses"
net_profit_losses = df['Profit/Losses'].sum()

# Calculate the changes in "Profit/Losses" over the entire period
df['Change'] = df['Profit/Losses'].diff()
average_change = df['Change'].mean()

# Find the greatest increase in profits (date and amount)
max_increase_date = df.loc[df['Change'] == df['Change'].max(), 'Date'].values[0]
max_increase_amount = df['Change'].max()

# Find the greatest decrease in profits (date and amount)
max_decrease_date = df.loc[df['Change'] == df['Change'].min(), 'Date'].values[0]
max_decrease_amount = df['Change'].min()

# Print the results
print("Total number of months:", total_months)
print("Net total amount of Profit/Losses:", net_profit_losses)
print("Average change in Profit/Losses:", average_change)
print("Greatest increase in profits:", max_increase_date, max_increase_amount)
print("Greatest decrease in profits:", max_decrease_date, max_decrease_amount)