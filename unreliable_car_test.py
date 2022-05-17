from prac_08.unreliable_car import UnreliableCar


def main():
    first_car = UnreliableCar("Car 1", 100, 100)
    second_car = UnreliableCar("Car 2", 100, 10)

    for i in range(1, 5):
        print("Drive {} km:".format(i))
        print("{} drove {} km".format(first_car.name, first_car.drive(i)))
        print("{} drove {} km".format(second_car.name, second_car.drive(i)))

    print(first_car)
    print(second_car)
main()