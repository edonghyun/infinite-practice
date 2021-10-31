# -*-coding:utf-8-*-

'''
https://www.acmicpc.net/problem/5582

두 문자열이 주어졌을 때, 두 문자열에 모두 포함된 가장 긴 공통 부분 문자열을 찾는 프로그램을 작성하시오.

어떤 문자열 s의 부분 문자열 t란, s에 t가 연속으로 나타나는 것을 말한다. 

예를 들어, 문자열 ABRACADABRA의 부분 문자열은 ABRA, RAC, D, ACADABRA, ABRACADABRA, 빈 문자열 등이다.

하지만, ABRC, RAA, BA, K는 부분 문자열이 아니다.

두 문자열 ABRACADABRA와 ECADADABRBCRDARA의 공통 부분 문자열은 CA, CADA, ADABR, 빈 문자열 등이 있다. 

이 중에서 가장 긴 공통 부분 문자열은 ADABR이며, 길이는 5이다. 

또, 두 문자열이 UPWJCIRUCAXIIRGL와 SBQNYBSBZDFNEV인 경우에는 가장 긴 공통 부분 문자열은 빈 문자열이다.

첫째 줄과 둘째 줄에 문자열이 주어진다. 문자열은 대문자로 구성되어 있으며, 길이는 1 이상 4000 이하이다.

첫째 줄에 두 문자열에 모두 포함 된 부분 문자열 중 가장 긴 것의 길이를 출력한다.

'''


import collections


def solve():
    return


if __name__ == '__main__':
    # with open('5582.txt') as f:
    #     inputs = [
    #         i.strip() for i in f.readlines()
    #     ]
    #     string_1 = inputs.pop(0)
    #     string_2 = inputs.pop(0)

    #     longer = string_1 if len(string_1) > len(string_2) else string_2
    #     shorter = string_1 if len(string_2) >= len(string_1) else string_2

    #     max_length = 0
    #     shorter_length = len(shorter)
    #     found = False
    #     for length in range(shorter_length, 0, -1):
    #         if found:
    #             break
    #         for start_index in range(0, shorter_length - length):
    #             if found:
    #                 break
    #             string = ''
    #             for delta in range(length):
    #                 string += shorter[start_index + delta]
    #             if string in longer:
    #                 print(len(string))
    #                 found = True
    #     if not found:
    #         print(0)
