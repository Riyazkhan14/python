'''
Lambda Functions
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.


Syntax
lambda arguments : expression
'''

x = lambda a: a+10
print(x(5))

y = lambda a,b : a*b
print(y(5,6))

z = lambda a,b,c : a+b+c
print(z(5,6,2))

'''
Why Use Lambda Functions?
The power of lambda is better shown when you use them as an anonymous function inside another function.

Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
'''

def myfunc1(n):
    return lambda a:a*n

mydoubler = myfunc1(2)
mytripler = myfunc1(3)

print(mydoubler(11))
print(mytripler(11))

'''
Lambda with Built-in Functions
Lambda functions are commonly used with built-in functions like map(), filter(), and sorted().

Using Lambda with map()
The map() function applies a function to every item in an iterable:
'''

numbers = [1,2,3,4,5,6,7,8]
doubeled1 = list(map(lambda x: x*2, numbers))
odd_numbers = list(filter(lambda x: x% 2 !=0, numbers))
print(doubeled1)
print(odd_numbers)


# Using Lambda with sorted()
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

# Sort strings by length
words = [ "Apple", "Pie", "Banana", "Cherry" ]
sorted_words = sorted(words, key = lambda x : len(x))
print(sorted_words)





























