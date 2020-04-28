x = int(input("Enter a number "))
odd_or_even = lambda x : x % 2 == 0 
if odd_or_even(x):
    print("Even")
else:
    print("Odd")
num = int(input("Enter a number: "))
def integer_divisor (num):
    liste = list()
    for i in range(1,num+1):
        if  num % i ==0:
            liste.append(i)
    return liste
print(integer_divisor(num))
