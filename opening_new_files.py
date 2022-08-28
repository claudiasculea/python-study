#nameHandle = open("names", "w")   
#for i in range(2): 
    #name = input("Enter name: ")
    #nameHandle.write(name + '\n')
#nameHandle.close() 

#with open("names", "w") as nameHandle:
    #for i in range(2): 
        #name = input("Enter name: ")
        #nameHandle.write(name + '\n')

with open("names", "r") as nameHandle:
    for line in nameHandle:
        print(line)