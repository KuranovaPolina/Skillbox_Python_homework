violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

N = int(input("Number of sounds: "))
time = 0

for i in range(N):
    name = input(f"{i + 1} sound: ")
    time += violator_songs[name]

print(f"\nAll time: {round(time, 2)} minutes")

# зачтено
