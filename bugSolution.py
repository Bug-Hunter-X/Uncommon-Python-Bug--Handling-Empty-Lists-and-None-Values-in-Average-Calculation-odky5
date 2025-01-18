def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    numbers = [num for num in numbers if num is not None]
    if not numbers:
        return 0 #Handle list with only None values
    return sum(numbers) / len(numbers)

# Example usage with an empty list
average = calculate_average([])
print(f"The average is: {average}")

#Example with a list containing None values
number_list = [1,2,3,None,5]
average = calculate_average(number_list)
print(f"The average is: {average}") 