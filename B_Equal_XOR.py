from itertools import combinations
from collections import Counter
def find_subsets(array, k):
    n = len(array)
    first_half = array[:n//2]
    second_half = array[n//2:]

    # Calculate XOR of both halves
    xor_first = xor_second = 0
    for num in first_half:
        xor_first ^= num
    for num in second_half:
        xor_second ^= num

    # Find the most common XOR value
    most_common_xor = xor_first ^ xor_second

    # Count frequency of each element in both halves
    freq_first_half = Counter(first_half)
    freq_second_half = Counter(second_half)

    # Select 2k elements from each half that contribute to the most common XOR value
    subset1 = []
    subset2 = []
    for num in array:
        if num in freq_first_half and freq_first_half[num] > 0 and num ^ xor_first == most_common_xor:
            subset1.append(num)
            freq_first_half[num] -= 1
            if len(subset1) == 2 * k:
                break
        elif num in freq_second_half and freq_second_half[num] > 0 and num ^ xor_second == most_common_xor:
            subset2.append(num)
            freq_second_half[num] -= 1
            if len(subset2) == 2 * k:
                break

    return subset1, subset2
test_cases = int(input())
for _ in range(test_cases):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    l, r = find_subsets(arr, k)
    print(*l)
    print(*r)