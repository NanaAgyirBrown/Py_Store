import csv


class Item:
    discount_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validation
        assert price >= 0, f"Price {price} must be greater or equal to zero(0)!"
        assert quantity >= 0, f"Quantity {quantity} must be greater or equal to zero(0)"

        self.__name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    # Property Decorator = Read-Only Attribute
    def name(self):
        return self.__name

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.discount_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('store.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price} , {self.quantity})"
