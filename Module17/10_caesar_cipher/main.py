alfa = ['а','б','в','г','д','е','ж','з','и','й',
        'к','л','м','н','о','п','р','с','т','у',
        'ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']

message = list(input("Введите сообщение: "))
K = int(input("Введите сдвиг: "))

new_message = [ alfa[(alfa.index(i) + K) % len(alfa)] if i != " " else " " for i in message]

print("Зашифрованное сообщение: ", ''.join(new_message))