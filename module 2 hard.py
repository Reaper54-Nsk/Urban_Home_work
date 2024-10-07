def find_password (n):
    numbers = ''
    for i in range(1,n):
        for j in (i+1, n+1):
            if n % (i+j) == 0:
                numbers += str(i) + str(j)
    return numbers
n = int(input('Введите число от 3 до 20: '))
print(find_password(n))
