def compare_triplets(arr1, arr2):
    points = [0, 0]
    for i in range(len(arr1)):
        if arr1[i] > arr2[i]:
            points[0] += 1
        elif arr2[i] > arr1[i]:
            points[1] += 1
    return points


def main():
    alice_points = map(int, input().rstrip().split())
    bob_points = map(int, input().rstrip().split())
    print(compare_triplets(alice_points, bob_points))


if __name__ == "__main__":
    main()
