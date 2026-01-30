customer_name = 'Henry'
drink = 'Fresh Lime'
main_course = 'Broasted Burger'
desert = 'Choco Lava Ice Cake'

# Basic if else
if ((main_course == 'Broasted Burger') and (desert == 'Choco Lava Ice Cake')) or (drink == 'Mint Lemonade'):
    print('Your Order is being prepared!')
else:
    print('Your order cannot be processed')


# Multiple ifs
if ((main_course == 'Broasted Burger') and (desert == 'Choco Lava Ice Cake')) or (drink == 'Mint Lemonade'):
    print('Your Order is being prepared!')

if customer_name.startswith('H'):
    print('15% Discount Applicable')



# Multiple ifs
if ((main_course == 'Broasted Burger') and (desert == 'Choco Lava Ice Cake')) or (drink == 'Mint Lemonade'):
    print('Your Order is being prepared!')

elif ((main_course == 'Broasted Burger') or (desert == 'Choco Lava Ice Cake')) or (drink == 'Mint Lemonade'):
    print('You can order more foods from our menu')

else:
    print('Your order cannot be processed')


# Nested ifs
hasNadraInitialSlip = True
hasDocuments = True

if hasNadraInitialSlip:
    if hasDocuments:
        print('Proceed with the application')