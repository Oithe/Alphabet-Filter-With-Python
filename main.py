class AlphabetFilter_Solution:

    def __init__(self, s):
        self.s = s

    def filter_vowels(self):
        for i in s:
            if i == 'b' or i == 'c' or i == 'd' or i == 'f' or i == 'g' or i == 'h' or i == 'j' or i == 'k' or i == 'l' or i == 'm' or i == 'n' or i == 'p' or i == 'q' or i == 'r' or i == 's' or i == 't' or i == 'v' or i == 'w' or i == 'x' or i == 'y' or i == 'z':
                print(i, end = '')


    def filter_consonants(self):
        for i in s:
            if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
                print(i, end = '')


s = input("Enter the desired word: ")
f = AlphabetFilter_Solution(s)
f.filter_vowels()
print()
f.filter_consonants()
