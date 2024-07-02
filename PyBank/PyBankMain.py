#!/usr/bin/env python
# coding: utf-8

# In[1]:


#PyBank Instructions

#Your task is to create a Python script that analyzes the records to calculate each of the following values:
#The total number of months included in the dataset
#The net total amount of “Profit/Losses” over the entire period
#The changes in “Profit/Losses” over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period

import os
import csv

budget_data = os.path.join ('.' , 'Resources' , 'budget_data.csv')

# Lists to store data
dates = []
profit_loss = []
change = []
    
#open and read csv 
with open (budget_data, encoding='utf') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    #print(csv_reader)

# Read the header row first 
    csv_header = next(csv_reader)
    #print(csv_header)

    print("Financial Analysis")
    print("_____________________________")

# Read each row of data after the header
    for row in csv_reader:
        #print(row)
        
        #Add dates
        dates.append(row[0])
        
        #Add Profit/Losses
        profit_loss.append(int(row[1]))

#The total number of months included in the dataset
    total_months = len(dates)       
    print("Total Months: " + str(total_months))
    
#The net total amount of “Profit/Losses” over the entire period
    net_total = str(sum(profit_loss))
    print("Total: " + "$"+ (net_total))

#The changes in “Profit/Losses” over the entire period, and then the average of those changes
    #add change
    for x in range(1, len(profit_loss)):
        change.append((int(profit_loss[x]) - int(profit_loss[x-1])))
        #print(change)
    average = sum(change) / len(change)
    print("Average Change: " + "$"+str(average))

#The greatest increase in profits (date and amount) over the entire period
    greatest_increase = max(change)
    #print(str(greatest_increase))
    print("Greatest Increase in Profits: " + str(dates[change.index(max(change))+1]) + " " + "(" +"$"+str(greatest_increase)+")")   
    
#The greatest decrease in profits (date and amount) over the entire period
    greatest_decrease = min(change)
    #print(str(greatest_decrease))
    print("Greatest Decrease in Profits: " + str(dates[change.index(min(change))+1]) + " " + "(" +"$"+str(greatest_decrease)+")")        

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

output_path = os.path.join('.', 'Analysis', 'FinancialAnalysis.txt')   
#print(output_path)
with open(output_path, "w") as txtfile:
    txtfile.write("Financial Analysis" + "\n")
    
    txtfile.write("___________________"+ "\n")

    txtfile.write("Total Months: " + str(total_months) + "\n")
    
    txtfile.write("Total: " + "$"+ (net_total) + "\n")
    
    txtfile.write("Average Change: " + "$"+str(average) + "\n")
    
    txtfile.write("Greatest Increase in Profits: " + str(dates[change.index(max(change))+1]) + " " + "(" +"$"+str(greatest_increase)+")" 
                  + "\n")
    
    txtfile.write("Greatest Decrease in Profits: " + str(dates[change.index(min(change))+1]) + " " + "(" +"$"+str(greatest_decrease)+")" + "\n")


# In[ ]:




