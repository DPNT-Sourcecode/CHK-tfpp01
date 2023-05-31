

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {'A':50, 'B': 30, 'C':20, 'D':15, 'E':40}
    count = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0}

    for sku in skus:
        if sku not in prices:
            return -1
        count[sku] += 1
    
    chk_val = 0
    for sku, cnt in count.items():
        if sku == 'A':
            grp_5A = cnt // 5
            rem_5A = cnt % 5
            grp_3A = rem_5A // 3
            rem_3A = rem_5A % 3

            chk_val += (200*grp_5A) + (130*grp_3A) + (50*rem_3A)

        elif sku == 'B':
            grp_2B = cnt // 2
            rem_2B = cnt % 2

            chk_val += (45*grp_2B) + (30*rem_2B)
        
        elif sku == 'E':
            grp_2E = cnt // 2

            chk_val += (40*cnt)

        else:
            chk_val += cnt*prices[sku]

    return chk_val

    
    # total = 0
    # cnt_A = 0
    # cnt_B = 0

    # for sku in skus:
        
    #     if sku not in 'ABCD':
    #         return -1

    #     elif sku == 'A':
    #         cnt_A += 1

    #     elif sku == 'B':
    #         cnt_B += 1
        
    #     elif sku == 'C':
    #         total += 20

    #     elif sku == 'D':
    #         total += 15

    # # Get groups of multipack and remainder
    # grp_A = cnt_A // 3
    # rem_A = cnt_A % 3

    # grp_B = cnt_B // 2
    # rem_B = cnt_B % 2

    # total += (grp_A*130) + (rem_A*50) + (grp_B*45) + (rem_B*30)

    # return total


