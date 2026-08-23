def BinarySearch(List, Value, middle):
    if List[middle] == Value: return middle

    else:
        if List[middle] < Value: return BinarySearch(List[middle + 1:], Value, (middle - 1) // 2) + middle + 1

        else: return BinarySearch(List[: middle], Value, (middle) // 2)

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(BinarySearch(L, 5, len(L) // 2))


# NOT COMPLETED: WRONG ANSWERS