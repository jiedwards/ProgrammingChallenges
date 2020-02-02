
def largestOneDigit(A):
    valid_numbers = []
    for numbers in A:
        if numbers in range(1,10):
            valid_numbers.append(numbers)
        else:
            pass

    if valid_numbers:
    	return (max(valid_numbers))
    else:
    	return "Invalid input supplied"