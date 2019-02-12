# LARGEST PALINDROME PRODUCT - 5%
def is_pal(num):
    num = str(num)
    for i in range(int(len(num))):
        if num[i] != num[-(i+1)]:
            return False
    return True

def max_pal():
    pal_list = []
    for i in range(999,0,-1):
        for j in range(999,0,-1):
            if is_pal(i*j):
                pal_list.append(i*j)
                break
    return max(pal_list)

max_pal()