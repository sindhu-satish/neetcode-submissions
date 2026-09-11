class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s))
            encoded_str += "#"
            encoded_str += s
        return encoded_str


    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0

        while(i<len(s)):
            j = i
            if s[j] != "#":
                j = j+1
            length = int(s[i:j])
            temp_str = s[j + 1: j + 1 + length]
            decoded_strs.append(temp_str)
            i += j + 1 + length
        return decoded_strs


