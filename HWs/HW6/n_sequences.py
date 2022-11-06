import itertools
n = int(input())

def find_subset(sequence):
    highest = 1
    count = 1
    current = sequence[0]
    for i in range(1, len(sequence)):
        if sequence[i] == current: count += 1
        else:
            current = sequence[i]
            if count > highest: highest = count
            count = 1
    if count > highest: highest = count
    return highest


def generate_n_sequences(n):
    sequences = itertools.product(range(1, n + 1), repeat = n)
    sum = 0
    for sequence in sequences:
        sum += find_subset(sequence)
    return sum

print(generate_n_sequences(n) % 1000000009)
#print(find_subset([2, 2, 2, 2]))