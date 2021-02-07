import numpy as np
class lesson_1 ():
    def __init__(self):
        self.b = np.array([[0.1, 0.4, 0.5], [0.3, 0.2, 0.5], [0.6, 0.35, 0.05]])
        self.A = np.array([0.1, 0.2, 0.3])
    
    #ЗАДАЧА 1
    def task_1 (self, k):

        for i in range(k):
            if i == 0:
                P_k = self.b
            else:
                P_k = P_k @ self.b

        return (P_k)

    #ЗАДАЧА 2
    def task_2 (self, k):
        return (self.A @ self.task_1(k))

if __name__ == "__main__":
    lesson_1_start = lesson_1()
    print(lesson_1_start.task_1(int(input('Введите степень: '))))
    print(lesson_1_start.task_2(int(input('Введите степень: '))))
