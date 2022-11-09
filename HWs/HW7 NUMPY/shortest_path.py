def shortest(map, current_pos, target, counter):
    #print(current_pos)
    target_pos = getPos(map, target)
    if current_pos == getPos(map, target): 
        return shortest(map, current_pos, str(int(target) + 1), counter)
    if target_pos == None: 
        return counter
    if current_pos[0] != target_pos[0]:
        dif = target_pos[0] - current_pos[0]
        dx = 1 if dif > 0 else -1
        return shortest(map, (current_pos[0] + dx, current_pos[1]), str(target), counter + 1)
    if current_pos[1] != target_pos[1]:
        dif = target_pos[1] - current_pos[1]
        dy = 1 if dif > 0 else -1
        return shortest(map, (current_pos[0], current_pos[1] + dy), str(target), counter + 1)


def shortest_path(l):
    return shortest(l, getPos(l, '1'), '2', 0)

def getPos(map, target):
    r, c = None, None
    for row in map:
        if target in row:
            r = map.index(row)
            for chr in row:
                if chr == target:
                    c = row.index(target)
                    return (r, c)
    return None


#print(int('1'))
print(shortest_path([
  ("00000"),
  ("01006"),
  ("02000"),
  ("30050"),
  ("00004")
]))

print(shortest_path([
  ("00020000"),
  ("01000000")
])) 
print(shortest_path([
  ("001"),
  ("002"),
  ("003")
])) 

