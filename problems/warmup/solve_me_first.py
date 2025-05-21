def sum_func(a: int, b: int) -> int:
    return a + b


def main():
    a = int(input("Enter the first value"))
    b = int(input("Enter the second value"))
    print(f"Sum - {sum_func(a, b)}")


if __name__ == '__main__':
    main()
