"""
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	256 MB	7546	4082	3341	53.792%
문제
    ChAOS(Chung-ang Algorithm Organization and Study) 회장이 되어 일이 많아진 준석이는 시험기간에도 일 때문에 공부를 하지 못하다가 시험 전 날이 되어버리고 말았다.
    다행히도 친절하신 교수님께서 아래와 같은 힌트를 시험 전에 공지해 주셨다. 내용은 아래와 같다.
        1. 여러 단원을 융합한 문제는 출제하지 않는다.
        2. 한 단원에 한 문제를 출제한다. 단, 그 단원에 모든 내용을 알고 있어야 풀 수 있는 문제를 낼 것이다.
    이런 두가지 힌트와 함께 각 단원 별 배점을 적어 놓으셨다. 어떤 단원의 문제를 맞추기 위해서는 그 단원의 예상 공부 시간만큼, 혹은 그보다 더 많이 공부하면 맞출 수 있다고 가정하자.
    이때, ChAOS 회장 일로 인해 힘든 준석이를 위하여 남은 시간 동안 공부해서 얻을 수 있는 최대 점수를 구하는 프로그램을 만들어 주도록 하자.

입력
    첫째 줄에는 이번 시험의 단원 개수 N(1 ≤ N ≤ 100)과 시험까지 공부 할 수 있는 총 시간 T(1 ≤ T ≤ 10000)가 공백을 사이에 두고 주어진다.
    둘째 줄부터 N 줄에 걸쳐서 각 단원 별 예상 공부 시간 K(1 ≤ K ≤ 1000)와 그 단원 문제의 배점 S(1 ≤ S ≤ 1000)가 공백을 사이에 두고 주어진다.

출력
    첫째 줄에 준석이가 얻을 수 있는 최대 점수를 출력한다.
---
3 310
50 40
100 70
200 150

3 310
100 70
200 150
50 40
"""
import sys


def input_data():
    n, limit_time = map(int, sys.stdin.readline().split())
    expectation = [[0, 0]] + [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    expectation.sort()

    return n, limit_time, expectation


def solve(n, limit_time, expectation):
    dp = [[0] * (limit_time + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(limit_time + 1):
            if j >= expectation[i][0]:
                dp[i][j] = max(dp[i-1][j], dp[i - 1][j - expectation[i][0]] + expectation[i][1])
            else:
                dp[i][j] = dp[i - 1][j]

    print(max(dp[n]))


if __name__ == "__main__":
    n, limit_time, expectation = input_data()
    solve(n, limit_time, expectation)
