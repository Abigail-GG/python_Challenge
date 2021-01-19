# import os
# import csv
# import numpy as np

# csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
# with open(csvpath) as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=',')
#     print(csvreader)
import os
import csv
import pandas as pd
import numpy as np

csvpath = os.path.join('Resources/budget_data.csv')
with open(csvpath) as csvfile:
    data = pd.read_csv (csvfile, delimiter=',')
    # print(data)
    revenue_change = []
    profits = np.array(data['Profit/Losses'])
    months = np.array(data['Date'])
    i = 0
    for i in range(len(profits)-1):
        profit_loss =(profits[i+1]) - (profits[i])
        revenue_change.append(profit_loss)
        total=np.array(revenue_change)
    max_increase_month = revenue_change.index(max(total)) + 1
    max_decrease_month = revenue_change.index(min(total)) + 1

print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {len(months)}')
print(f'Total: ${profits.sum()}')
print(f'Average Change: ${total.mean()}')
print(f'Greatest Increase in Profits: {months[max_increase_month]} (${total.max()})')
print(f'Greatest Decrease in Profits: {months[max_decrease_month]} (${total.min()})')
print("----------------------------")

f=open('Results3.txt','w+')
f.write('\nFinancial Analysis')
f.write('\n----------------------------')
f.write(f'\nTotal Months: {len(months)}')
f.write(f'\nTotal: ${profits.sum()}')
f.write(f'\nAverage Change: ${total.mean()}')
f.write(f'\nGreatest Increase in Profits: {months[max_increase_month]} (${total.max()})')
f.write(f'\nGreatest Decrease in Profits: {months[max_decrease_month]} (${total.min()})')
f.write("\n----------------------------")
f.close()