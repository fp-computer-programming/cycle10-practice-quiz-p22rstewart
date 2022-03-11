# RTS 2/20/22

# Question 1
from operator import index

def food_costs(groceries, costs):
# Create for loop
    for items in groceries:
        for index, price in enumerate(items):
            groceries_mod = price + ": $" + str(costs[0])
            del(costs[0])
        return groceries_mod


# Test 
print(food_costs([['apple','pear','banana'],['salmon','tuna','cod'],['milk','eggs','yogurt']],[1.99,2.99,0.99,9.99,10.99,6.99,3.49,2.49,1.49]) == 
['apple: $1.99','pear: $2.99','banana: $0.99'],['salmon: $9.99','tuna: $10.99','cod:$6.99'],['milk: $3.49','eggs: $2.49','yogurt: $1.49'])

# Question 2

# Define for loop
def factorial(number):
    result = 1 
    num = 1 
    if number == 0:
        result = 0 
        #Finds factoral
    else:
        while num <= number: 
            result = num * result 
            # counter
            num += 1 
    return result

 #Test
print(factorial(5))
print(factorial(4))
print(factorial(42))

# Question 3
# define function 
def fib_nums(number):
    # Conditonals to set input values
    if number == 1:
        return [0]
    if number == 2:
        return [0,1]
    fib = [0,1]
    while number > len(fib):
        fib.append(fib[-1] + fib[-2])
    return fib

# Test
print(fib_nums(2))
print(fib_nums(4))
print(fib_nums(6))
