# structure
def recursive_function(parameters):
    if base_case_condition(parameters):
        return base_case_value
    recursive_function(modified_parameters)


# example
def recursive_factorial(n):
    print('factorial called with '+str(n))
    if n<2:
        print('Returning 1')
        return 1
    result = n * recursive_factorial(n-1)
    print("Returning " + str(result) + " for factorial of "+str(n))
    return result

recursive_factorial(4)

