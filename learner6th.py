s = int(input("enter the time in seconds"))
h=s//60
m= s*60
time_left = s-h*60+s-m//60
print("seconds to hours is",h)
print("seconds to minutes is ", m)
print("time_left in seconds", time_left)
