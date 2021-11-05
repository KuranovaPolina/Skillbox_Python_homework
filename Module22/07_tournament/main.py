import os

result = {}

path = os.path.abspath("first_tour.txt")
file = open(path, 'r')
K = int(file.readline())

for i_line in file:
    parts = i_line.split()
    if int(parts[2]) > K:
        result[parts[0][0] + ". " + parts[1]] = parts[2]

file.close()

sorted_result_keys = sorted(result, key=result.get)

path = os.path.abspath("second_tour.txt")
file = open(path, 'w')
file.write(str(len(sorted_result_keys)))
line = 1
for person in sorted_result_keys:
    file.write(f"\n{line}) {person} {result[person]}")
    line += 1

file.close()
