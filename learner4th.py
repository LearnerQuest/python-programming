age = int(input("enter your age"))
re = age>=18
out = "canvote"*re+ "cannotvote"*(1-re)
print(out)

