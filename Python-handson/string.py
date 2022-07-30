# embedded the variable value with in string using formater f
# name = input("Enter name\n")
name= " Padmanabha"
greeting = f"hello {name}"
print (greeting)


# using format function
name= "Ganesh"
str = "hello {}"
print(str.format(name))
print(str.format("bob"))

# multiple 
str = "hello, {} Today is {}"
embedstr = str.format("Padmanabha", "Saturday")
print(embedstr)