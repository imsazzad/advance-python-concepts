def root_function(dynamic_function):
    print("this is intialization of root function")

    def internal_function():
        print("before dynamic function execution")
        dynamic_function(100)
        print("after dynamic function execution")

    return internal_function


def dynamic_function(var=21):
    print( "inside dynamically added function", var)


internal_function = root_function(dynamic_function)
print("calling internal function")
internal_function()


print("#############got idea from https://www.geeksforgeeks.org/decorators-in-python/")


# defining a decorator
def hello_decorator(func):
    # inner1 is a Wrapper function in
    # which the argument is called

    # inner function can access the outer local
    # functions like in this case "func"
    def inner1():
        print("Hello, this is before function execution")

        # calling the actual function now
        # inside the wrapper function.
        func()

        print("This is after function execution")

    return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
    print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behavior
function_to_be_used = hello_decorator(function_to_be_used)

# calling the function
function_to_be_used()