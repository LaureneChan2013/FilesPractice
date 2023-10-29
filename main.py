with open ("code.txt")as f:
        c = f.read()

list1 = c.split('\n')
print(list1)
with open ("code.txt") as f:
     f.write("This file has been written to") 
