# import os

# print(os.listdir())

# print('hello!')

# print (''' in order to print a multiline
# statements in print stmt we have to use \''' ''')

# for i in range(1,11):
#     #print('5 * ', i,'= {}'.format(5*i) )
#     print('5 *',i,'=',(5*i))

# from audioop import avg
# from math import sqrt


# a = int(input("Enter first numbers :"))
# b = int(input("Enter second numbers :"))
# print((a+b)/2)

# print(a*a)


from collections import Counter






def seqstring (s):
    freq = Counter(s)
    for i in s:
        if freq[i] == 1:
            return s.index(i)
    return -1

s = input("Enter the string : ")
print(seqstring(s))
print("Hi")

