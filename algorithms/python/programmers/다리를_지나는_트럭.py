# https://programmers.co.kr/learn/courses/30/lessons/42583

class Bridge:
    bridge_length = None
    durable_weight = None
    queue = []
    total_weight = False
    _tick = 0

    def __init__(self, bridge_length, durable_weight):
        self.bridge_length = bridge_length
        self.durable_weight = durable_weight

    def enqueue(self, weight):
        if weight + self.total_weight > self.durable_weight:
            return False

        self.queue.append({
            'id': len(self.queue),
            'weight': weight,
            'time_on_bridge': 0,
        })
        self.total_weight += weight
        return True

    def dequeue(self):
        truck = self.queue.pop(0)
        self.total_weight -= truck['weight']

    def tick(self):
        self._tick += 1

        for truck in self.queue[::1]:
            truck['time_on_bridge'] += 1
            if truck['time_on_bridge'] >= self.bridge_length:
                self.dequeue()


def solution(bridge_length, weight, truck_weights):
    bridge = Bridge(bridge_length, weight)

    while bridge._tick == 0 or bridge.queue:
        bridge.tick()
        if truck_weights:
            truck = truck_weights[0]
            if bridge.enqueue(truck):
                truck_weights.pop(0)
    return bridge._tick
