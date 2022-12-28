def Reverse(n):
    str=""
    for i in n:
        str=i+str
    return str

print(Reverse("saaho"))
def IsPalindrome(n):
    newStr=""
    for i in n:
        if i.isalnum():
            newStr+=i.lower()
    if(newStr==newStr[::-1]):
        print("true")
    else:
        print("fsld")

IsPalindrome(" bil s aa sli")


