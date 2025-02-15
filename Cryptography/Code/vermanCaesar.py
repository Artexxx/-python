"""
Шифр Вернама -- шифр с абсолютной криптостойкостью, т.к. использует случайные ключи для каждого символа.
В данном примере шифр Вернама основан на шифре Цезаря, но чаще всего имеет реализацию с операцией XOR (Исключающее ИЛИ).

      Message: rip and tear until
          Key: None
Final message: ('PSZSQDOAAUSUGTVWXF', '24.10.10.25.16.16.11.7.7.16.18.3.13.25.8.3.15.20')
"""

from random import randint
from re import findall


def regular(text):
    template = r"[0-9]+"
    return findall(template, text)


def encryptDecrypt(mode, message, final="", keys=[]):
    if mode == 'E':
        for symbol in message:
            key = randint(0, 25)
            keys.append(str(key))
            final += chr((ord(symbol) + key - 13) % 26 + ord('A'))
        return final, '.'.join(keys)
    else:
        keys = input("Write the keys: ")
        for index, symbol in enumerate(message):
            final += chr((ord(symbol) - int(regular(keys)[index]) - 13) % 26 + ord('A'))
        return final


if __name__ == '__main__':
    cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
    if cryptMode not in ['E', 'D']:
        print("Error: mode is not Found!")
        raise SystemExit
    startMessage = input("Write the message: ").upper()
    print("Final message:", encryptDecrypt(cryptMode, startMessage))
