def count_pairs(k, numbers):
    count = 0
    remainder_count = [0] * k

    for num in (numbers):
        remainder = num % k
        complement = (k - remainder) % k
        count += remainder_count[complement]
        remainder_count[remainder] += 1

    return count