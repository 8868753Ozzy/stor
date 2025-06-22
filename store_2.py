# Класс Товар (Product)
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price} руб."

    



# Класс Скидка (Discount)
class Discount:
    def __init__(self, description, discount_percent):
        self.description = description
        self.discount_percent = discount_percent

    @staticmethod
    def apply_discount(price, discount_percent):
        return price * (1 - discount_percent / 100)

    @staticmethod
    def seasonal_discount(price):
        return Discount.apply_discount(price, 10)  # 10% сезонная скидка

    @staticmethod
    def promo_code_discount(price, code):
        promo_codes = {
            "PROMO10": 10,
            "PROMO20": 20,
            "VIP": 30
        }
        return Discount.apply_discount(price, promo_codes.get(code, 0))

    def __str__(self):
        return f"{self.description} ({self.discount_percent}%)"

    


# Класс Заказ (Order)
class Order:
    all_orders = []

    def __init__(self, products):
        self.products = products
        Order.all_orders.append(self)

    def total_price(self):
        return sum(product.price for product in self.products)

    def apply_discount(self, discount):
        return Discount.apply_discount(self.total_price(), discount.discount_percent)

    @classmethod
    def total_orders_count(cls):
        return len(cls.all_orders)

    @classmethod
    def total_orders_sum(cls):
        return sum(order.total_price() for order in cls.all_orders)

    def __str__(self):
        product_list = ', '.join(p.name for p in self.products)
        return f"Заказ: {product_list} | Сумма: {self.total_price()} руб."

    


# Класс Клиент (Customer)
class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def __str__(self):
        return f"Клиент: {self.name}, Кол-во заказов: {len(self.orders)}"

  
    # Создаем товары
p1 = Product("Ноутбук", 50000)
p2 = Product("Смартфон", 30000)
p3 = Product("Наушники", 5000)

# Создаем клиентов
c1 = Customer("Анна")
c2 = Customer("Иван")

# Создаем заказы
order1 = Order([p1, p3])
order2 = Order([p2])
order3 = Order([p2, p3])

# Добавляем заказы клиентам
c1.add_order(order1)
c1.add_order(order2)
c2.add_order(order3)

# Применяем скидку
discount = Discount("Сезонная скидка", 10)
print(f"\nПрименение скидки к заказу 1: {order1.apply_discount(discount)} руб.")

# Применение скидки по промокоду
print(f"Скидка по промокоду 'VIP' к заказу 3: {Discount.promo_code_discount(order3.total_price(), 'VIP')} руб.")

# Статистика заказов
print(f"\nОбщее количество заказов: {Order.total_orders_count()}")
print(f"Общая сумма заказов: {Order.total_orders_sum()} руб.\n")

# Информация о клиентах и заказах
for customer in [c1, c2]:
    print(customer)
    for order in customer.orders:
        print(f"  {order}")

