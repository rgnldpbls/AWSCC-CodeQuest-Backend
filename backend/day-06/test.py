ip = int(input("Limit: "))

for i in range(ip):
    i += 1
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz!')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)