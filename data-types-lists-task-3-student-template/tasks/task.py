from typing import List


def foo(nums: List[int]) -> List[int]:
    # TODO: Add your code here
    total_product = get_total_product(nums)
    result = []
    for i in nums:
        result.append(total_product // i)
    return result

def get_total_product(nums: List[int]) -> int:
    result = 1
    for num in nums:
        result *= num
    return result