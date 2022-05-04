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
    
    def verify_key(self, key: int) -> bool:
        if key < 0 or key > 9999:
            return False
        if self.__state == "ENCRYPTED":
            for i in range(len(self.text)):
                if ord(self.text[i]) - key < ord(' '):
                    return False
        return True

    def encrypt(self, key: int) -> None:
        if not self.verify_key(key) or self.__state == "ENCRYPTED":
            self.__state = "ENCRYPTION FAILED"
            return
        encrypted_text = ""
        for i in range(len(self.text)):
            encrypted_text += chr(ord(self.text[i]) + key)
        self.text = encrypted_text
        self.__state = "ENCRYPTED"

    def decrypt(self, key: int) -> None:
        if not self.verify_key(key) or self.__state not in ["ENCRYPTED", "DECRYPTION FAILED"]:
            self.__state = "DECRYPTION FAILED"
            return
        decrypted_text = ""
        for i in range(len(self.text)):
            decrypted_text += chr(ord(self.text[i]) - key)
        self.text = decrypted_text
        self.__state = "DECRYPTED"

    def __str__(self) -> str:
        return "Encrypted message: " + super().__str__()
