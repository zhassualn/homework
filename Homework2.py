CODE = {' ': '_',	"'": '.----.',	'(': '-.--.-',	')': '-.--.-',	',': '--..--',	'-': '-....-',	'.': '.-.-.-',	'/': '-..-.',
 '0': '-----',	'1': '.----',	'2': '..---',	'3': '...--',	'4': '....-',	'5': '.....',	'6': '-....',	'7': '--...',
 '8': '---..',	'9': '----.',	':': '---...',	';': '-.-.-.',	'?': '..--..',	'A': '.-',	'B': '-...',	'C': '-.-.',
 'D': '-..',	'E': '.',	'F': '..-.',	'G': '--.',	'H': '....',	'I': '..',	'J': '.---',	'K': '-.-',	'L': '.-..',
 'M': '--',	'N': '-.',	'O': '---',	'P': '.--.',	'Q': '--.-',	'R': '.-.',	'S': '...',	'T': '-',	'U': '..-',
 'V': '...-',	'W': '.--',	'X': '-..-',	'Y': '-.--',	'Z': '--..',	'_': '..--.-', '':' '}


inverseMorseAlphabet = {x: k for k, x in CODE.items()}

def converttomorsecode(sentence):
    sentence = sentence.upper()
    englishcodedSentence = ""
    for character in sentence:
        englishcodedSentence += CODE[character] + " "
    return englishcodedSentence


def converttoenglish(sentence1):
    b = sentence1.split(' ')
    MorsecodedSentence1 = ""
    for character in range(len(b)):
        MorsecodedSentence1 += inverseMorseAlphabet[b[character]]
    return MorsecodedSentence1

choice=input("Text or morse: ")


if choice == "text":
    given_sentence = input("enter text code: ")
    print(converttomorsecode(given_sentence))


elif choice == "morse":
    given_sentence = input("enter morse code: ")
    print(converttoenglish(given_sentence))
