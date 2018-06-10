def main():
    print("Phonebooke")
    menu()

def menu():
    a="5"
    while a!='4':
        print('What do you want to do?')
        print('1.Enter a new record')
        print('2.Output all records')
        print('3. Delete abonent')
        print('4.Quit the program')
        a=input()
        if a=='1':
            inpute_name_and_phone_number()
        if a=='2':
            outpute_base()
        if a=='3':
            delete_abonent()
        if a=='4':
            exit()


def inpute_name_and_phone_number():
    a=2
    print(a)
    save_data_base()
    menu()
def save_data_base():
    b=3
    print(b)


def outpute_base():
    c=4
    print(c)
    menu()

def delete_abonent():
    f=5
    print(f)
    menu()


if __name__ == "__main__":
    main()
