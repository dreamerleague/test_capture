# coding: utf-8


import os

def rotate (matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    ##翻转两次，一次上下翻转，一次反对角线翻转
    # global matrix
    print 'id2--->',id(matrix)
    matrix = matrix[::-1]
    # matrix.reverse()
    print 'id3--->',id(matrix)
    print '1--> ',matrix
    n = len(matrix)
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            print '2--> ',i,j,matrix
            print 'id4--->',id(matrix)
    # return matrix
# matrix = [[1,2],[3,4]]
# print 'id1--> ',id(matrix)
# rotate(matrix)

# print 'id5---> ',id(matrix)
# print "3--> ",matrix



def find_min(s):
    numbers = {1:'ONE',2:'TWO',3:'THREE',4:'FOUR',5:'FIVE',6:'SIX',7:'SEVEN',8:'EIGHT',9:'NINE'}
    for number,eng in numbers.items():
        s = s.replace(eng,str(number))
        print s
    # return int(s)
    # return int(s)
    s = sorted(s)
    return int(''.join(s))


s = 'TWOONETHREE'
n = find_min(s)
print n





