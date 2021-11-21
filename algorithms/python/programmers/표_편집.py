# https://programmers.co.kr/learn/courses/30/lessons/81303

class Command:
    type = None
    number = None

    def __init__(self, command):
        if command[0] in ['Z', 'C']:
            self.type = command
        else:
            command = command.split(' ')
            self.type, self.number = command[0], int(command[1])

    def execute(self, operation):
        if self.type == 'D':
            operation.current_index += self.number
        if self.type == 'U':
            operation.current_index -= self.number
        if self.type == 'C':
            operation.delete()
        if self.type == 'Z':
            operation.undelete()


class Operation:
    commands = []
    data = []
    original_data = []
    current_index = None
    deleted_data = []

    def __init__(self, n, k, commands):
        self.current_index = k
        self.original_data = [
            index
            for index in range(n)
        ]
        self.data = [
            index
            for index in range(n)
        ]

        for command in commands:
            self.commands.append(
                Command(command)
            )

    def run(self):
        for command in self.commands:
            command.execute(self)

    def delete(self):
        deleted_data = self.data.pop(self.current_index)
        self.deleted_data.append(
            (self.current_index, deleted_data)
        )

        if self.current_index == len(self.data):
            self.current_index -= 1

    def undelete(self):
        deleted_index, deleted_data = self.deleted_data.pop()
        self.data.insert(deleted_index, deleted_data)

        if deleted_index <= self.current_index:
            self.current_index += 1

    @property
    def result(self):
        return_data = []
        for datum in self.original_data:
            return_data.append(
                'O' if datum in self.data else 'X'
            )
        return ''.join(return_data)


def solution(n, k, cmd):
    operation = Operation(n, k, cmd)
    operation.run()
    return operation.result
