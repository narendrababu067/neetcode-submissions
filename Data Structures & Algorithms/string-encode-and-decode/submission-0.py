from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        
        for word in strs:
            result += str(len(word)) + "#" + word
        
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        
        while i < len(s):
            j = i
            
            # find the '#'
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])   # get length
            word = s[j+1 : j+1+length]  # extract word
            
            result.append(word)
            
            i = j + 1 + length  # move to next
        
        return result