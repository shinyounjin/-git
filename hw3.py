def get_fixed_price(discount_rate, discounted_price):
    original_price = discounted_price / (1 - discount_rate / 100)
    return int(original_price)

def main():
    discount_rate = float(input('할인율은? '))
    
    a_discounted = float(input('A 상품의 할인된가격은? '))
    b_discounted = float(input('B 상품의 할인된가격은? '))
    
    a_fixed_price = get_fixed_price(discount_rate, a_discounted)
    b_fixed_price = get_fixed_price(discount_rate, b_discounted)

    print('A 상품의 정가는')
    print('B 상품의 정가는')

if __name__ == '__main__':
    main()
