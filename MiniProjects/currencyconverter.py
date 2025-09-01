# Currency Converter: Pkr-Dollar-Euro

def cur_converter(my_curr):
    amount = int(input("Enter amount:"))
    curr = input("Change currency into:") 
    if my_curr == "Pkr":
        if curr == "Eur":
            return amount * 350
        elif curr == "Usd":
            return amount * 280        
    elif my_curr == "Eur":
        if curr == "Pkr":
            return amount / 350
        elif curr == "Usd":
            return amount / 0.8
    elif my_curr == "Usd":
        if curr == "Pkr":
            return amount / 270
        elif curr == "Eur":
            return amount * 1.2
    else:
        return "Error!"


print(cur_converter("Pkr"))                 
