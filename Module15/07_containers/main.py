containers = []
N = int(input("Number of containers: "))

for _ in range(N):
    containers.append(int(input("Container's weight: ")))

new_weight = int(input("\nNew container's weight: "))

for i in range(N):
    if containers[i] < new_weight:
        print("\nPlace:", i + 1)
        break
