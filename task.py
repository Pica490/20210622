import datetime

def output(function):

    def new_function(*args,**kwargs):

        f = function(*args,**kwargs)
        record = f'{f}\nВызвана функция: {new_function.__name__}\nАргументы: {args}{kwargs}\nДата и время вызова: {datetime.datetime.now()}'
        return record

    return new_function

@output
def function1(a,b):
    print(a*b)
    return True

with open("result.txt", "w", encoding='utf-8') as f:
    f.write(function1(2,4))

