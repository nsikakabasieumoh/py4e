def elevatorConv():
    eu_floor = int(input('Europe floor: '))
    us_floor = eu_floor + 1
    return us_floor

def sample_try_except():
    prompt = input('Enter a Number: ')
    try:
        conv_int = int(prompt)
    except:
        conv_int = -1
    
    if conv_int > 0:
        return 'Nice Work.'
    else:
        return 'Not a number.'

def largest_number(iter:list, control = None):
    for item in iter:
        if control is None:
            control = item
        elif item > control: control = item
    return control
