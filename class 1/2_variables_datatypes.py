price = 10
type(price)

text_single_quotes = 'The price of zinger burger is:  '
type(text_single_quotes)

text_double_quotes = "The price of zinger burger is:  "
type(text_double_quotes)

# concatenate number and a string and see its type
product_price = text_single_quotes + str(price)
type(product_price)


# concatenate number and a string and see its type
product_name = 'Airpods'
thankyou_message = 'Thank You for purchasing our product: {} {}'.format(product_name, 20)
type(thankyou_message)
print(thankyou_message)


isDiscountCode = True
type(isDiscountCode)


price = '100'
price_num = int(price)
print(type(price))
print(type(price_num))