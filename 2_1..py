import random
n = int(input("Введіть n: "))
lst1 = []
i = 0

while i < n:
    lst1.append(random.uniform(0, 10)) 
    i += 1
print (lst1)

lst2 = lst1.copy()
lst1.sort()
print (lst1)

i = 1
for i in range(n):
    if lst2[i] > lst1[i]:
        print('Збільшили свій номер ',lst2[i])
        