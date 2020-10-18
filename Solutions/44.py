def largest(array):
    return max(array)

def largest_without_max(array):
    highest = min(array)
    for element in array:
        if element > highest:
            highest = element
    return highest