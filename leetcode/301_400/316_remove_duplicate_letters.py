"""
316. Remove Duplicate Letters
Given a string s, remove duplicate letters so that every letter appears once and only once. Y
ou must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"


Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
"""


class RemoveDuplicateLetters:
    def draw(self, seq: str):
        result = self.remove_duplicate(seq)
        print(result)

    def remove_duplicate(self, seq: str) -> str:
        output = []
        for out in seq:
            if out not in output:
                output.append(out)
            else:
                if output[-1] < out:
                    output.remove(out)
                    output.append(out)
                else:
                    index = output.index(out)
                    if index >0:
                        if not (output[index - 1] < output[index] < output[index + 1]):
                            output.remove(out)
                            output.append(out)
                    else:
                        if not (output[index] < output[index + 1]):
                            output.remove(out)
                            output.append(out)


        pass


sequence1 = "bcabc"
sequence2 = "cbacdcbc"
obj = RemoveDuplicateLetters()
# obj.draw(sequence1)
obj.draw(sequence2)
