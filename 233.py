number=int(input("Enter three digits (each digit for one pig):"))
a = number//100
number=number % 100
b=number // 10
c=number%10
print(a+b+c)
print((a+b+c)//3)
print((a+b+c)%3)
print(((a+b+c)%3)==0)