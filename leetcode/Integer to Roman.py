class Solution:
    def intToRoman(self, num: int) -> str:
        answer = ""

        mapp = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10:"X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }


        value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        for i in range(len(value)):
            cur = value[i]
            if num >= cur:
                mok = num//cur
                answer += (mok * mapp[cur])
                num = (num%cur)
        
        return answer