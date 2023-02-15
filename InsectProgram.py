import InsectClass as c


def main():
    new_insect = c.Insect('mosquito', 2, 4)

    new_insect.flight()

    print(
        f"The {new_insect.get_name()} can fly {new_insect.get_flight()} mile(s). ")


main()
