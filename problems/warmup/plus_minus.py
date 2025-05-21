from typing import List


def calculate_ratio(nums: List[int]) -> List[str]:
    n = len(nums)
    positive, negative, zero = 0, 0, 0
    for num in nums:
        if num > 0:
            positive += 1
        elif num < 0:
            negative += 1
        else:
            zero += 1
    return [f"{(positive/n):.6f}", f"{(negative/n):.6f}", f"{(zero/n):.6f}"]


def main():
    n = int(input())
    nums = list(map(int, input().rstrip().split()))
    for ratio in calculate_ratio(nums):
        print(ratio)


if __name__ == "__main__":
    main()