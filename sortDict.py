from functools import cmp_to_key
def compare(a, b):
    if a[0]!=b[0]:
        if a[0]>b[0]:
            return -1
        else:
            return 1     
    else:
        if a[1]<b[1]:
            return 1
        else:
            return -1   

d={'a':3,'b':5,'c':6,'d':5}
dt = [(d[i],i) for i in d]
print(dt)
sorted_dt = sorted(dt, key=cmp_to_key(compare), reverse=False)
print(sorted_dt)
sorted_by_tel = sorted(dt, key=lambda x:x[1],reverse=False)
print(sorted_by_tel)