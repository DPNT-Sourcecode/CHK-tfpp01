
from collections import defaultdict
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {
        'A':50, 
        'B':30, 
        'C':20, 
        'D':15, 
        'E':40, 
        'F':10, 
        'G':20, 
        'H':10, 
        'I':35, 
        'J':60, 
        'K':70,
        'L':90,
        'M':15,
        'N':40,
        'O':10,
        'P':50,
        'Q':30,
        'R':50,
        'S':20,
        'T':20,
        'U':40,
        'V':50,
        'W':20,
        'X':17,
        'Y':20,
        'Z':21
        }

    # Single special prices
    special_prices = {
        'B':45,
        'K':120,
        'P':200,
        'Q':80,
        'A':200,
        'H':80,
        'V':130
    }

    special_prices_2 = {
        'A':130,
        'H':45,
        'V':90
    }

    # Quanitity needed to be eligible for promotion
    promo_quant = {
        'F':3,
        'U':4,
        'B':2,
        'K':2,
        'P':5,
        'Q':3,
        'E':2,
        'N':3,
        'R':3,
        'A':5,
        'H':10,
        'V':3
    }

    promo_quant_2 = {
        'A':3,
        'H':5,
        'V':2
    }

    # mapping for X item A -> free itemB
    other = {
        'E':'B',
        'N':'M',
        'R':'Q'
    }
    
    count = {chr(i):0 for i in range(ord('A'), ord('Z')+1)}

    for sku in skus:
        if sku not in prices:
            return -1
        count[sku] += 1
    
    chk_val = 0

    # Promo for X item A -> free item B
    for sku, cnt in count.items():
        if sku == 'E' or sku == 'N' or sku == 'R':
            grp = cnt // promo_quant[sku]
            if count[other[sku]] <= grp:
                count[other[sku]] = 0
            else:
                count[other[sku]] -= grp   
    
    # Count total STXYZ 
    total_cnt = 0
    for sku in 'ZYSTX':
        total_cnt += count[sku]

    grp_cnt = 0
    # number of group of 3 we can make from STXYZ
    grp3 = total_cnt // 3
    for sku in 'ZYSTX':
        while count[sku] > 0 and grp3 > 0:
            count[sku] -= 1
            grp_cnt += 1

            if grp_cnt == 3:
                chk_val += 45
                grp_cnt = 0
                grp3 -= 1

    for sku, cnt in count.items():
        if sku == 'A' or sku == 'H' or sku == 'V':
            grp1 = cnt // promo_quant[sku]
            rem1 = cnt % promo_quant[sku]
            grp2 = rem1 // promo_quant_2[sku]
            rem2 = rem1 % promo_quant_2[sku]
            chk_val += (special_prices[sku]*grp1) + (special_prices_2[sku]*grp2) + (prices[sku]*rem2)

        # Promo for special price for X item A
        elif sku == 'B' or sku == 'K' or sku == 'P' or sku == 'Q':
            grp = cnt // promo_quant[sku]
            rem = cnt % promo_quant[sku]
            
            chk_val += (special_prices[sku]*grp) + (prices[sku]*rem)

        # Promo for X item A -> free item A
        elif sku == 'F' or sku == 'U':
            grp = cnt // promo_quant[sku]

            chk_val += prices[sku]*(cnt-grp)

        else:
            chk_val += cnt*prices[sku]

    return chk_val


