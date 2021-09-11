def sort(numbers, N):
    for j in range(N):
        F = 0
        for i in range(N - j):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                F += 1

        if F == 0:
            break

numbers = [1, 4, -3, 0, -2]

print("Start list:", numbers)

sort(numbers, len(numbers) - 1)

print("Sorted list:", numbers)

#Знаю, сортировка не выглядит как просто выдуманная человеком. Потому что это обычная Bubble сортировка из Википедии.
# Но я правда в них разбираюсь) Я просто не хочу снова писать сортировку с нуля)
