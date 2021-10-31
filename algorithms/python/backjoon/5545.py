'''
https://www.acmicpc.net/problem/5545

상근이는 근처 피자 가게에서 매일 저녁으로 피자를 배달해 먹는다. 주머니 사정이 얇아진 상근이는 이번 달부터는 "최고의 피자"를 구매하려고 한다. 최고의 피자란, 피자 가게에서 주문할 수 있는 피자 중 1원당 열량이 가장 높은 피자를 말한다. 최고의 피자는 여러 종류가 있을 수도 있다.

이 피자 가게는 토핑 N개에서 여러 종류를 선택해서 주문할 수 있다. 같은 종류의 토핑을 2개 이상 선택할 수는 없다. 또, 토핑을 전혀 선택하지 않을 수도 있다.

선택한 토핑은 도우 위에 올라간다. 도우의 가격은 A원이고, 토핑의 가격은 모두 B원이다. 피자의 가격은 도우와 토핑의 가격의 합계가 된다. 즉, 토핑을 k종류 (0 ≤ k ≤ N) 선택했다면, 피자의 가격은 A + B*k원이 된다. 피자의 열량은 도우와 토핑의 열량의 합이다.

도우의 가격, 토핑의 가격, 그리고 도우와 각 토핑의 열량 값이 주어졌을 때, 최고의 피자의 1원 당 열량을 구하는 프로그램을 작성하시오.

'''

# 총 열량 / 가격 1원당 열량 가장 큰 피자 최고의파자
# (열랑은 클수록, 가격은 낮을수록)


def solve(dough_price,
          dough_kalory,
          topping_price,
          topping_kalories):
    topping_kalories.sort(reverse=True)

    total_kalories = dough_kalory
    total_price = dough_price

    kalories_per_price = total_kalories / total_price
    old_kalories_per_price = 0

    for kalory in topping_kalories:
        old_kalories_per_price = kalories_per_price

        total_kalories += kalory
        total_price += topping_price

        kalories_per_price = total_kalories / total_price
        # 토핑을 추가함으로써 1원당 칼로리가 그대로거나 감소함.
        if kalories_per_price <= old_kalories_per_price:
            break

    return int(old_kalories_per_price)


topping_count = int(input())
dough_price, topping_price = input().split(' ')
dough_kalory = input()
topping_kalories = []
for i in range(topping_count):
    topping_kalories.append(
        int(input())
    )

print(
    solve(
        int(dough_price),
        int(dough_kalory),
        int(topping_price),
        topping_kalories
    )
)

if __name__ == '__main__':
    with open('5545.txt') as f:
        inputs = [
            i.strip() for i in f.readlines()
        ]
        topping_count = inputs.pop(0)
        dough_price, topping_price = str(
            inputs.pop(0)
        ).split(' ')
        dough_kalory = inputs.pop(0)

        print(
            solve(
                int(dough_price),
                int(dough_kalory),
                int(topping_price),
                [
                    int(v) for v in inputs
                ]
            )
        )
