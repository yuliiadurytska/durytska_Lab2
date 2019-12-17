S = input("Введіть рядок: ")
k = 1
n = len(S)
i = 0
for i in range (n):
    if S[i] == ' ':
        k = k + 1
print ('Кількість слів ',k)
r = S.split( )
print (set(r))