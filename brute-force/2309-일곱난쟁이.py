# https://www.acmicpc.net/problem/2309

heights = []
for _ in range(9):
    heights.append(int(input()))

found = False
for i in range(9):
    if found == True:
        break
    for j in range(i+1,9):
        if 100 == (sum(heights) - (heights[i]+ heights[j])):
            lier1 = heights[i]
            lier2 = heights[j]
            found = True
            break

heights.remove(lier1)
heights.remove(lier2)

for height in sorted(heights):
    print(height)

