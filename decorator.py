def decorate(func):
    def wrapper(*args, **kwargs):
        f_name = func.__name__
        value = func(*args, **kwargs)
        with open('logs.txt', 'a+') as file:
            file.write(f'{f_name} return value of: {value}\n')
            file.close()
        return func(*args, **kwargs)
    return wrapper

@decorate
def add_(c , y):
    return c + y

print(add_(10, 20))
print(add_(10, 20))
print(add_(10, 20))
print(add_(10, 20))
print(add_(10, 20))
print(add_(10, 20))
print(add_(10, 20))
print(add_(10, 20))

    