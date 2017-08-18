"""LIAM"""
name = input (" please enter name:")
while len(name)<1:
    print("error blank space")
    name = input("please enter name")
print (name [1::2])