#Assign values to variables
spend = 2000
budget = 100000
rate = 0.05
day = 0

#Open a file and indicate it for w for writing, a for appending
out = open('report.txt', 'w')

#Print out the headers for data
print ('{:>5s} {:^25s} {:^12s}'. format('Day', 'Spend', 'Remaining'), file = out)

#Create while loop to calculate budget and spend changes over time
while budget > 0:
	day = day + 1
	add_spend = spend * rate
	if day >= 2:
		spend = spend + add_spend
	budget = budget - spend
	if budget < 0:
		spend = spend + budget
		budget = 0
	print ('{:>5s} {:<5d} {:>5s}{:<10.2f} {:>5s}{:<10.2f}'.format('Day', day, '$', spend, '$', budget), file = out)

#Closing the file
out.close()
