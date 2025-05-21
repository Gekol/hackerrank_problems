from typing import List


def big_sum(arr: List[int]) -> int:
    s = 0
    for num in arr:
        s += int(num)
    return s


def main():
    arr = map(int, input().rstrip().split())
    print(big_sum(arr))


if __name__ == "__main__":
    main()
