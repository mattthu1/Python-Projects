#Matthew Hu, Feb 1
#collecting the input from the user with three nonspecific sports

sport1= (input("Please Enter Sport #1 "))
sport2= (input("Please Enter Sport #2 "))
sport3= (input("Please Enter Sport #3 "))
print()
print("Here are your sports in every possible order:",'\n')

#printing, adjusting the syntax and adding punctuation to match the formatting of the requirements given

print("1.", sport1,', ', sport2,', ', sport3,'\n',sep='' )


print("2.",'***',sport1,'*** ','***', sport3, '*** ','***', sport2,'*** ','\n',sep='')


print("3.", sport2,':', sport1, ':',sport3, '\n',sep='')


print("4.", sport2,'\n', sport3, '\n', sport1 , '\n')

print("5.", sport3,"?",'\n',sport2,"!","\n", sport1,"?!","\n",sep='')

print("6.", "--",sport3,'\n', " -----",sport1,"\n" " -----", sport2,sep='')




