items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}

wallet = "$300"
# outuput ["Bread", "Fertilizer", "Water"]

def can_afford(wallet:str, items_dict:dict)-> None:
    '''A function that checks in a dict of items and prices
    if can buy. Arguments = wallet, items_dict'''
    can_buy = []

    #cleaning dollar sign
    wallet_clean = wallet.strip('$')
    for product, price in items_dict.items():
        price_clean = price.strip('$').replace(',', '')

        #converting the str to int
        price_clean = int(price_clean)
        wallet_clean = int(wallet_clean)

        #checking what can affort
        if price_clean > wallet_clean:        
            continue
        else:
            can_buy.append(product)
            wallet_clean -= price_clean

        result = f' you can buy: {can_buy} and you have {wallet_clean} dollars in your wallet'

    return result


items_purchase = {
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2"
}

wallet = "$100" 

print(can_afford(wallet, items_purchase))


# # ["Apple", "Bananas", "Fan", "Honey", "Spoon"]

# items_purchase = {
#   "Phone": "$999",
#   "Speakers": "$300",
#   "Laptop": "$5,000",
#   "PC": "$1200"
# }

# wallet = "$1" 
# #nothing


