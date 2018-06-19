#!/usr/bin/python

def solution(nums):
    numset = set(nums)
    counter = 1

    while True :
        if counter not in numset :
            return counter
        counter += 1

assert(solution([]) == 1)
print("\n")
assert(solution([1,2,4]) == 3)
print("\n")
assert(solution([-2,-1,2,4]) == 1)
print("\n")
assert(solution([-2,-1,1,2,4]) == 3)
print("\n")
assert(solution([-2,1,1,2,4]) == 3)
print("\n")
assert(solution([2,3,4,1]) == 5)
