print("welcome to pattern generator and pattern analyzer")

print("select an option:")
print("1. Generate pattern (triangle)")
print("2. Analyze pattern")
print("3. Exit")


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
    elif choice ==2:
        start=int(input("enter the starting range: "))
        end=int(input("enter the ending range: "))
        while True:
            
            if end<start:
                print("warning: the ending range should be greater than the starting range.")
                start=int(input("enter the starting range: "))
                end=int(input("enter the ending range: "))
            else:
                for i in range(start,end+1):
                    if i % 2 == 0:
                        print(i, "is even")
                    else:
                        print(i, "is odd")
                sum=0
                for i in range(start,end+1):
                    sum += i
                print(f"sum of numbers from {start} to {end} is: {sum}")
                break
    elif choice==3:
        print("exiting...")
        print("thank you for using the pattern generator and analyzer.")
        break
    else:
        print("invalid choice. please try again.")

