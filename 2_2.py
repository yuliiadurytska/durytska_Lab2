m,n = input('Введіть кількіть рядків та стовбців через пробіл: ').split(' ')
u = list(input('Введіть двомірний масив: ').split(' '))
m,n = int(m),int(n)

p =[]

for i in range(int(m)):
    k = []
    for j in range(int(n)):
        k.append(int(u[int(n)*i+j]))
    p.append(k)
k = True

for i in range(m):
    for j in range(n//2):
        if p[i][j] != p[i][n-1-j]:
                k = False
                break
if k == True:
    print('Має вертикальну вісь симетрії')
else:
    print('Не має вертикальну вісь симетрії')