class Cat:
    xвост = True

    def may(self):
        print(self.name, 'мяукает')

    def init(self, name, age):
        self.name = name
        self.age = age

    def str(self):
        return f'name is {self.name}\n' \
               f'age is {self.age}'

    def len(self):
        return len(self.name)

    def x2(self):
        self.age *= 9
        print(self)