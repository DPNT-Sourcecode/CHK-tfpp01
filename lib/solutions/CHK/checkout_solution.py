

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total = 0
    cnt_A = 0
    cnt_B = 0

    for sku in skus:
        
        if sku not in 'ABCD':
            return -1

        elif sku == 'A':
            cnt_A += 1

        elif sku == 'B':
            cnt_B += 1
        
        elif sku == 'C':
            total += 20

        elif sku == 'D':
            total += 15

    # Get groups of multipack and remainder
    grp_A = cnt_A // 3
    rem_A = cnt_A % 3

    grp_B = cnt_B // 2
    rem_B = cnt_B % 2

    total += (grp_A*130) + (rem_A*50) + (grp_B*45) + (rem_B*30)

    return total


