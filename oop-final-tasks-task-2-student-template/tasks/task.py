class KeyChain:
    def __init__(self, key: str):
        self.key = key
        self.key_chain, self.reverse_key_chain = self.generate_key_chain(self.key) 
        
    def generate_key_chain(self, key):
        key_chain = {}
        reverse_key_chain = {}
        i = 0
        for c in key:
            if c not in key_chain:
                key_chain[c] = i
                reverse_key_chain[i] = c
                i += 1
        return key_chain, reverse_key_chain
    
    def get_index(self, c):
        return self.key_chain.get(c, -1)
    
    def get_char(self, i):
        return self.reverse_key_chain.get(i, -1)

class Cipher:
    DEFAULT_KEY = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    def __init__(self, key):
        self.key = (key + Cipher.DEFAULT_KEY).upper()
        self.key_chain = KeyChain(self.key)
        self.default_key_chain = KeyChain(Cipher.DEFAULT_KEY)
        
    def encode(self, data):
        result = ""
        for c in data:
            index = self.default_key_chain.get_index(c.upper())
            if index != -1:
                encoded_char = self.key_chain.get_char(index)
                if c.isupper():
                    result += encoded_char.upper()
                else:
                    result += encoded_char.lower()
            else:
                result += c
        return result
    
    def decode(self, data):
        result = ""
        for c in data:
            index = self.key_chain.get_index(c.upper())
            if index != -1:
                decoded_char = self.default_key_chain.get_char(index)
                if c.isupper():
                    result += decoded_char.upper()
                else:
                    result += decoded_char.lower()
            else:
                result += c
        return result