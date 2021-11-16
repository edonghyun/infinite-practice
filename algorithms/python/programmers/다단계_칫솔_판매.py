# https://programmers.co.kr/learn/courses/30/lessons/77486

class Node:
    name = None
    parent = None
    profit = 0

    def __init__(self, id, name):
        self.id = id
        self.name = name


def solution(enroll, referral, seller, amount):
    nodes = {
        '-': Node(-1, '-')
    }

    for id, name in enumerate(enroll):
        node = Node(id, name)
        nodes[name] = node
        ref = referral[id]
        reffered_node = nodes[ref]
        node.parent = reffered_node

    for index, seller_name in enumerate(seller):
        profit = amount[index] * 100
        node = nodes[seller_name]

        while True:
            if not node.parent:
                node.profit += profit
                break

            profit_to_give = int(profit * 0.1)
            profit_to_have = profit - profit_to_give
            if profit_to_give == 0:
                node.profit += profit
                break

            node.profit += profit_to_have

            node = node.parent
            profit = profit_to_give

    return [
        node.profit
        for index, (name, node)
        in enumerate(nodes.items())
        if index != 0
    ]
