import re
option = '   '
unit = 'X'
def create_field():
    global option
    c = [' ' + i for i in option]
    b = ''.join(c)
    res = re.findall('......', b)
    print('-' * 9)
    for i in res:
        print(f'|{i} |')
    print('-' * 9)

def def_win():
    global option
    pattern = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    pattern_num = []
    for i in pattern:
        res = []
        for num in i:
            res += option[num]
        pattern_num.append(res)
    for i in pattern_num:
        if set(i) == {'X'} or set(i) == {'O'}:
            res = set(i)
    if type(res) is set:
        res = list(res)
        print(f'{res[0]} wins')
    elif ' ' not in option:
        print('Draw')
    else:
        step()

def move(enter_move):
    global option
    global unit
    check_move = ['11', '12', '13', '21', '22', '23', '31', '32', '33']
    get_index = check_move.index(enter_move)
    if option[get_index] == 'X' or option[get_index] == 'O':
        print('This cell is occupied! Choose another one!')
        step()
    elif option[get_index] == ' ':
        option = list(option)
        option[get_index] = unit
        option = ''.join(option)
        unit = 'O' if unit == 'X' else 'X'
        create_field()
        def_win()
def step():
    enter_move = input('Enter the coordinates:').replace(' ', '')
    if enter_move.isdigit() == True:
        if enter_move[0] > '3' or enter_move[1] > '3':
            print('Coordinates should be from 1 to 3!')
            return step()
        else:
           return move(enter_move)
    if type(enter_move) == str:
        print('You should enter numbers!')
        return step()


create_field()
step()


