class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for word in strs:
            w = ""
            for letter in word:
                w += chr(ord(letter) + 3)
            encoded = encoded + w + " "
        
        return encoded

    def decode(self, s: str) -> List[str]:  
        text = []

        current_word = ""
        for letter in s:
            if letter == " ":
                text.append(current_word)
                current_word = ""
            else:
                current_word += chr(ord(letter) - 3)

        return text