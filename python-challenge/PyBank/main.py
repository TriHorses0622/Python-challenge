#PyBank Main File
dataFile = '/Users/zhongyuliu/Desktop/colnyc201907data3/Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv'
import pandas as pd
dataFrame = pd.read_csv(dataFile, header=0)
#print(dataFrame)
print('Financial Analysis')
print('---------------------------')
rowsNum=len(dataFrame.index)
print('Total Months: '+str(rowsNum))
total=dataFrame['Profit/Losses'].sum()
print('Total: $'+str(total))
changes=[]
#print(dataFrame.iat[0,1])
for i in range(rowsNum-1):
    change=dataFrame.iat[i+1,1]-dataFrame.iat[i,1]
    changes.append(change)
    i+=1
#print(changes)
averageChanges=sum(changes)/85
#print(averageChanges)
print('Average Change: $'+str(averageChanges))
#print(max(changes))
maxium=max(changes)
maxIndex=changes.index(maxium)
maxDate=dataFrame.iat[maxIndex,0]
minimum=min(changes)
minIndex=changes.index(minimum)
minDate=dataFrame.iat[minIndex,0]
print('Greatest Increase in Profits: '+str(maxDate)+' '+'($'+str(maxium)+')')
print('Greatest Decrease in Profits: '+str(minDate)+' '+'($'+str(minimum)+')')

