class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ansArr = []
        for i in operations:
            if i == "+":
                ansArr.append(ansArr[-1] + ansArr[-2])
            elif i == "C":
                ansArr.pop()
            elif i == "D":
                ansArr.append(int(ansArr[-1]) * 2)
            else:
                ansArr.append(int(i))

        return sum(ansArr)