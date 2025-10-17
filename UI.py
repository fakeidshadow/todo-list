from User import User

PROJECT_IDX = -1

def print_main_menu():
    print('- '*10)
    print('1  -> add project')
    print('2  -> edit project')
    print('3  -> delete project')
    print('4  -> show projects')
    print('-1 -> exit')


def start():
    user = User()
    command = ''
    while command != '-1':
        print_main_menu()
        command = input()
        if command == '1':
            pass
        elif command == '2':
            pass
        elif command == '3':
            pass
        elif command == '4':
            pass
        elif command != '-1':
            pass
