import InsectClass as c


def main():
    new_insect = c.Insect()

    new_insect.flight()

    print(f"This insect can fly {new_insect.get_flight()} mile(s). ")


main()
