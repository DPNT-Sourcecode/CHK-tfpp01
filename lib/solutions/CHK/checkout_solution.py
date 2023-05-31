

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {'A':50, 'B': 30, 'C':20, 'D':15, 'E':40, 'F':10 }
    count = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0}

    for sku in skus:
        if sku not in prices:
            return -1
        count[sku] += 1
    
    chk_val = 0

    grp_2E = count['E'] // 2
    if count['B'] <= grp_2E:
        count['B'] = 0
    elif count['B'] > grp_2E:
        count['B'] -= grp_2E
    

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
        
        elif sku == 'F':
            grp_2F = cnt // 3

            chk_val += 10*(cnt-grp_2F)

        else:
            chk_val += cnt*prices[sku]

    return chk_val

