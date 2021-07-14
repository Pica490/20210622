import hashlib
import json
import logging

with open('result.json', encoding='utf-8') as f:
    data = json.loads(f.read())

def output(file_name):

    def _output(function):

        def new_function(*args,**kwargs):
            f = function(*args,**kwargs)

            logging.basicConfig(filename = file_name, filemode='a',format= '%(asctime)s - %(message)s', level=logging.DEBUG)
            logging.debug(f'Функция {function.__name__} с аргументами {args, kwargs} результатом {f} зарегистрирована.')
            return f

        return new_function

    return _output

@output(file_name = 'app2.log')
def gen_hash(start,end):
    while start < end:
        yield start
        start += 1


for item in gen_hash(0, len(data)-1):
    print(hashlib.md5(data[item].encode('utf-8')).hexdigest())