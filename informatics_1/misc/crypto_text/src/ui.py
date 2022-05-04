import os
from src.message import EncryptedMessage


class UI:
    def __init__(self) -> None:
        self.message = EncryptedMessage()
        self.text = ""
        self.status = ""
        self.menu = main_menu

    def clear(self) -> None:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def change_message(self, text: str) -> None:
        self.message.create_message(text)
        self.update_text()

    def encrypt_message(self, key: int) -> None:
        self.message.encrypt(key)
        self.update_all()

    def decrypt_message(self, key: int) -> None:
        self.message.decrypt(key)
        self.update_all()

    def update_text(self) -> None:
        text = self.message.get_text()
        if self.message.get_state() == "ENCRYPTED":
            text = [char for char in text]
        else:
            text = text.split()
        res = "| "
        l = 1
        for i in text:
            if len(res + i) + 2 <= 64 * l:
                res += i + " "
            else:
                if l == 1:
                    res += (63 - (len(res))) * " " + "|\n| " + i + " "
                else:
                    res += (63 - (len(res) % 65)) * " " + "|\n| " + i + " "
                l += 1
        res += (63 - (len(res) % 65)) * " " + "|"
        self.text = res

    def update_status(self) -> None:
        res = self.message.get_state()
        res = (57 - len(res)) * " " + "-> " + res
        self.status = res

    def update_menu(self, menu: str) -> None:
        if menu == "e":
            self.menu = encrypt_menu
        elif menu == "d":
            self.menu = decrypt_menu
        else:
            self.menu = main_menu

    def update_all(self) -> None:
        self.update_text()
        self.update_status()

    def print_ui(self) -> None:
        self.update_all()
        self.clear()
        print(interface.format(self.text, self.status, self.menu))


interface = """
----------------------------------------------------------------
|                         CRYPTO_TEXT                          |
----------------------------------------------------------------
|                                                              |
{}
|                                                              |
----------------------------------------------------------------
| {} |
----------------------------------------------------------------
{}"""

main_menu = """| 'q' to quit | 'e' to encrypt | 'd' to decrypt | 'r' to reset |
|                      or enter a message                      |"""

encrypt_menu = """| enter a 4-digit key to ENCRYPT                               |"""

decrypt_menu = """| enter a 4-digit key to DECRYPT                               |"""
