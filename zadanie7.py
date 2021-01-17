def person_print(name, last_name, *others, age):
    formatted_data = 'imię: {}, nazwisko: {}, wiek: {}'.format(name,last_name,age)
    others_str = ' '
    for arg in others:
        others_str += arg + ' '
    print(formatted_data + others_str)

person_print('Ksawery', 'Grzesiak', 'Test jeden', 'Test dwa', age='27')
print("-------------")

def argsy(argument, *args):
    print("argument: {}".format(argument))
    print("args: {}".format(args))
        
argsy('test', 'jezyki', 'skryptowe', 'python')
print("-------------")

def kwargsy(argument, **kwargs):
    print("argument: {}".format(argument))
    print("kwargs: {}".format(kwargs))
        
kwargsy(dodatkowy=48, nastepny=111, argument=12)
print("-------------")

def argskwargs(argument, *args, **kwargs):
    print("argument: {}".format(argument))
    print("args: {}".format(args))
    print("kwargs: {}".format(kwargs))

argskwargs('Test', 'args jeden', 'args dwa', a='kwargs', b='drugi')