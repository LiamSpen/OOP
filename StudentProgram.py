import StudentClass as c


def main():
    student = c.Student(851, "Liam", "12/13/2002", "S")

    student.age()
    student.register()

    print(f"This student is {student.get_age()} years old.")
    print(f"This student needs to register {student.get_registration()}.")


main()
