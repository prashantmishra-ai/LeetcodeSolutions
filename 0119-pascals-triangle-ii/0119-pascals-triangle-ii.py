from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]

        prev_row = [1, 1]
        for _ in range(2, rowIndex + 1):
            curr_row = [1]
            for i in range(1, len(prev_row)):
                curr_row.append(prev_row[i-1] + prev_row[i])
            curr_row.append(1)
            prev_row = curr_row
        
        return curr_row