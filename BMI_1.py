def validation(type):
    is_valid_input = False

    while not is_valid_input:
        result = input(f'Enter your {type}: ')
        try:
            result = float(result)
            if result > 0:
                print(result)
                is_valid_input = True
            else:
                print(f'Your {type} cannot be less or equal 0')
        except ValueError:
            print('You entered not number or you left empty field, try again')
    return result

def print_bmi(weight, height, age):
    max_height = 2.8

    if height > max_height:
        height = height / 100
    ind = round(weight / height ** 2, 2)
    if ind <= 16:
        bmi = 'Выраженный дефицит массы тела'
    elif ind > 16 and ind <= 18.5:
        bmi = 'Недостаточная (дефицит) масса тела'
    elif ind > 18.5 and ind <= 25:
        bmi = 'Норма'
    elif ind > 25 and ind <= 30:
        bmi = 'Избыточная масса тела (предожирение)'
    elif ind > 30 and ind <= 35:
        bmi = 'Ожирение первой степени'
    elif ind > 35 and ind <= 40:
        bmi = 'Ожирение второй степени'
    else:
        bmi = 'Ожирение третьей степени (морбидное)'
    if age >= 0 and age <= 1:
        old = 'Младенец'
    elif age > 1 and age <= 10:
        old = 'Ребенок'
    elif age > 10 and age <= 18:
        old = 'Подросток'
    elif age > 18 and age <= 60:
        old = 'Взрослый'
    else:
        old = 'Пожилой'

    print(ind)
    print(bmi)
    print(old)

weight = validation('weight')
height = validation('height')
age = validation('age')

print_bmi(weight, height, age)


### 


class Class_Bmi:

    def __init__(self):
        self.weight = self.validation('weight')
        self.height = self.validation('height')
        self.age = self.validation('age')

    def validation(self, type):
        is_valid_input = False
        while not is_valid_input:
            result = input(f'Enter your {type}: ')
            try:
                result = float(result)
                if result > 0:
                    is_valid_input = True
                else:
                    print(f'Your {type} cannot be less or equal 0')
            except ValueError:
                print('You entered not number or you left empty field, try again')
        return result

    def print_bmi(self):
        max_height = 2.8

        if self.height > max_height:
            self.height = self.height / 100
        ind = round(self.weight / self.height ** 2, 2)
        if ind <= 16:
            bmi = 'Выраженный дефицит массы тела'
        elif ind > 16 and ind <= 18.5:
            bmi = 'Недостаточная (дефицит) масса тела'
        elif ind > 18.5 and ind <= 25:
            bmi = 'Норма'
        elif ind > 25 and ind <= 30:
            bmi = 'Избыточная масса тела (предожирение)'
        elif ind > 30 and ind <= 35:
            bmi = 'Ожирение первой степени'
        elif ind > 35 and ind <= 40:
            bmi = 'Ожирение второй степени'
        else:
            bmi = 'Ожирение третьей степени (морбидное)'
        if self.age >= 0 and self.age <= 1:
            old = 'Младенец'
        elif self.age > 1 and self.age <= 10:
            old = 'Ребенок'
        elif self.age > 10 and self.age <= 18:
            old = 'Подросток'
        elif self.age > 18 and self.age <= 60:
            old = 'Взрослый'
        else:
            old = 'Пожилой'

        print(ind)
        print(bmi)
        print(old)

p1 = Class_Bmi()
p1.print_bmi()

p2 = Class_Bmi()
p2.print_bmi()



