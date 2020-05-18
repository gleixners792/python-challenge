# -*- coding: utf-8 -*-
"""
Created on Thu May 14 22:36:46 2020

@author: gleix
"""

# OS Module to allow us to create paths across operating systems.
import os

# Module for reading CSV files
import csv

csvpath = r"C:\Users\gleix\git\python-challenge\PyBank\Resources\Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv"

Monthcnt = 0
Averagecnt = 0
TotalChange = 0
GreatestIncrease = 0
GreatestDecrease = 0
DateGreatestIncrease = " "
DateGreatestDecrease = " "
ProfitChange = 0
TotalProfit = 0
LastProfit = 0
AverageChange = 0
FirstPass = True

# Open the CSV File

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
 #   print(csvreader)
    
 # Pull in header from the file
    csv_header = next(csvreader)
  
# Read Through Each Record
    for row in csvreader:
 #       print("Date--> " + row[0] + " Profit/Loss--> " + row[1]) 
        
 # Keep Track of Totals
        TotalProfit = TotalProfit + int(row[1])
        Monthcnt = Monthcnt + 1
        
 # Get Data from the First Record of Real Data       
        if FirstPass :
            FirstPass = False
            LastProfit = int(row[1])

# Sum amd Check Data once we get past the first real data record
     
        else:
            ProfitChange = int(row[1]) - LastProfit
            LastProfit = int(row[1])
            TotalChange = TotalChange + ProfitChange
            Averagecnt = Averagecnt + 1
 
        
            if ProfitChange > GreatestIncrease:
                GreatestIncrease = ProfitChange
                DateGreatestIncrease = str(row[0])
            
            if ProfitChange < GreatestDecrease:
                GreatestDecrease = ProfitChange
                DateGreatestDecrease = str(row[0])
        
 
AverageChange = TotalChange / Averagecnt


# print("End of Data")
print(" ")
print("Financial Analysis")
print("------------------------------")
print("Total Months: " + str(Monthcnt))
print("Total: $" + str(TotalProfit))
print("Average  Change: $" + str(round(AverageChange,2)))
print("Greatest Increase in Profits: " + str(DateGreatestIncrease) + " ($" + str(GreatestIncrease) + ")")
print("Greatest Decrease in Profits: " + str(DateGreatestDecrease) + " ($" + str(GreatestDecrease) + ")")

