
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
        'K':80,
        'L':90,
        'M':15,
        'N':40,
        'O':10,
        'P':50,
        'Q':30,
        'R':50,
        'S':30,
        'T':20,
        'U':40,
        'V':50,
        'W':20,
        'X':90,
        'Y':10,
        'Z':50
        }

    # Single special prices
    special_prices = {
        'B':45,
        'K':150,
        'P':200,
        'Q':80,
        'A':200,
        'H':80,
        'V':130
    }

    # Quanitity needed to be eligible for promotion
    promo_quant = {
        'F':2,
        'U':3,
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


    count = defaultdict(int)

    for sku in skus:
        if sku not in prices:
            return -1
        count[sku] = 1 + count.get(sku, 0)
    
    chk_val = 0

    # mapping for X item A -> free itemB
    other = {
        'E':'B',
        'N':'M',
        'R':'Q'
    }

    # Promo for X item A -> free item B
    for sku, cnt in count.items():
        if sku == 'E' or sku == 'N' or sku == 'R':
            grp = cnt // promo_quant[sku]
            if count[other[sku]] <= grp:
                count[other[sku]] = 0
            else:
                count[other[sku]] -= grp   


    for sku, cnt in count.items():
        if sku == 'A':
            grp_5A = cnt // 5
            rem_5A = cnt % 5
            grp_3A = rem_5A // 3
            rem_3A = rem_5A % 3

            chk_val += (200*grp_5A) + (130*grp_3A) + (prices[sku]*rem_3A)

        elif sku == 'H':
            grp_10H = cnt // 10
            rem_10H = cnt % 10
            grp_5H = rem_10H // 5
            rem_5H = rem_10H // 5

            chk_val += (80*grp_10H) + (45*grp_5H) + (prices[sku]*rem_5H)

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


