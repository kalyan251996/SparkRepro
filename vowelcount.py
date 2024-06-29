element=str(input("Enter the input string:-"))
vowels="aeiouAEIOU"
count=0
for i in element:
    if i in vowels:
        count+=1
print("Total Count:-",count)