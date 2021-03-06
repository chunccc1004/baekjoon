# 하루에 한 시간 단위로 일을 하거나 일을 쉬어도 된다. 하루에 한 시간 일하면 피로도는 A 만큼 쌓이고 일은 B 만큼 처리할 수 있다.
# 만약에 한 시간을 쉰다면 피로도는 C 만큼 줄어든다. 단, 피로도가 음수로 내려가면 0으로 바뀐다. 당연히 일을 하지 않고 쉬었기 때문에 처리한 일은 없다.
# 피로도를 최대한 M 을 넘지 않게 일을 하려고 한다. M 를 넘기면 일하는데 번아웃이 와서 이미 했던 일들도 다 던져버리고 일을 그만두게 된다.
# 번아웃이 되지 않도록 일을 할때 하루에 최대 얼마나 일을 할 수 있는지 구해보자. 하루는 24시간이다.

# 첫 번째 줄에 네 정수 A, B, C, M이 공백으로 구분되어 주어진다.
# 맨 처음 피로도는 0이다.

"""
1시간 일했을 때
피로도 : +A
한 일 : +B

1시간 쉈을 때
피로도 : -C

M이 최대 피로도
P는 현재 피로도

1시간 일했을 때
체력 : P + A <= M 이어야 함
일은 : A가 호출된 횟수 * B

1시간 쉈을 때
체력 : P - C -> 만약 P>C -> P = 0

for 문으로 24시간을 확인해도 괜찮을듯..? 최대 반복이 24니까
"""
A,B,C,M = map(int,input().split())
P = 0 # 현재 피로도

Cnt = 0
for _ in range(24) :
    if P + A <= M : #일할 수 있는 상태
        P += A
        Cnt += 1
        continue
    else:
        P -= C
        if P < 0 :
            P =0
print(Cnt*B)