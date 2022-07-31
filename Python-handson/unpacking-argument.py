

def mul(*args):
    print(args)    #it prints arguments as a tuple eg:  (1,2,3)
    total=1
    for i in args:
        total = total * i
    print(total)

mul(1, 2, 3)




# kwargs argument
# it will take a argument and print as dictionary
def named(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(f"key= {key} and value= {value}")


named(name="padmanabha", age=23)