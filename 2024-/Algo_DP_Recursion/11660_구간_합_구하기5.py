"""
문제
    N×N개의 수가 N×N 크기의 표에 채워져 있다. (x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램을 작성하시오. (x, y)는 x행 y열을 의미한다.
    예를 들어, N = 4이고, 표가 아래와 같이 채워져 있는 경우를 살펴보자.

    1	2	3	4
    2	3	4	5
    3	4	5	6
    4	5	6	7
    여기서 (2, 2)부터 (3, 4)까지 합을 구하면 3+4+5+4+5+6 = 27이고, (4, 4)부터 (4, 4)까지 합을 구하면 7이다.
    표에 채워져 있는 수와 합을 구하는 연산이 주어졌을 때, 이를 처리하는 프로그램을 작성하시오.

입력
    첫째 줄에 표의 크기 N과 합을 구해야 하는 횟수 M이 주어진다. (1 ≤ N ≤ 1024, 1 ≤ M ≤ 100,000)
    둘째 줄부터 N개의 줄에는 표에 채워져 있는 수가 1행부터 차례대로 주어진다.
    다음 M개의 줄에는 네 개의 정수 x1, y1, x2, y2 가 주어지며, (x1, y1)부터 (x2, y2)의 합을 구해 출력해야 한다.
    표에 채워져 있는 수는 1,000보다 작거나 같은 자연수이다. (x1 ≤ x2, y1 ≤ y2)

출력
    총 M줄에 걸쳐 (x1, y1)부터 (x2, y2)까지 합을 구해 출력한다.

4 3
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
2 2 3 4
3 4 3 4
1 1 4 4
"""
import sys


def input_data():
    n, m = map(int, sys.stdin.readline().split())
    nums = [[0] * (n + 1)] + [[0] + list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    test_cases = []
    for i in range(m):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        test_cases.append((x1, y1, x2, y2))

    return n, nums, test_cases


def get_dp(n, nums):
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            dp[x][y] = dp[x - 1][y] + dp[x][y - 1] - dp[x - 1][y - 1] + nums[x][y]
    return dp


def solve(n, nums, test_cases):
    dp = get_dp(n, nums)

    for x1, y1, x2, y2 in test_cases:
        if x1 == x2 and y1 == y2:
            print(nums[x1][y1])
            continue
        else:
            total = dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]
            print(total)


if __name__ == '__main__':
    n, nums, test_cases = input_data()
    solve(n, nums, test_cases)
