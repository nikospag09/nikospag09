x=int(input("Enter a number: "))
x=(x*3)+1
result=0
hold = x
if x>10:
 while x > 0:
    rem = x % 10
    result = result + rem
    x = int(x/10)
 print("The sum is: ",result)



