def recursion(iteration, vert = "A"):
    if name in tree[vert]: return iteration
    else:
        for city in tree[vert]: return recursion(iteration + 1, city)




tree = {"A" : "B", "B" : ["C", "D"], "C" : ['E', 'F', 'G']}
name = input("Name of the city: ")
vert = "A"
print(recursion(1, vert)) 