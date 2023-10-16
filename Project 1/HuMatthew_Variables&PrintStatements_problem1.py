#Matthew Hu, Feb 1
#collecting the data from the test scores and storing them in variables 

score1 = 92
score2 = 90
score3 = 88
first_name = "Grace"
last_name = "Hopper"
class_curve = 1.5

# applying the variables so we are able to find users name, find the average of the scores, and apply the curve to the average score

print("Fall semester grades for:", first_name, last_name, '\n')
print("Test Scores:", score1,",",  score2,"and", score3,'\n')
print("Average Score:", (score1+score2+score3)/3,'\n')
print('Average Score + Class Curve:', (score1+score2+score3)/3 + class_curve)


