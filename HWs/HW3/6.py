list = ["42536258796157867", "4424414244424443", "5122-2368-7954 - 3214", "44244x4424442444", "0525362587961578", "4342-3422-1111-0000"]
import re

for id in list:
    consecutive = False
    digits = re.findall(r'\d', id)
    pair = [digits[0], 1]

    for digit in digits:
        if pair[1] == 4: 
            consecutive = True
            break
        if pair[0] == digit: pair[1] += 1
        else: pair[0] = digit; pair[1] = 1

    pattern = r'[456]\d\d\d-?\d{4}-?\d{4}-?\d{4}'
    print("VALID") if re.search(pattern, id) and not consecutive else print("INVALID") 
