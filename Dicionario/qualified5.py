def positive_sum(arr):
    soma = 0
    for i in arr:
        if i > 0:
            soma = i + soma
        elif i == "":
            return 0
        else:
            continue 
    return soma

print(positive_sum([5,4,7,8,1,-9]))



def reverse_string(str):
    return str[::-1]