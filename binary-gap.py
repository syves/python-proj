#!/usr/bin/python

#A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

#For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

#returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.
def solution(n):
    ints = map(int, format(n, "b"))
    #print("ints :"+ ''.join(str(e) for e in ints))
    maxgap = 0

    occurs = [i for i,val in enumerate(ints) if val==1]
    #print("occurs : " + ''.join(str(e) for e in occurs))
    #[0, 6, 10]
    if len(occurs) < 2:
        print("no occur")
        return 0
    else:
        for n in occurs:
            while n < len(occurs) -1:
                #print("n :" + str(n))
                bingap = abs(occurs[n] - occurs[n +1]) -1
                #print("bingap" + str(bingap))
                if maxgap < bingap:
                    maxgap = bingap
                n += 1
    return maxgap

#max(map(len,format(0, 'b').rstrip('0').split('1')))

assert(solution(32) == 0)
print("\n")
#print(solution(1041))
assert(solution(1041) == 5)
print("\n")
