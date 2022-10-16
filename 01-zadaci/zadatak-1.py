def dz_func1(listOfStrings):
    assert all(isinstance(n, str) for n in listOfStrings)
    return [elem for elem in listOfStrings if len(elem) > 4]

print(dz_func1(["Pas", "Macka", "Stol"]))