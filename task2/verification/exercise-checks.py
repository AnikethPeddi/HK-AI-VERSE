# Checks run on 24 Oct 2026 for the AI-use record (exercises 1, 2 and 5). Needs Python 3 and NumPy.
import numpy as np
from collections import Counter
# 1. NLP add-one
sents=[["<s>","the","cat","sat","</s>"],["<s>","the","cat","ate","</s>"],["<s>","a","dog","sat","</s>"]]
uni=Counter(w for s in sents for w in s[:-1]); bi=Counter((s[i],s[i+1]) for s in sents for i in range(len(s)-1))
V=len({w for s in sents for w in s if w!="<s>"})
print("V",V,"c(cat)",uni["cat"],"c(cat sat)",bi[("cat","sat")],"P",(bi[("cat","sat")]+1)/(uni["cat"]+V))
print("MLE",bi[("cat","sat")]/uni["cat"])
# 2. DL gradient check, 2-layer MLP, BCE with sigmoid output
rng=np.random.default_rng(0); X=rng.normal(size=(5,3)); y=np.array([0,1,1,0,1.])
W1=rng.normal(size=(3,4))*.5;b1=np.zeros(4);W2=rng.normal(size=(4,1))*.5;b2=np.zeros(1)
sig=lambda z:1/(1+np.exp(-z))
def loss(W1,b1,W2,b2):
    h=np.tanh(X@W1+b1);p=sig(h@W2+b2).ravel()
    return -np.mean(y*np.log(p)+(1-y)*np.log(1-p))
def grads(W1,b1,W2,b2):
    h=np.tanh(X@W1+b1);z=h@W2+b2;p=sig(z).ravel()
    dz=((p-y)/len(y))[:,None]           # dL/dz = (sigma(z)-y)/N
    dW2=h.T@dz;db2=dz.sum(0);dh=dz@W2.T;da=dh*(1-h**2)
    return X.T@da,da.sum(0),dW2,db2
g=grads(W1,b1,W2,b2);P=[W1,b1,W2,b2];mx=0
for k in range(4):
    num=np.zeros_like(P[k]);it=np.nditer(P[k],flags=["multi_index"])
    for _ in it:
        i=it.multi_index;o=P[k][i];P[k][i]=o+1e-6;a=loss(*P);P[k][i]=o-1e-6;b=loss(*P);P[k][i]=o;num[i]=(a-b)/2e-6
    mx=max(mx,np.abs(num-g[k]).max())
print("max abs diff analytic vs numeric",mx)
l0=loss(*P);lr=.5
W1,b1,W2,b2=[p-lr*gg for p,gg in zip(P,g)];print("loss before",l0,"after one step",loss(W1,b1,W2,b2))
# 5. break-even
FC,price,vc=120000,200,40
print("break-even users",FC/(price-vc),"revenue",FC/(price-vc)*price)
