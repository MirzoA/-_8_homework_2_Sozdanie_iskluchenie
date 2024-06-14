class InvalidDataExeption(Exception):
    pass

class ProcessingException(Exception):
    pass

def generate_exception(name):
    if name == 'Alex':
        raise InvalidDataExeption('Предоставлены неверные данные')
    elif name == 'alex':
        raise ProcessingException('Во время обработки произошла ошибка')
def caller_function(name):
    try:
        generate_exception(name)
    except InvalidDataExeption as e:
        print('Исключение InvalidDataExeption прихвачено:', e)
        raise
    except ProcessingException as e:
        print('Исключение ProcessingException прихвачено:', e)
        raise
    else:
        print('Исключения не обнаружены')
    finally:
        print('Блок завершен')
try:
    caller_function('Alex')
except InvalidDataExeption as e:
    print('исключение InvalidDataExeption обрабатывается в основной программе:', e)
except ProcessingException as e:
    print('исключение ProcessingException обрабатывается в основной программе:', e)