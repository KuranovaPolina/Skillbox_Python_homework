video_cards = []
N = int(input("Nunber of video cards: "))

max = 0

for i in range(1, N + 1):
    val = int(input(f"{i} video card: "))
    video_cards.append(val)
    if val > max:
        max = val

print("Old list:", video_cards)

tmp_list = []

for card in video_cards:
    if card != max:
        tmp_list.append(card)

video_cards = tmp_list

print("New list:", video_cards)