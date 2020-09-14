#print("x"+3)
#TypeError: can only concatenate str (not "int") to str


try:
    print("a")
    print("x"+3)
    print("b") # this will not run - there was an error
except:
    #pass
    print("there was an error")
