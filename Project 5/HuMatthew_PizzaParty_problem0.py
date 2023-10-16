budget = float(input('Enter budget for your party:  '))
costperslice = float(input('Cost per slice of pizza:  '))
costperwholepizza = float(input('Cost per whole pizza pie (8 slices): '))
people = int(input('How many people will be attending your party? '))

slices = 0 
pizzaslices = 8
pie = 0 
slicestotal = 0



for i in range(1, people+1):
    sliceperperson = 0
    
    
    while sliceperperson <= 0:

        sliceperperson = float(input(f'Enter number of slices for person #{i}: '))
        slices += sliceperperson
        
        if sliceperperson <= 0:

            print('Not a valid entry, try again!')
            slices -=  sliceperperson



    
if slices >= pizzaslices:
    pies = slices // 8
    slicestotal = slices % 8

    totalcost = (slicestotal * costperslice)  + (pies * costperwholepizza)
    leftover = budget - totalcost
   
    
    overbudget = totalcost - budget 
    pies = slices // 8

    
    if leftover == 0:

        print(f'Your total cost will be: {totalcost}')
        print('You will have no money left after your order.')

    elif totalcost > budget:
        print('Your order cannot be completed.')
        print(f'You should purchase {pies} pies and {slicestotal} slices')
        print(f'This would put you over budget by {overbudget}')


    elif totalcost < budget:
        
        print(f'You should purchase {pies} pies and {slicestotal} slices') 
        print(f'Your total cost will be: {totalcost}')
        print(f'You will still have {leftover} left after your order') 




else:
    
    pies = slices // 8
    slicestotal = slices % 8
    
    totalcost = (slicestotal * costperslice)  + (pies * costperwholepizza)
    leftover = budget - totalcost
   
    
    print(f'You should purchase {0} pies and {slices} slices')


    if leftover == 0:

        print(f'Your total cost will be: {totalcost}')
        print('You will have no money left after your order.')

    else:
        print(f'Your total cost will be: {totalcost}')
        print(f'You will still have {leftover} left after your order')





