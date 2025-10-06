def is_factor(i, j):
    if j % i == 0:
        return True
    else:
        return False

i = int(input('Enter the first number: '))
j = int(input('Enter the second number: '))

print(is_factor(i, j))
