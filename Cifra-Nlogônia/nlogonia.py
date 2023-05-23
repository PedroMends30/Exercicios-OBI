nearest_vowel = [   
    ("B","A"),("C","A"),("D","E"),
    ("F","E"),("G","E"),("H","I"),
    ("J","I"),("K","I"),("L","I"),
    ("M","I"),("N","O"),("P","O"),
    ("Q","O"),("R","O"),("S","O"),
    ("T","U"),("V","U"),("W","U"),
    ("X","U"),("Y","U"),("Z","U")
    ]

next_consonant = [
    ("B","C"),("C","D"),("D","F"),
    ("F","G"),("G","H"),("H","J"),
    ("J","K"),("K","L"),("L","M"),
    ("M","N"),("N","P"),("P","Q"),
    ("Q","R"),("R","S"),("S","T"),
    ("T","V"),("V","W"),("W","X"),
    ("X","Y"),("Y","Z"),("Z","Z")
    ]

texto = input("Digite o texto a ser cifrado: ")

def nearest_consonant_finder(letter):
    for i in next_consonant:
        if letter.upper() == i[0]:
            return i[1]
    return letter

def nearest_vowel_finder(letter):
    for i in nearest_vowel:
        if letter.upper() == i[0]:
            return i[1]
    return letter

def cipher(texto):
    texto_cifrado = ""
    for letra in texto:
        if letra.upper() in "AEIOU":
            texto_cifrado += letra    
        else:
            texto_cifrado += letra + nearest_vowel_finder(letra) + nearest_consonant_finder(letra)
    return texto_cifrado.upper()

print(cipher(texto).capitalize())