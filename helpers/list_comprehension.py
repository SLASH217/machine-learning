numbers = [1,2,3,4,5]



squared = [i ** 2 for i in numbers] # mapping behaviour

# filtering behaviour
filtered = [i > 3 for i in numbers] # returns boolean list
print(filtered)
filtered = [i for i in numbers if i > 3] # returns list with condition applied

print(filtered)
print(squared)