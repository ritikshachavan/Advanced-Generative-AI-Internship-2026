#list of daily sales
sales = [1200, 1500, 900, 2200, 1400, 3000]

#Calculate average sales
total_sales = sum(sales)
number_of_days = len(sales)

average = total_sales / number_of_days

#Calculate 30% above average limit
threshold = average + (0.30 * average)

#spike days
print("Sales Spike Days:")

for i in range(len(sales)):
    
    if sales[i] > threshold:
        print("Day", i+1, ":", sales[i])