def _sort1(a):
    global sr
    global pr
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            sr+=1
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                pr+=1
    print (sr, pr)
    return a

def _sort2(a):
    global sr
    global pr
    for i in range(len(a) - 1):
        sm = i
        for j in range(i + 1, len(a)):
            sr+=1
            if a[j] < a[sm]:
                sm = j
                pr+=1
        a[i], a[sm] = a[sm], a[i]
    print (sr, pr)
    return a

def _sort3(a):
    global sr
    global pr
    for i in range(1, len(a)):
        t = a[i]
        j = i - 1
        sr+=1
        while (j >= 0 and t < a[j]):
            sr+=1
            a[j + 1] = a[j]
            pr+=1
            j = j - 1
        a[j + 1] = t
        
    print (sr, pr)
    return a

def _sort4(a):
    global sr
    global pr
    n = len(a)
    k = int(math.log2(n))
    r = 2**k -1
    while r > 0:
        for i in range(r, n):
            t= a[i]
            j = i
            sr+=1
            while (j >= r) and (a[j - r] > t):
                a[j] = a[j - r]
                j -= r
                pr+=1
                sr+=1
            a[j] = t
            
        k -= 1
        r = 2**k -1
    print (sr, pr)
    return a

def part(a, men, bol):
    global sr
    global pr
    p = a[(men + bol) // 2]
    i = men - 1
    j = bol + 1
    sr, pr = 0, 0
    while True:
        i += 1
        while a[i] < p:
            sr+=1
            i += 1
        j -= 1
        while a[j] > p:
            sr+=1
            j -= 1
        sr+=1
        if i >= j:
            pr+=1
            return j
        a[i], a[j] = a[j], a[i]

def quick_sort(it, men, bol):
    if (men < bol):
        spl = part(it, men, bol)
        quick_sort(it, men, spl)
        quick_sort(it, spl + 1, bol)

def _sort5(a):
    quick_sort(a, 0, len(a) - 1)
    print (sr, pr)

from random import shuffle
import math

n=[10, 100, 1000]
k=int(input())-1

a = [i  for i in range(n[k], 0, -1)] 
print (*a)

sr = 0
pr =0

#r=tuple(a)
#_sort1(a)
#a=list(r)
#_sort2(a)
#a=list(r)
#_sort3(a)
#a=list(r)
#_sort4(a)
#a=list(r)
_sort5(a)
print (*a)

b = [i+1  for i in range(n[k])]
b2=[]
for j in range(n[k]//2):
    b2.append(b[j])
shuffle(b2)
for j in range(n[k]//2):
    b[j]=b2[j]
#print (*b)

#r=tuple(b)
#_sort1(b, sr, pr)
#b=list(r)
#_sort2(b, sr, pr)
#b=list(r)
#_sort3(b, sr, pr)
#b=list(r)
#_sort4(b, sr, pr)
#b=list(r)
#_sort5(b, sr, pr)

c = [i+1  for i in range(n[k])]
#print (*c)

#_sort1(c, sr, pr)
#_sort2(c, sr, pr)
#_sort3(c, sr, pr)
#_sort4(c, sr, pr)
#_sort5(c, sr, pr)