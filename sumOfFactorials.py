print('Введите n:')
n = int(input())
def fact(n):
    if n == 1:
        return 1
    else:
        return(n*fact(n-1))

def sumFact(a):
    if a == 0:
        return 0
    else:
        return sumFact(a-1) + fact(a)
        
print(f'Сумма факториалов от 1 до n: {sumFact(n)}')
#Строка изменения файла для второго коммита
#Строка изменения файла для третьего коммита
