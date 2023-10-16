print('1 is technically not a prime number.')
for number in range(2, 1001):
    prime = True
    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            prime = False
            break
    if prime:
        print(f'{number} is a prime number!')
   
