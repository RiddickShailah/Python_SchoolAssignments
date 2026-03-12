#Function to find the maximum value in a list
def max_of_list(lst):
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num  
    return max_val

#Function to calculate the sum 
def sum_of_list(lst):
    total = 0  
    for num in lst:
        total += num
    return total

#Using range() and for loops to print specific sequences
list1 = []
for i in range(10, 21):
    list1.append(i)
print(list1)

#Printing multiples of 10 from 10 - 100
list2 = []
for i in range(10, 101, 10):
    list2.append(i)
print(list2)

#Printing numbers from 100 down to 10
list3 = []
for i in range(100, 9, -10):
    list3.append(i)
print(list3)