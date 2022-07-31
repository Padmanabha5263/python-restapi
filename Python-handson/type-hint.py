from typing import List

# def list_avg(sequence):
#     return sum(sequence)/len(sequence)   #this will give error

# list_avg(123) 


# so to solve this we have type hinting

def list_avg(sequence: List) -> float:
    return sum(sequence)/len(sequence)   #this will give error

list_avg(123) 