def max_subsequence_length(n, sequence):
    dp = [1] * n

    for j in range(n):
        for i in range(j):
            if sequence[i] | sequence[j] == sequence[j]:
                dp[j] = max(dp[j], dp[i] + 1)

    return max(dp)


n = int(input())
sequence = list(map(int, input().split()))

print(max_subsequence_length(n, sequence))
