def build_person(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


name = build_person("Arshad", "Maher", age=25)

print(name)
