class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total = 0
        record = []

        for item in operations:
            if item == "+":
                record.append(record[-1] + record[-2])
            elif item == "D":
                record.append(record[-1] * 2)
            elif item == "C":
                record.pop()
            else:
                record.append(int(item))

        for score in record:
            total += score

        return total

        

        