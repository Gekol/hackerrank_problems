from typing import List


def absolute_diagonal_difference(matrix: List[List[int]]):
    left_diagonal, right_diagonal = 0, 0
    for i in range(len(matrix)):
        left_diagonal += matrix[i][i]
        right_diagonal += matrix[i][(i * -1) - 1]
    return abs(left_diagonal - right_diagonal)


def main():
    n = int(input())
    matrix = []
    for i in range(n):
        row = map(int, input().rstrip().split())
        matrix.append(row)
    print(absolute_diagonal_difference(matrix))


if __name__ == "__main__":
    main()
