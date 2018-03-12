import numpy as np

def dot_product(l1, l2):
    sum_dp = 0
    for i in range(len(l1)):
        sum_dp += l1[i] * l2[i]
    return sum_dp

def length(l1):
    sum_l = 0
    for i in l1:
        sum_l += i**2
    return sum_l ** 0.5


def cosine_similary(l1,l2):
    #print (np.dot(l1,l2)) 
    a = np.dot(l1,l2)
    b = (np.sqrt(np.sum(l1**2)) *np.sqrt(np.sum(l2**2)))
    return a/b
    #return np.dot(l1,l2)/(np.sum(l1**2) *np.sum(l2**2))
    #for i in range(len(l1)):

l1 = np.array([3,0,5,0,2,6,0,2,0,2])
l2 = np.array([0,7,0,2,1,0,0,3,0,0])
l3 = np.array([0,1,0,0,1,2,2,0,3,0])

print (cosine_similary(l1,l2))
print (cosine_similary(l1,l3))
print (cosine_similary(l3,l2))


