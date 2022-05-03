class Message:
    def __init__(self, text=""):
        self.text = text
        self.__state = "original"
    
    def get_state(self):
        return self.__state

    def ask_message(self):
        self.text = input("\nEnter message: ")
    
    def ask_key(self):
        key = int(input("Enter key: "))
        return key
    
    def encrypt(self, key):
        encrypted_text = ""
        for i in range(len(self.text)):
            encrypted_text += chr(ord(self.text[i]) + key)
        self.text = encrypted_text
        self.__state = "encrypted"
    
    def decrypt(self, key):
        decrypted_text = ""
        for i in range(len(self.text)):
            decrypted_text += chr(ord(self.text[i]) - key)
        self.text = decrypted_text
        self.__state = "decrypted"
    
    def print_message(self):
        match self.get_state():
            case "original":
                print("\nmessage: ", self.text)
            case "encrypted":
                print("\nencrypted message: ", self.text)
            case "decrypted":
                print("\ndecrypted message: ", self.text)

def main():
    message = Message()
    message.ask_message()
    message.encrypt(message.ask_key())
    message.print_message()
    message.decrypt(message.ask_key())
    message.print_message()

main()
