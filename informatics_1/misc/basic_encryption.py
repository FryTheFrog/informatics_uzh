class Message:
    def __init__(self, text="") -> None:
        self.text = text

    def ask_message(self) -> None:
        self.text = input("\nEnter message: ")

    def print_message(self) -> None:
        print("\nMessage:", self.text)

    def __str__(self) -> str:
        return self.text


class EncryptedMessage(Message):
    def __init__(self, text="") -> None:
        super().__init__(text)
        self.__state = "original"

    def get_state(self) -> str:
        return self.__state

    def ask_key(self) -> int:
        key = int(input("Enter key: "))
        return key

    def encrypt(self, key: int) -> None:
        encrypted_text = ""
        for i in range(len(self.text)):
            encrypted_text += chr(ord(self.text[i]) + key)
        self.text = encrypted_text
        self.__state = "encrypted"

    def decrypt(self, key: int) -> None:
        decrypted_text = ""
        for i in range(len(self.text)):
            decrypted_text += chr(ord(self.text[i]) - key)
        self.text = decrypted_text
        self.__state = "decrypted"

    def print_message(self) -> None:
        match self.get_state():
            case "original":
                print("\nmessage: ", self.text)
            case "encrypted":
                print("\nencrypted message: ", self.text)
            case "decrypted":
                print("\ndecrypted message: ", self.text)


def main():
    message = EncryptedMessage()
    message.ask_message()
    message.encrypt(message.ask_key())
    message.print_message()
    message.decrypt(message.ask_key())
    message.print_message()


main()
