def height(man):
    if man not in pedigree:
        return 0
    else:
        return 1 + height(pedigree[man])

N = int(input("N = "))
pedigree = {}

for i in range(N - 1):
    pair = input("{0} pair: ".format(i+1)).split(" ")
    pedigree[pair[0]] = pair[1]

heights = {}
for man in set(pedigree.keys()).union(set(pedigree.values())):
    heights[man] = height(man)

print("\nHeigh:")
for key in sorted(heights.keys()):
    print(key, heights[key])