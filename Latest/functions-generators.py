'''
Generators
Generators are functions that can pause and resume their execution.

When a generator function is called, it returns a generator object, which is an iterator.
The code inside the function is not executed yet, it is only compiled. The function only executes when you iterate over the generator.

Generators allow you to iterate over data without storing the entire dataset in memory.
Instead of using return, generators use the yield keyword.
'''

def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)

'''
The yield Keyword
The yield keyword is what makes a function a generator.

When yield is encountered, the function's state is saved, and the value is returned. The next time the generator is called, it continues from where it left off.
'''
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
for num in count_up_to(5):
    print(num)

'''
Generators Saves Memory
Generators are memory-efficient because they generate values on-the-fly instead of storing everything in memory.

For large datasets, generators save memory:
'''
def large_sequence(n):
    for i in range(n):
        yield i

gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))

'''
Using next() with Generators
You can manually iterate through a generator using the next() function:
'''

def simple_gen():
    yield "Emil"
    yield "Tobias"
    yield "Linus"

gen1 = simple_gen()
print(next(gen1))
print(next(gen1))
print(next(gen1))

'''
Generator Expressions
Similar to list comprehensions, you can create generators using generator expressions with parentheses instead of square brackets:
'''

# list Comprehension - creates a list
list_comp = [x * x for x in range(5)]
print(list_comp)

# Generator expression - creates a generator
gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))

# Use SUM
total = sum(x * x for x in range(10))
print(total)

'''
Fibonacci Sequence Generator
Generators can be used to create the Fibonacci sequence.

It can continue generating values indefinitely, without running out of memory:
'''

def fibinaaci():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b

# get first 100 Numbers
gen3 = fibinaaci()
for _ in range(100):
    print(next(gen3))


'''
Generator Methods
Generators have special methods for advanced control:

send() Method
The send() method allows you to send a value to the generator:
'''
def echo_generator():
    while True:
        received = yield
        print("Received:", received)
gen4 = echo_generator()
next(gen4) # Prime the generator
gen4.send("Hello")
gen4.send("World")


# close() Method

def my_gen():
    try:
        yield 1
        yield 2
        yield 3
    finally:
        print("Generator Closed")

gen5 = my_gen()
print(next(gen5))
gen5.close()















































