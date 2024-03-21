from cli.states import Start

print(r'''
 _    _       _    _ _____  ______       _ _     _     
| |  | |     | |  | /  ___| | ___ \     (_) |   | |
| |  | | ___ | |  | \ `--.  | |_/ /_   _ _| | __| |___ 
| |/\| |/ _ \| |/\| |`--. \ | ___ \ | | | | |/ _` / __|
\  /\  / (_) \  /\  /\__/ / | |_/ / |_| | | | (_| \__ \
 \/  \/ \___/ \/  \/\____/  \____/ \__,_|_|_|\__,_|___/

''')

state = Start()

while True:
    state.show()
    option = input('\nSelect option: ')
    print('\n' + '=' * 60 + '\n')

    if not option.isnumeric():
        continue
    else:
        state = state.go_to(int(option))
