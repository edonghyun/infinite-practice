class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        lists = [
            []
            for _ in range(numRows)
        ]

        direction = "UP"
        bounce_count = 0
        for char in s:
            lists[bounce_count].append(char)

            if bounce_count == 0:
                direction = "UP"

            if bounce_count == numRows-1:
                direction = "DOWN"

            if direction == "UP":
                bounce_count += 1
            else:
                bounce_count -= 1

        result = ""
        for _list in lists:
            result += "".join(_list)
        return result
