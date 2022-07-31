from requests import TooManyRedirects


try:
    res = 123/0
except ZeroDivisionError as e:
    print("divisor should not be zero")
    print(e)

finally:
    print("operation completed")



# to rise custom exception

class TooManyPagesReadEror(ValueError):
    pass 

raise TooManyPagesReadEror(
    f"you tried to read too many pages at a time"
)


