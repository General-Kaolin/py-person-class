class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}

    [Person(pers["name"], pers["age"]) for pers in people]

    for pers in people:
        person_instance = Person.people[pers["name"]]

        wife_name = pers.get("wife")
        if wife_name:
            person_instance.wife = Person.people[wife_name]

        husband_name = pers.get("husband")
        if husband_name:
            person_instance.husband = Person.people[husband_name]

    return [Person.people[pers["name"]] for pers in people]
