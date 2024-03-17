# savarjisho 1

# female_passenger = 0
# with open("titanic.txt", "r")as file:
#     for each in file:
#         data = each.strip().split(',')
#         if Sex == "female":
#             female_passenger += 1
# print(female_passenger)
        # if Sex in file == female:
        #     female_passenger += 1
        #     print(female_passenger)





































# savarjisho 2
class Ticket:
    def __init__(self, film_name, ticket_price, sum_of_tickets, language="Geo"):
        self.film_name = film_name
        self.ticket_price = ticket_price
        self.sum_of_tickets = sum_of_tickets
        self.language = language



    def __str__(self):
        return f"Name: {self.film_name}, Ticket_Price: {self.ticket_price}, Sum_of_Tickets: {self.sum_of_tickets} "


ticket = Ticket("zangebi", 15, 100)
print(ticket)


class User(Ticket):
    def __init__(self, user_name, money_balance):
        self.user_name = user_name
        self.money_balance = money_balance

    def __str__(self):
        return f"User_Name: {self.user_name}, Money_Balance: {self.money_balance}"

    def deposit(self, tanxis_shetana):
        self.money_balance += tanxis_shetana
        print(f"dadepositebuli tanxa: {tanxis_shetana}, ganaxlebuli balance: {self.money_balance}")

    def __eq__(self, other):
        return self.sum_of_tickets == other.sum_of_tickets
    def __lt__(self, other):
        return self.sum_of_tickets < other.sum_of_tickets


user1 = User("gela", 1.5)
user1.deposit(2)
print(user1)
