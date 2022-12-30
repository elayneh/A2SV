class Solution:
    def sentense_sorter(self, sentence):
        s = sentence.split()
        n = len(s)
        sentence = [""] * n

        for c in s:
            i = int(c[-1])
            sentence[i - 1] = c[:-1]

        return " ".join(sentence)

if __name__ == "__main__":

    sol = Solution()
    print(sol.sentense_sorter("this2 is0 the1 sentence3"))
