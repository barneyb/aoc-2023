def max_consecutive_ones(input):
    prev, curr = None, 0
    best = 0
    for d in input:
        if d == 1:
            curr += 1
        else:
            best = max(best, 1 + curr if prev is None else prev + 1 + curr)
            prev, curr = curr, 0
    if curr:
        best = max(best, curr if prev is None else prev + 1 + curr)
    return best


def sliding_window_is_slower(nums):
    longest_sequence = 0
    left, right = 0, 0
    num_zeroes = 0

    while right < len(nums):  # While our window is in bounds
        if nums[right] == 0:  # Increase num_zeroes if the rightmost element is 0
            num_zeroes += 1

        while num_zeroes == 2:  # If our window is invalid, contract our window
            if nums[left] == 0:
                num_zeroes -= 1
            left += 1

        longest_sequence = max(
            longest_sequence, right - left + 1
        )  # Update our longest sequence answer
        right += 1  # Expand our window

    return longest_sequence


def check(e, i):
    a = max_consecutive_ones(i)
    assert a == e, f"expected {e}, but got {a} for input {i}"
    a = sliding_window_is_slower(i)
    assert a == e, f"expected {e}, but got {a} for input {i}"


check(0, [])
check(1, [0])
check(1, [1])
check(2, [0, 1])
check(2, [1, 1])
check(1, [0, 0])
check(2, [1, 0])
check(2, [0, 1, 0])
check(3, [1, 1, 0])
check(1, [0, 0, 0])
check(2, [1, 0, 0])
check(3, [0, 1, 1])
check(3, [1, 1, 1])
check(2, [0, 0, 1])
check(3, [1, 0, 1])
check(2, [0, 1, 0, 0])
check(3, [1, 1, 0, 0])
check(1, [0, 0, 0, 0])
check(2, [1, 0, 0, 0])
check(3, [0, 1, 1, 0])
check(4, [1, 1, 1, 0])
check(2, [0, 0, 1, 0])
check(3, [1, 0, 1, 0])
check(3, [0, 1, 0, 1])
check(4, [1, 1, 0, 1])
check(2, [0, 0, 0, 1])
check(2, [1, 0, 0, 1])
check(4, [0, 1, 1, 1])
check(4, [1, 1, 1, 1])
check(3, [0, 0, 1, 1])
check(4, [1, 0, 1, 1])
check(4, [1, 0, 1, 1, 0])
check(2, [1, 0, 0, 0, 0, 0, 0, 1])
