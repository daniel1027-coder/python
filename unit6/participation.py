
pet1 = {
    "type": "dog",
    "owner": "Alice"
}

pet2 = {
    "type": "cat",
    "owner": "Bob"
}

pet3 = {
    "type": "parrot",
    "owner": "Steve"
}

pet4 = {
    "type": "hamster",
    "owner": "David"
}

pets = [pet1, pet2, pet3, pet4]


for pet in pets:
    print("Pet type:", pet["type"])
    print("Owner's name:", pet["owner"])
    print() 