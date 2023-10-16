#Input: Two numeric values 

#Processing: describing the larger of the two values when given two numeric values. For example, it determines if a (5) is larger than b (10) and pics the larger number. 

#Output: It retunrs the larger/smaller of the two input values


def maximum(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
        
def minimum(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2

# test


a = 5
b = 10
c = 15
d = 20

ans1 = maximum(a,b)
ans2 = maximum(a,c)
ans3 = maximum(a,d)
print(ans1, ans2, ans3) # 10 15 20

ans4 = minimum(d,c)
ans5 = minimum(d,b)
ans6 = minimum(d,a)
print(ans4, ans5, ans6) # 15 10 5

ans7 = maximum(maximum(a,b), maximum(c,d))
print("The biggest is:", ans7) # 20
