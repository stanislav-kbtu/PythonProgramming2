count = 0

def recursion(n, seq):
    if len(seq) == n: 
        global count
        count += 1
        return seq
    else:
        for i in range(seq[len(seq) - 1] + 2, (seq[len(seq) - 1] + 1) ** 2): 
            recursion(n, seq + [i])


n = int(input())
recursion(n, [2])
print(count)