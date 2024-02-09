class Employee:
    vacation_days = 28

    def __init__(
            self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = self.vacation_days
        # Сюда добавьте новый атрибут remaining_vacation_days

    # Сюда добавьте методы consume_vacation и get_vacation_details.
    def consume_vacation(self, days_spent: int):
        self.days_spent = days_spent
        self.remaining_vacation_days -= self.days_spent

    def get_vacation_details(self):
        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'


employee = Employee(first_name='Роберт', second_name='Крузо', gender='м')


employee.consume_vacation(7)
print(employee.get_vacation_details())
