from typing import List

def check(row_start:int, row_end:int, column_start:int, column_end:int) -> List[List[int]]:
    """
    Add your code here or call it from here   
    """
    result = []
    for i in range(row_start, row_end + 1):
        row_result = []
        for j in range(column_start, column_end + 1):
            row_result.append(i * j)
        result.append(row_result)
    return result
