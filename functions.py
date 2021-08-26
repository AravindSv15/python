def calculate_exp(exp):
    total = 0
    for item in exp:
        total = total + item
    return total


tom_exp = [232, 323, 454, 4646]
joe_exp = [2424, 424, 232]
tom_total = calculate_exp(tom_exp)
joe_total = calculate_exp(joe_exp)

print("tom total exp:", tom_total)
print("joe total exp:", joe_total)


# sum function
def sum(a, b):
    
    total1 = a + b
    return total1


n = sum(5, 6)
print(n)
