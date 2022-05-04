
def main():
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != '':
      year = int(input("Year: "))
      cost = int(input("Cost: $"))
      guitar_add = Guitar(name, year, cost)
      guitars.append(guitar_add)
      print(guitar_add, "added.")
      name = input("Name: ")

    if guitars != '':
        for i, guitar in enumerate(guitars):
            if guitar.is_vintage():
                vintage_string = "(vintage)"
            else:
                vintage_string = " "
            print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i+1, guitar.name, guitar.year, guitar.cost, vintage_string))
    else:
            print("No guitars :( Quick, go and buy one!")


main()