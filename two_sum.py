def two_sum(nums: list[int], target: int) -> list[int]:

    for n_a, item_a in enumerate(nums):

        for n_b, item_b in enumerate(nums):
            if n_a != n_b:
                if item_a + item_b == target:
                    return [n_a, n_b]


i, j = two_sum(nums=[2, 7, 11, 15], target=26)
print(i, j)
