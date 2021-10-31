'''
평면 상에 N개의 점이 찍혀있고, 그 점을 집합 P라고 하자. 

집합 P의 벡터 매칭은 벡터의 집합인데, 

모든 벡터는 집합 P의 한 점에서 시작해서, 

또 다른 점에서 끝나는 벡터의 집합이다. 

또, P에 속하는 모든 점은 한 번씩 쓰여야 한다.

V에 있는 벡터의 개수는 P에 있는 점의 절반이다.

평면 상의 점이 주어졌을 때, 

집합 P의 벡터 매칭에 있는 벡터의 합의 길이의 최솟값을 

출력하는 프로그램을 작성하시오.

'''

import itertools
import copy
import math

if __name__ == '__main__':
    with open('1007.txt') as f:
        inputs = [
            i.strip() for i in f.readlines()
        ]
        test_case_count = int(inputs.pop(0))
        for _ in range(test_case_count):
            dot_count = int(inputs.pop(0))
            dots = list()
            for index in range(dot_count):
                x, y = inputs.pop(0).split(' ')
                dots.append(
                    (int(x), int(y))
                )

            result = 9999999999
            for permutation in itertools.permutations(
                dots,
                len(dots),
            ):
                temp_result = 0
                for index in range(0, len(permutation), 2):
                    x1, y1 = permutation[index]
                    x2, y2 = permutation[index+1]
                    temp_result += math.sqrt(
                        (
                            (x2-x1)**2
                        ) + (
                            (y2-y1)**2
                        )
                    )
                result = min(
                    result,
                    temp_result
                )
            print(result)