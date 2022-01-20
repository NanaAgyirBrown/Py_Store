from StoreClass import Item
from phone import Phone

Item.instantiate_from_csv()

phone1 = Phone("Nokia", 46.45, 4500, 10)


print(Item.all)
print(Phone.all)

print(phone1.calculate_total_price())
