def _sort1(a): #метод пузырька
    global sr
    global pr
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            sr+=1
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                pr+=1
    return a


def _sort2(a): #метод выбором
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
    return a


def _sort3(a): #метод вставок
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
    return a


def _sort4(a): #метод Шелла
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
    return a


def part(a, men, bol): #вспомогательная функция для быстрой сортировки
    global sr
    global pr
    p = a[(men + bol) // 2]
    i = men - 1
    j = bol + 1
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

def quick_sort(it, men, bol): #вспомогательная функция для быстрой сортировки
    if (men < bol):
        spl = part(it, men, bol)
        quick_sort(it, men, spl)
        quick_sort (it, spl + 1, bol)

def _sort5(a): #метод быстрой сортировки
    quick_sort(a, 0, len(a) - 1)


from random import shuffle
import math

n=[10, 100, 1000]
k=int(input('Сколько элементов в списке? Если 10 эл. введите 1, 100 - 2, 1000 - 3 '))-1

a = [i  for i in range(n[k], 0, -1)] #полностью не отсортированный список
#print (*a)


r=tuple(a)
sr, pr = 0, 0

print ('Полностью не отсортированный список')
_sort1(a)
print ('Метод пузырька: сравнений: ', sr, ' перестановок: ', pr)
a=list(r)
sr, pr = 0, 0
_sort2(a)
print ('Метод выбором: сравнений: ', sr, ' перестановок: ', pr)
a=list(r)
sr, pr = 0, 0
_sort3(a)
print ('Метод вставок: сравнений: ', sr, ' перестановок: ', pr)
a=list(r)
sr, pr = 0, 0
_sort4(a)
print ('Метод Шелла: сравнений: ', sr, ' перестановок: ', pr)
a=list(r)
sr, pr = 0, 0
_sort5(a)
print ('Метод быстрой сортировки: сравнений: ', sr, ' перестановок: ', pr)
print ()


b = [i+1  for i in range(n[k])] #частично отсортированный список
b2=[]
for j in range(n[k]//2):
    b2.append(b[j])
shuffle(b2)
for j in range(n[k]//2):
    b[j]=b2[j]
#print (*b)

r=tuple(b)

print ('Частично отсортированный список')
_sort1(b)
print ('Метод пузырька: сравнений: ', sr, ' перестановок: ', pr)
b=list(r)
sr, pr = 0, 0
_sort2(b)
print ('Метод выбором: сравнений: ', sr, ' перестановок: ', pr)
b=list(r)
sr, pr = 0, 0
_sort3(b)
print ('Метод вставок: сравнений: ', sr, ' перестановок: ', pr)
b=list(r)
sr, pr = 0, 0
_sort4(b)
print ('Метод Шелла: сравнений: ', sr, ' перестановок: ', pr)
b=list(r)
sr, pr = 0, 0
_sort5(b)
print ('Метод быстрой сортировки: сравнений: ', sr, ' перестановок: ', pr)
print ()

c = [i+1  for i in range(n[k])] #полностью отсортированный список
#print (*c)
print ('Полностью отсортированный список')
_sort1(c)
print ('Метод пузырька: сравнений: ', sr, ' перестановок: ', pr)
sr, pr = 0, 0
_sort2(c)
print ('Метод выбором: сравнений: ', sr, ' перестановок: ', pr)
sr, pr = 0, 0
_sort3(c)
print ('Метод вставок: сравнений: ', sr, ' перестановок: ', pr)
sr, pr = 0, 0
_sort4(c)
print ('Метод Шелла: сравнений: ', sr, ' перестановок: ', pr)
sr, pr = 0, 0
_sort5(c)
print ('Метод быстрой сортировки: сравнений: ', sr, ' перестановок: ', pr)
