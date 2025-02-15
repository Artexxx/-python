"""
Шифр Полибия -- шифр замены, часто представляется в виде квадрата,
с прочертанными по горизонтали и вертикали числами от 1 до 6.

      Message: rip and tear until
          Key: None
Final message: 36.23.34.11.32.14.42.15.11.36.43.32.42.23.26
"""
from re import findall

keysPolibiy = {
    'A': '11', 'B': '12', 'C': '13', 'D': '14',
    'E': '15', 'F': '16', 'G': '21', 'H': '22',
    'I': '23', 'J': '24', 'K': '25', 'L': '26',
    'M': '31', 'N': '32', 'O': '33', 'P': '34',
    'Q': '35', 'R': '36', 'S': '41', 'T': '42',
    'U': '43', 'V': '44', 'W': '45', 'X': '46',
    'Y': '51', 'Z': '52', '0': '53', '1': '54',
    '2': '55', '3': '56', '4': '61', '5': '62',
    '6': '63', '7': '64', '8': '65', '9': '66'
}


def regular(text):
    template = r"[0-9]{2}"
    return findall(template, text)


def encryptDecrypt(mode, message, final=[]):
    if mode == 'E':
        for symbol in message:
            if symbol in keysPolibiy:
                final.append(keysPolibiy[symbol])
    else:
        for twoNumbers in regular(message):
            for key in keysPolibiy:
                if twoNumbers == keysPolibiy[key]:
                    final.append(key)
    return ".".join(final)


if __name__ == '__main__':
    cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
    if cryptMode not in ['E', 'D']:
        print("Error: mode is not Found!")
        raise SystemExit
    startMessage = input("Write the message: ").upper()
    startKey = input("Write the message: ").upper()
    print("Final message:", encryptDecrypt(cryptMode, startMessage))
