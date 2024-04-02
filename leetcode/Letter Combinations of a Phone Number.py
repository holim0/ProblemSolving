from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        answer = []

        number_dict = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"]
        }
        mapp = []


        for d in digits:
            mapp.append(number_dict[int(d)])

        answer = list(product(*mapp))

        real_answer = []

        for value in answer:
            a = "".join(value)
            real_answer.append(a)

        return real_answer