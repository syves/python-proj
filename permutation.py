#!/usr/bin/python

#A non-empty array A consisting of N integers is given.

#A permutation is a sequence containing each element from 1 to N #once, and only once.

#def solution(nums):
#    if sorted(nums) == range(1, len(nums) + 1):
#        return 1
#    else:
#        return -1

def solution(nums):
    perm = 1
    for n in range(1, len(nums) + 1):
        if n not in set(nums):
            perm = -1
            return perm
    return perm

#alrernative? if we have a large collection does sort become worse? can we escape early if we do not find the num we are looking for?

#assert(solution([]) == -1) = 1
print("\n")
assert(solution([4,1,3,2]) == 1)
print("\n")
assert(solution([4, 1, 3]) == -1)
print("\n")
assert(solution([4, 1, 3, 3, 2]) == -1)
print("\n")
assert(solution([4, 3, 3, 2]) == -1)
print("\n")
