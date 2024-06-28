num =int(input ("Enter the given number:-"))
if num > 1:
    for i in range(2,int(num/2)):
        if((num%i) == 0 ):
            print(num , " is not prime")
            break;
    else:

        if (num%2==0):
            print(num, " is prime and odd" )
        print("Invalid")
