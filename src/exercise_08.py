import string

letters_upper = string.ascii_uppercase
letters_lower = string.ascii_lowercase


def cifrado_cesar(message, moves):
    result = ""

    for char in message:
        if char in letters_lower:
            idx = letters_lower.find(char)
            new_idx = (idx + moves) % len(letters_lower)
            result += letters_lower[new_idx]
        elif char in letters_upper:
            idx = letters_upper.find(char)
            new_idx = (idx + moves) % len(letters_upper)
            result += letters_upper[new_idx]
        else:
            result += char

    return result


message = input("Ingrese un mensaje: ")
moves = int(input("Ingrese el desplazamiento: "))

encrypted = cifrado_cesar(message, moves)
print(f"Mensaje cifrado: {encrypted}")
print(f"Mensaje descifrado: {cifrado_cesar(encrypted, -moves)}")
