class Solution:
    def isValid(self, s: str) -> bool:
        new_string = []
        maping = {")":"(","]":"[","}":"{"}
        for char in s:
            if char in "([{ ":
                new_string.append(char)
            elif char in ")]}":
                if not new_string:
                    return False
                val = new_string.pop()
                if val == maping[char]:
                    continue
                else:
                    return False
        return len(new_string) == 0