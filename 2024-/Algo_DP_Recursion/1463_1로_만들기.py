"""
문제
    정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
        X가 3으로 나누어 떨어지면, 3으로 나눈다.
        X가 2로 나누어 떨어지면, 2로 나눈다.
        1을 뺀다.
    정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

입력
    첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.

출력
    첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
"""


def solve():
    x = int(input())
    if x == 1:
        print(0)
        return
    elif x == 2 or x == 3:
        print(1)
        return

    def make_dp(x):
        dp = [0] * (x + 1)
        dp[2] = 1
        dp[3] = 1

        for i in range(4, x + 1):
            pre_list = []

            if i % 3 == 0:
                pre_list.append(dp[i // 3])
            if i % 2 == 0:
                pre_list.append(dp[i // 2])

            pre_list.append(dp[i - 1])

            dp[i] = min(pre_list) + 1

        return dp

    dp = make_dp(x)
    print(dp[x])


if __name__ == '__main__':
    solve()
