
ins = open('maze.txt',"r")              #From input to nested list result = Maze
results = []
for line in ins:
    results.append(list(line.rstrip()))
print(results)

for i in range (len(results)):
    for j in range (len(results[i])):
        if (results[i][j] == 'S'):      #Finding The Start
            Sx = i
            Sy = j
        if (results[i][j] == 'G'):      #Finding The Goal
            Gx = i
            Gy = j

