"""Find the contiguous subarray that contains ``0`` and has the maximum sum.

The previous implementation computed every possible subarray and therefore had
``O(n^3)`` complexity.  This version uses a pair of Kadane style passes to
achieve ``O(n)`` time while also returning the actual subarray.

>>> attack([-1, 2, 0, 3, -2])
[2, 0, 3]
"""


def attack(arr_data):
    """Return the subarray with maximum sum that includes a ``0``.

    Parameters
    ----------
    arr_data: list[int]
        Input array which must contain at least one ``0``.

    Returns
    -------
    list[int]
        The contiguous subarray containing ``0`` with the largest possible sum.
    """

    if 0 not in arr_data:
        raise ValueError("Input array must contain at least one zero")

    n = len(arr_data)
    # Kadane from the left – max sum ending at each index and its start position
    left_sum = [0] * n
    left_start = [0] * n
    max_ending = arr_data[0]
    start = 0
    left_sum[0] = arr_data[0]
    left_start[0] = 0
    for i in range(1, n):
        if max_ending + arr_data[i] < arr_data[i]:
            max_ending = arr_data[i]
            start = i
        else:
            max_ending += arr_data[i]
        left_sum[i] = max_ending
        left_start[i] = start

    # Kadane from the right – max sum starting at each index and its end position
    right_sum = [0] * n
    right_end = [0] * n
    max_start = arr_data[-1]
    end = n - 1
    right_sum[-1] = arr_data[-1]
    right_end[-1] = n - 1
    for i in range(n - 2, -1, -1):
        if max_start + arr_data[i] < arr_data[i]:
            max_start = arr_data[i]
            end = i
        else:
            max_start += arr_data[i]
        right_sum[i] = max_start
        right_end[i] = end

    best_sum = None
    best_start = best_end = 0
    for i, val in enumerate(arr_data):
        if val == 0:
            curr_sum = left_sum[i] + right_sum[i]
            if best_sum is None or curr_sum > best_sum:
                best_sum = curr_sum
                best_start = left_start[i]
                best_end = right_end[i]

    return arr_data[best_start : best_end + 1]


if __name__ == "__main__":
    arr = [-1, 2, 0, 3, -2]
    print(attack(arr))
