
numbers_lst = []
second_numbers_lst = []

for x in range(10) :
    a = int(input("Insert a number here "))
    numbers_lst.append(a)

for x in range(0, 10, 2) :
    second_numbers_lst.append(numbers_lst[x])


print(second_numbers_lst)