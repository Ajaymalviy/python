def greed_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@greed_decorator
def say_hello():
    print("Hello!")

say_hello()


# def log_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__} with {args} and {kwargs}")
#         result = func(*args, **kwargs)
#         print(f"{func.__name__} returned {result}")
#         return result
#     return wrapper



#another decorator 


# def decor(func):
#     def inner(name):
#         print("this is the first decor be call")
#         func(name)
#         return inner

# def decor1(func):
#     def inner(name):
#         print("this is the second decor be call")
#         func(name)
#         return inner

# @decor1
# @decor
# def hello(name):
#     print("hello ji ",name)

# hello("ajay")
#arguments parser, environment variable inside a function, command line args , main program vs library import ,
# arguments parser, environment variable inside a function, command line args , main program vs library import ,positional variable args , keyword  variable args, 



#lambda function in python
#lambda arguments: expression
lambda x, y: x + y
# Define a lambda function to calculate the area of a triangle
area_triangle = lambda base, height: 0.5 * base * height

# Example usage
base = 5
height = 8
area = area_triangle(base, height)

print(f"The area of the triangle with base {base} and height {height} is: {area}")

