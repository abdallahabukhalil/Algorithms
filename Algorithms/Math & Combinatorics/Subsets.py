def AllSubsets(elements: list) -> None:

    """Print all subsets of the set of elements"""

    n = len(elements)

    for mask in range(1 << n): # 1 << n == 2^n
        current_subset = []

        for i in range(n):
            if (mask >> i) & 1 == 1:
                current_subset.append(elements[i])

        print(current_subset)



elements = ["A", "B", "C"]
AllSubsets(elements)