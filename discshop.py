purchase=int(input("enter the amount:--"))
if (purchase>100):
    if(purchase>150):
        print("elgible for free shipping and discount ")
    else:
        print("elgible for free shipping")
else:
    print("not elgible either")
