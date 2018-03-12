import numpy as np

def tf_idf(l1,l):                   #l1 is a document, l is condensed document
    #print (np.sum(l,axis=0))
    #a = np.sum(l,axis=0)
    #print (float(l.shape[0])/np.sum(l>0,axis=0))
    #print (np.log(float(l.shape[0])/np.sum(l>0,axis=0)))
    a = l1
    b = np.log(float(l.shape[0])/np.sum(l>0,axis=0))
    #print ("return with intermidiate veriables", a*b)
    return a*b
    #return (np.sum(l,axis=0) * np.log(l.shape[0]/np.sum(l>0,axis=0)))


l1 = np.array([3,0,5,0,2,6,0,2,0,2]).reshape(10,1).T
l2 = np.array([0,7,0,2,1,0,0,3,0,0]).reshape(10,1).T
l3 = np.array([0,1,0,0,1,2,2,0,3,0]).reshape(10,1).T
l4 = np.concatenate((l1,l2, l3),axis = 0)
res1 = tf_idf(l1, l4)
res2 = tf_idf(l2, l4)
res3 = tf_idf(l3, l4)
print ("res")
print res1.shape
print res2.shape
print res3
print ("cos************************")
#print tf_idf(l4)
#print (l4>0)
#print (np.sum(l4>0,axis=0))
def cosine_similary(l1,l2):
    a = np.dot(l1,l2)
    b = (np.sqrt(np.sum(l1**2)) *np.sqrt(np.sum(l2**2)))
    #print (a.shape)
    #print (b.shape)
    return a/b
print (cosine_similary(res1,res2.T))
print (cosine_similary(res1,res3.T))
print (cosine_similary(res3,res2.T))


