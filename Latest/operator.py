print(10+5)

sum1 = 100+50
sum2 = sum1 + 250
sum3 = sum2 + sum2

print(sum1, sum2, sum3)

x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

print(x:=3)


numbers = [1,2,3,4,5]
count = len(numbers)
if count > 3:
    print(f"List has {count} elements")

if (counts := len(numbers)) > 3:
    print(f"List has {counts} elements")
