def factorial(n):
    product=1
    for i in range(1,n+1):
        product*=i
    return product
n=int(input('Enter the number: '))
if n<0:
    print('Incorrect Number')
else:
    f=factorial(n)
    print('Factorial of', n ,'is', f)