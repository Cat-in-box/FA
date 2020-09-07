import struct
import math
from bitarray import bitarray
import hashlib

class MD5:
    def __init__(self, string):
        self.buffers = {'A': 0x67452301, 'B': 0xEFCDAB89, 'C': 0x98BADCFE, 'D': 0x10325476} # Шаг 3. Буфер значений
        self.string = string
        self.result = None

        self.step_4(self.step_2(self.step_1()))
        self.result = self.step_5()

    def step_1(self): # Шаг 1. Выравнивание потока (конвертация строки в bit array)

        bit_array = bitarray(endian='big')
        bit_array.frombytes(self.string.encode('utf-8'))
        
        bit_array.append(1) # Сначала к концу потока дописывают единичный бит.

        while bit_array.length() % 512 != 448: # Затем добавляют 0, чтобы новая длина потока стала сравнима с 448 по модулю 512
            bit_array.append(0)
        return bitarray(bit_array, endian='little')

    def step_2(self, step_1_result): # Шаг 2. Добавление длины сообщения

        # В конец сообщения дописывают 64-битное представление длины данных (количество бит в сообщении) до выравнивания
        length = (len(self.string) * 8) % pow(2, 64)
        length_bit_array = bitarray(endian='little')
        length_bit_array.frombytes(struct.pack('<Q', length))

        result = step_1_result.copy()
        result.extend(length_bit_array)
        return result

    def step_4(self, step_2_result): # Шаг 4. Вычисление в цикле

        def F(x, y, z): # 1й раунд
            return (x & y) | (~x & z)
        
        def G(x, y, z): # 2й раунд
            return (x & z) | (~z & y)
        
        def H(x, y, z): # 3й раунд
            return x ^ y ^ z
        
        def I(x, y, z): # 4й раунд
            return y ^ (~z | x)

        def rotate_left(x, n):
            return (x << n) | (x >> (32 - n))
        def modular_add(a, b):
            return (a + b) % pow(2, 32)

        # Определение таблицы констант T
        T = [math.floor(pow(2, 32) * abs(math.sin(i + 1))) for i in range(64)]

        N = len(step_2_result) // 32

        for chunk_index in range(N // 16):

            start = chunk_index * 512 # Каждый 512-битный блок проходит 4 этапа вычислений по 16 раундов. Для этого блок представляется в виде массива X из 16 слов по 32 бита.
            X = [step_2_result[start + (x * 32): start + (x * 32) + 32] for x in range(16)]

            X = [int.from_bytes(word.tobytes(), byteorder='little') for word in X] # Переводим все в int из байтов

            A = self.buffers['A'] # Значение из буферов
            B = self.buffers['B']
            C = self.buffers['C']
            D = self.buffers['D']

            for i in range(4 * 16):

                # 1-й раунд
                if 0 <= i <= 15:
                    k = i
                    s = [7, 12, 17, 22]
                    buff = F(B, C, D)

                # 2-й раунд
                elif 16 <= i <= 31:
                    k = ((5 * i) + 1) % 16
                    s = [5, 9, 14, 20]
                    buff = G(B, C, D)

                # 3-й раунд
                elif 32 <= i <= 47:
                    k = ((3 * i) + 5) % 16
                    s = [4, 11, 16, 23]
                    buff = H(B, C, D)

                # 4-й раунд
                elif 48 <= i <= 63:
                    k = (7 * i) % 16
                    s = [6, 10, 15, 21]
                    buff = I(B, C, D)

                buff = modular_add(buff, A) # Тут происходит что-то
                buff = modular_add(buff, X[k])
                buff = modular_add(buff, T[i])
                buff = rotate_left(buff, s[i % 4])
                buff = modular_add(buff, B)

                A = D # Замена регистров
                D = C
                C = B
                B = buff

            self.buffers['A'] = modular_add(self.buffers['A'], A) # Обновление буферов
            self.buffers['B'] = modular_add(self.buffers['B'], B)
            self.buffers['C'] = modular_add(self.buffers['C'], C)
            self.buffers['D'] = modular_add(self.buffers['D'], D)

    def step_5(self): # Шаг 5. Результат вычислений (Результат вычислений находится в буфере ABCD, это и есть хеш.) Если выводить побайтово, начиная с младшего байта A и закончив старшим байтом D, то мы получим MD5-хеш.

        A = struct.unpack('<I', struct.pack('>I', self.buffers['A']))[0] # Конвертация в прямой порядок байтов
        B = struct.unpack('<I', struct.pack('>I', self.buffers['B']))[0]
        C = struct.unpack('<I', struct.pack('>I', self.buffers['C']))[0]
        D = struct.unpack('<I', struct.pack('>I', self.buffers['D']))[0]

        A = format(A, "08x") # Форматирование на выходе в 16ричной системе
        B = format(B, "08x")
        C = format(C, "08x")
        D = format(D, "08x")

        return A+B+C+D

if __name__ == '__main__':
    input_string = input('Введите строку для хеширования -> ')
    md5_hash = MD5(input_string)
    print('Хеш MD5:\n', md5_hash.result)
    result = hashlib.md5(input_string.encode())
    print('Хеш MD5 (hashlib):\n', result.hexdigest())
    print('Совпадение результатов:', md5_hash.result == result.hexdigest())