# from PyPDF2 import PdfFileReader, PdfFileWriter
#
# file = PdfFileReader("Event_Monthly_Report.pdf")
# total_page = file.numPages
#
# out = PdfFileWriter()
# for page_i in range(total_page):
#     page_data = file.getPage(page_i)
#     out.addPage(page_data)
#
# password = input("Please set password for file encryption: ")
# out.encrypt(password)
#
# protected_file = "protected_file.pdf"
# with open(protected_file, "wb") as fl:
#     out.write(fl)
#
# print("File was saved in %s " % protected_file)
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = [[]]

        for num in nums:
            newarr = [curr + [num] for curr in output]
            output += newarr


        return output

    def permutaltion(self,n):
        output = [[]]
        for num in range(n):
            marr = [out + [num] for out in output]
            output +=marr
        return len(output) - 1

    def removeDuplicateLetters(self, s: str) -> str:
        output = []
        for out in s:
            if out not in output:
                output.append(out)
            else:
                output.remove(out)
                output.append(out)

        # output.sort()
        return "".join

m = Solution()
lis = [1,2,3,4,5,6]
# print(m.subsets(lis))
# print(m.permutaltion(3))

s = "cbacdcbc"
m.removeDuplicateLetters(s)