def pick_pet(pet) :
    try:
        pets = {'bird': 3.5, 'cat': 5.0, 'dog': 7.25, 'gerbil': 1.5}
        return pets[pet]
    except KeyError:
        print("I don't know what that pet is.  Please try again.")


print(pick_pet('dog'))
print(pick_pet('bunny'))
