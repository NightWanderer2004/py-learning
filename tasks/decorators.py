# Example of logging function call

def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Calling function" + ': ' + func.__name__)
        result = func(*args, **kwargs)
        return result
    return wrapper


@log_function_call
def add(a, b):
    return a + b


add(3, 5)


# Authentication example

def authenticate(func):
    def wrapper(*args, **kwargs):
        if user_authenticated():  # some func
            return func(*args, **kwargs)
        else:
            raise Exception("Authentication failed")
    return wrapper


@authenticate
def access_sensitive_data():
    return "You have access to sensitive data"
