#print("x"+3)
#TypeError: can only concatenate str (not "int") to str

import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)


try:
    print("a")
    print(3+"x")
    print("b") # this will not run - there was an error
except:
    #pass
    print("there was an error")
