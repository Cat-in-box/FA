# -*- coding: utf-8 -*-
import random
def Isklyucheniya():
    global r
    print ('Генерирую число...')
    r = random.randint(1, 50)
    if r == 2:
        raise Exception
    elif r == 4:
        raise AttributeError
    elif r == 6:
        raise IOError
    elif r == 8:
        raise IndexError
    elif r == 10:
        raise KeyError
    elif r == 12:
        raise KeyboardInterrupt        
try:
    Isklyucheniya()
except KeyboardInterrupt:
    print('У меня небольшая проблема. Это KeyboardInterrupt')
except KeyError:
    print('У меня небольшая проблема. Это KeyError')
except IndexError:
    print('У меня небольшая проблема. Это IndexError')
except IOError:
    print('У меня небольшая проблема. Это IOError')
except AttributeError:
    print('У меня небольшая проблема. Это AttributeError')
except Exception:
    print('У меня небольшая проблема. Это Exception')
else:
    print('Какое красивое число! Это ', r)
