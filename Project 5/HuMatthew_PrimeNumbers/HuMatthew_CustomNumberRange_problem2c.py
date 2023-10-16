start = int(input('Start number:'))

while start < 0:
    print('Start must be positive')
    start = int(input('Start number:'))


end = int(input('End number:'))

while end < 0:
    print('Start and end must be positive')
    end = int(input('End number:'))

while start > end:
    print('End number must be greater than start number')
    end = int(input('End number:'))



for number in range(start, end+1):
    prime = True
    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            prime = False
            break
    if prime:
        print(number)
  
