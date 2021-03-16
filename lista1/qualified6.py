def find_smallest(numbers):
    menor = max(numbers)
    for i in numbers:
        if i <= menor:
           menor = i
    return menor

print(find_smallest([2,-5,1]))