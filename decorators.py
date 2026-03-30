def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper

@announce
def hello():
    print("Hello, World!")

hello()


'''
def announce(f):
    def wrapper(*args, **kwargs):
        print("Iniciando...")
        result = f(*args, **kwargs)
        print("Terminado.")
        return result
    return wrapper
'''