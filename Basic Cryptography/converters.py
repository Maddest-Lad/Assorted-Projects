LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ALPHANUMERICS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

# Returns All 25 Cesar Cipher Shifts
def cesar_cipher(text: str) -> [str]:
    for key in range(len(LETTERS)):
        translated = ''
        for symbol in text:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(LETTERS)
                translated = translated + LETTERS[num]
            else:
                translated = translated + symbol
        print('Hacking key #%s: %s' % (key, translated))

cesar_cipher("Test")