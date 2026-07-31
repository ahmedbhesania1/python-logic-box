while True:
    choice=int(input("enter your choice: "))
    if choice==1:
        rows=int(input("enter the number of rows for the triangle: ")) 
        while True:
            
                   
                if rows<0:
                    print("please enter a valid number of rows.")
                    rows=int(input("enter the number of rows for the triangle: "))
                else:
                    for i in range(1,rows+1):
                        for j in range(1,i+1):
                            print("*", end=" ")
                        print()
                    
                    break   