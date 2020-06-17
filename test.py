from random import choice


class Person:

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f'Hello, im {self.name}'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name


def test() -> int:
    return 20


def main():
    people = [
        Person('Pier'),
        Person('Lacazet'),
        Person('Pepe'),
        Person('Lucas')
    ]

    person = choice(people)
    print(person)
    print(person.name)
    person.name = 'new'
    print(person)
    del person.name
    print(person)


if __name__ == '__main__':
    main()
