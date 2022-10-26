from temperature import Temperature


class Calorie:
    """Represent number of calories calculated with the
    BMR = 10*weight + 6.25*height - 5*age + 5 - 10*temperature
    """

    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        return 10 * self.weight + 6.26 * self.height + \
                    5 * self.age - 10 * self.temperature


if __name__ == '__main__':
    temperature = Temperature(country='italy', city='rome').get()
    calorie = Calorie(weight=70, height=175, age=32, temperature=temperature)
    print(calorie.calculate())
