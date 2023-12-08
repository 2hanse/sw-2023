while True :
    n = int(input("Enter the number : "))
    if n ==0:
        print('EXIT')
        break
    
    elif n %2 == 0:
            print("%d is even number" %n)
    else:
        print(n,"is odd number")
