class Message:
    def __init__(self, text="") -> None:
        self.text = text

    def get_text(self) -> str:
        return self.text

    def create_message(self, text: str) -> None:
        self.text = text

    def __str__(self) -> str:
        return self.text


class EncryptedMessage(Message):
    def __init__(self, text="") -> None:
        super().__init__(text)
        self.__state = "NO MESSAGE"

    def get_state(self) -> str:
        return self.__state

    def create_message(self, text: str) -> None:
        self.text = text
        self.__state = "ORIGINAL"

    def encrypt(self, key: int) -> None:
        encrypted_text = ""
        for i in range(len(self.text)):
            encrypted_text += chr(ord(self.text[i]) + key)
        self.text = encrypted_text
        self.__state = "ENCRYPTED"

    def decrypt(self, key: int) -> None:
        decrypted_text = ""
        for i in range(len(self.text)):
            decrypted_text += chr(ord(self.text[i]) - key)
        self.text = decrypted_text
        self.__state = "DECRYPTED"

    def __str__(self) -> str:
        return "Encrypted message: " + super().__str__()
