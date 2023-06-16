def longest_increasing_subsequence(seq):
    n = len(seq)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if seq[i] > seq[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


print(26 - longest_increasing_subsequence(input()))
