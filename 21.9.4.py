class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'Client:{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб.'
    def get_guests(self):
        return f'Client:{self.name} {self.surname}. {self.city}'

client_1 = Client('Иван', 'Петров', 'Москва', 50)
client_2 = Client('Макар', 'Селезнев', 'Волгоград', 100)
client_3 = Client('Станислав', 'Арбузов', 'Нижний Новгород', 160)

guest_list=[client_1, client_2, client_3]

for guest in guest_list:
    print(guest.get_guests())
