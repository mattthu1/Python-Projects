#Matthew Hu, Feb 1
#converting the units from mm to inches, inches to links... etc etc 

mm = 750
inch = mm*0.0394
link = inch/7.92
ft = inch/12
yds = ft/3
rods = link/25
chains = rods/4
mile = yds/1760


#printing the conversions so that we are able to see the different measurements for 750mm 

print("mm to US length units")
print('mm:',mm)
print('in:', inch)
print('links:',link)
print('ft:',ft)
print('yds:',yds)
print('rods:', rods)
print('chains:', chains)
print('mi:', mile)
