# 세준이는 length × width × height 크기의 박스를 가지고 있다. 그리고 세준이는 이 박스를 큐브를 이용해서 채우려고 한다.
# 큐브는 정육면체 모양이며, 한 변의 길이는 2의 제곱꼴이다. (1×1×1, 2×2×2, 4×4×4, 8×8×8, ...)
# 세준이가 가지고 있는 박스의 종류와 큐브의 종류와 개수가 주어졌을 때, 박스를 채우는데 필요한 큐브의 최소 개수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 세 자연수 length width height가 주어진다.
# 둘째 줄에 세준이가 가지고 있는 큐브의 종류의 개수 N이 주어진다.
# 셋째 줄부터 총 N개의 줄에 큐브의 종류 Ai와 개수 Bi가 i가 증가하는 순서대로 주어진다. 큐브의 종류는 한 변의 길이를 나타낼 때 쓰는 2^i에서 i이다.

# 출력
# 첫째 줄에 필요한 큐브의 개수의 최솟값을 출력한다. 만약 채울 수 없다면 -1을 출력한다.
"""
In
4 4 8
3
0 10
1 10
2 1

Out
9

흠.. 어떻게 풀어야 할까..
일단 2의 제곱인 애들을 값으로 변경하자
그냥 부피로 될지 안될지 계산하면.. 안끼워지는 것도 있고 그래서 안될라나..
그럼 가로, 세로, 높이를 각자 넣으면서 계산하고 비교하면 어떨까??

분할 알고리즘이라고 했잖아..?
그러면 1 1 1 1 1 ... 일케 돼어 있는 걸 합쳐서?
부피로..?
아 모르겠는데..
"""

"""
정답 확인
박스 자체를 2^n x 2^n x 2^n으로 분할해 보면서 가지고 있는 큐브를 집어 넣어보는 것입니다.

4 4 8      - 박스의 가로, 세로, 높이
3            - 사용할 큐브의 종류
0 10       - 1 x 1 x 1 큐브 10개 보유 
1 10       - 2 x 2 x 2 큐브 10개 보유
2 1         - 4 x 4 x 4 큐브 1개 보유

현재, 큐브의 최대 사이즈는 4 x 4 x 4이기때문에 박스를 4 x 4 x 4 부터 1 x 1 x 1까지 차례대로 분할해 봅시다.
박스는 4 x 4 x 8이기때문에 4 x 4 x 4로 분할하면 1 x 1 x 2 = 2개로 되는 것을 알 수 있습니다.
하지만, 4 x 4 x 4 큐브는 1개를 갖고 있기때문에 1개만 넣는 것이 가능합니다.
그리고 과거에 넣었던 큐브의 개수를 before라는 변수에 저장해 둡시다. 현재 before는 1인 상태입니다.

다음은, 박스를 2 x 2 x 2로 분할해 봅시다.
박스는 4 x 4 x 8이기 때문에 2 x 2 x 2로 분할하면 2 x 2 x 4 = 16개로 되는 것을 알 수 있습니다.
하지만, 4 x 4 x 4짜리 큐브가 이미 들어가 있는 상태이기때문에 4 x 4 x 4 큐브도 2 x 2 x 2 큐브로 분할함으로써 before에 8을 곱해주어야 합니다. 
따라서, 현재 박스에 들어갈 수 있는 2 x 2 x 2 큐브는 16 - 8 = 8개임을 알 수 있습니다. 그리고 이 8을 before에 더 해주게되면, before = 16이 됩니다.

마지막으로, 박스를 1 x 1 x 1로 분할해 봅시다.
박스는 4 x 4 x 8이기 때문에 1 x 1 x 1로 분할하면 4 x 4 x 8 = 128개로 되는 것을 알 수 있습니다.
하지만, 4 x 4 x 4와 2 x 2 x 2큐브가 이미 들어가 있는 상태이기때문에 기존에 before에다가 8을 곱해주어야합니다.

따라서, 현재 박스에 들어갈 수 있는 1 x 1 x 1큐브는 128 - 128 = 0개임을 알 수 있습니다.
1 x 1 x 1 분할이 완료되었으면, 더이상 분할 작업은 진행하지 않습니다.

이제, before과 실제 박스의 부피가 같은지 비교해 보아야 합니다.
before = 128이고, L X W X H = 128로 서로 같다는 것을 알 수 있습니다.
따라서, 박스에 들어갈 수 있는 큐브의 최솟값은 1 + 8 = 9개라는 결론을 내릴 수 있습니다.
"""
length, width, height = map(int, input().split())
n = int(input())
cube = [list(map(int, input().split())) for _ in range(n)]
volume = length * width * height
ans = 0
before = 0
cube.sort(reverse=True)

for w, cnt in cube:
    before <<= 3
    v = 2 ** w
    maxCnt = (length // v) * (width // v) * (height // v) - before
    maxCnt = min(cnt, maxCnt)
    ans += maxCnt
    before += maxCnt

if before == volume:
    print(ans)
else:
    print(-1)