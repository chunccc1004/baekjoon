"""
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	15219	5708	4258	37.068%

문제
    세계적인 호텔인 형택 호텔의 사장인 김형택은 이번에 수입을 조금 늘리기 위해서 홍보를 하려고 한다.
    형택이가 홍보를 할 수 있는 도시가 주어지고, 각 도시별로 홍보하는데 드는 비용과, 그 때 몇 명의 호텔 고객이 늘어나는지에 대한 정보가 있다.
    예를 들어, “어떤 도시에서 9원을 들여서 홍보하면 3명의 고객이 늘어난다.”와 같은 정보이다.
    이때, 이러한 정보에 나타난 돈에 정수배 만큼을 투자할 수 있다.
    즉, 9원을 들여서 3명의 고객, 18원을 들여서 6명의 고객, 27원을 들여서 9명의 고객을 늘어나게 할 수 있지만, 3원을 들여서 홍보해서 1명의 고객, 12원을 들여서 4명의 고객을 늘어나게 할 수는 없다.
    각 도시에는 무한 명의 잠재적인 고객이 있다. 이때, 호텔의 고객을 적어도 C명 늘이기 위해 형택이가 투자해야 하는 돈의 최솟값을 구하는 프로그램을 작성하시오.

입력
    첫째 줄에 C와 형택이가 홍보할 수 있는 도시의 개수 N이 주어진다. C는 1,000보다 작거나 같은 자연수이고, N은 20보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 각 도시에서 홍보할 때 대는 비용과 그 비용으로 얻을 수 있는 고객의 수가 주어진다. 이 값은 100보다 작거나 같은 자연수이다.

출력
    첫째 줄에 문제의 정답을 출력한다.
"""
import sys


def input_data():
    c, n = map(int, sys.stdin.readline().split())
    hotels = []

    for _ in range(n):
        cost, customer = map(int, sys.stdin.readline().split())
        hotels.append([cost, customer])

    return c, hotels


def solve(c, hotels):
    INF = sys.maxsize
    dp = [INF] * (c + 100)
    dp[0] = 0

    for cost, customer in hotels:
        for i in range(customer, c + 100):
            dp[i] = min(dp[i], dp[i - customer] + cost)

    print(min(dp[c:]))


if __name__ == '__main__':
    c, hotels = input_data()
    solve(c, hotels)
