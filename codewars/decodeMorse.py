MORSE_CODE = {
    ".-":   "A",
    "-...": "B",
    "-.-.": "C",
    "-..":  "D",
    ".":    "E",
    "..-.": "F",
    "--.":  "G",
    "....": "H",
    "..":   "I",
    ".---": "J",
    "-.-":  "K",
    ".-..": "L",
    "--":   "M",
    "-.":   "N",
    "---":  "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.":  "R",
    "...":  "S",
    "-":    "T",
    "..-":  "U",
    "...-": "V",
    ".--":  "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    ".----":    1,
    "..---":    2,
    "...--":    3,
    "....-":    4,
    ".....":    5,
    "-....":    6,
    "--...":    7,
    "---..":    8,
    "----.":    9,
    "-----":    0
}

def decodeMorse(morse_code):
    code = morse_code.split(" ")
    decode=''
    
    for x in code:
        if x == '':
            decode += " "
        else:
            decode += MORSE_CODE[x]

    return decode.replace("  "," ").strip()

morse_code = '.... . -.--   .--- ..- -.. .'
print(decodeMorse(morse_code))