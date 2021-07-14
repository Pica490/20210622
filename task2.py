import logging

def output(file_name):

    def _output(function):

        def new_function(*args,**kwargs):
            f = function(*args,**kwargs)

            logging.basicConfig(filename = file_name, filemode='a',format= '%(asctime)s - %(message)s', level=logging.DEBUG)
            logging.debug(f'Функция {function.__name__} с аргументами {args, kwargs} результатом {f} зарегистрирована.')
            return f

        return new_function

    return _output

@output(file_name = 'app.log')
def function1(a,b):
    print(a*b)
    return True

function1(2,4)


