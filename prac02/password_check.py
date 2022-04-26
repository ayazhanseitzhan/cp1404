minimum = 10
def main():
 password = get_password()

 asterisks(password)


def asterisks(password):
    print('*' * len(password))


def get_password():
    password = input("Enter password of at least {} characters: ".format(minimum))
    while len(password) < minimum:
        print('password is too short')
        password = input("Enter password of at least {} characters: ".format(minimum))
    return password


main()