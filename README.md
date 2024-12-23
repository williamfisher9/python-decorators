# Python Decorators
- `Python decorators` allow you to wrap a function with another function to extend or modify its behavior without altering the original function’s code.
- `Practical use cases` for decorators include logging, enforcing access control, caching results, and measuring execution time.
- `Custom decorators` are written by defining a function that takes another function as an argument, defines a nested wrapper function, and returns the wrapper.
- `Multiple decorators` can be applied to a single function by stacking them, one per line, before the function definition. 
- `The order of decorators` impacts the final output, as each decorator wraps the next, influencing the behavior of the decorated function.

## First-Class Object
This means that functions can be passed around and used as arguments, just like any other object like str, int, float, list, and so on.

A function name without parentheses is a reference to a function
```
def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we're the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")

val = greet_bob(be_awesome)
print(val)
```

## Inner Functions
```
def parent():
    print("Printing from parent()")

    def first_child():
        print("Printing from first_child()")

    def second_child():
        print("Printing from second_child()")

    second_child()
    first_child()

parent()
```

## Functions as Return Value
Note that you’re returning first_child without the parentheses. Recall that this means that you’re returning a reference to the function first_child.
```
def parent(num):
    def first_child():
        return "Hi, I'm Elias"

    def second_child():
        return "Call me Ester"

    if num == 1:
        return first_child
    else:
        return second_child
        
>>> first = parent(1)
>>> second = parent(2)

>>> first
<function parent.<locals>.first_child at 0x7f599f1e2e18>

>>> second
<function parent.<locals>.second_child at 0x7f599dad5268>

>>> first()
'Hi, I'm Elias'

>>> second()
'Call me Ester'
```

## Example
```
def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = decorator(say_whee)

say_whee()

Something is happening before the function is called.
Whee!
Something is happening after the function is called.
```

```
from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        print(datetime.now().hour)
        if 7 <= datetime.now().hour < 24:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper

def say_whee():
    print("Whee!")

say_whee1 = not_during_the_night(say_whee)

say_whee1()

23
Whee!
```

## Using Decorators
Python allows you to call the decorated function without typing the name of the function 3 times.
```
def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@decorator
def say_whee():
    print("Whee!")

say_whee()

Something is happening before the function is called.
Whee!
Something is happening after the function is called.
```

So, @decorator is just a shorter way of saying say_whee = decorator(say_whee). It’s how you apply a decorator to a function.

You can name the wrapper function as wrapper() to make it more generic.
```decorators.py
def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice
```

```
>>> from decorators import do_twice

>>> @do_twice
... def say_whee():
...     print("Whee!")

>>> say_whee()
```

## Decorating Functions With Arguments
```decorators.py
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice
```

```
>>> from decorators import do_twice

>>> @do_twice
... def say_whee():
...     print("Whee!")
...

>>> say_whee()
Whee!
Whee!

>>> @do_twice
... def greet(name):
...     print(f"Hello {name}")
...

>>> greet("World")
Hello World
Hello World
```

## Returning Values From Decorated Functions
```
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice
```

```
>>> from decorators import do_twice

>>> @do_twice
... def return_greeting(name):
...     print("Creating greeting")
...     return f"Hi {name}"
...

>>> return_greeting("Adam")
Creating greeting
Creating greeting
'Hi Adam'
```

