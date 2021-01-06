ranlis = ['1','2','3','9','23','43','53','63','73','83','93','43','23','33','43']


def chop(arr):
    del arr[0]
    del arr[-1]

def middle(arr):
    newarr = arr[1:-1]
    return newarr
   
choparr = chop(ranlis)   
newran = middle(ranlis)
print(choparr)
print(newran)