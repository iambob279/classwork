from collections import namedtuple

Person = namedtuple("Person", "firstname lastname age")

prime_minister = Person("Boris", "Johnson", 57)

print(f"The prime minister's first name is {prime_minister.firstname}")
print(f"Prime minister's last name is {prime_minister.lastname}")
print(f"Prime minister's age is {prime_minister.age}")
print(prime_minister[0])