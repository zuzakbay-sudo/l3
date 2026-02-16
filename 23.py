def str_to_number(s):
    mapping = {
        "ZER": "0", "ONE": "1", "TWO": "2", "THR": "3", "FOU": "4",
        "FIV": "5", "SIX": "6", "SEV": "7", "EIG": "8", "NIN": "9"
    }
    
    number = ""
    for i in range(0, len(s), 3):
        number += mapping[s[i:i+3]]
    
    return int(number)


def number_to_str(num):
    mapping = {
        "0": "ZER", "1": "ONE", "2": "TWO", "3": "THR", "4": "FOU",
        "5": "FIV", "6": "SIX", "7": "SEV", "8": "EIG", "9": "NIN"
    }
    
    result = ""
    for digit in str(num):
        result += mapping[digit]
    
    return result


# Read input
expression = input()

# Find operator
for op in "+-*":
    if op in expression:
        left, right = expression.split(op)
        operator = op
        break

# Convert strings to numbers
num1 = str_to_number(left)
num2 = str_to_number(right)

# Calculate
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
else:
    result = num1 * num2

# Output result
print(number_to_str(result))
