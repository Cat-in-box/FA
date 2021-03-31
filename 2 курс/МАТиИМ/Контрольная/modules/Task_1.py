import numpy as np

class Task_1 ():
	def __init__(self, matrix):
		try:
			if len(matrix) != 15:
				raise ValueError
			for i in range(len(matrix)):
				if len(matrix[i]) != 15:
					raise ValueError
		except:
			print('Что-то не так с матрицей')
			exit(0)
		else:
			self.matrix = matrix
			for i in range(len(self.matrix)):
				self.matrix[i, i] = 1 - sum(self.matrix[i])
			self.E_matrix = np.eye(self.matrix.shape[0])
	
	def Par_1(self, k, i, j):
		return (np.linalg.matrix_power(self.matrix, k)[i-1, j-1])
	
	def Par_2(self, k, A):
		return np.dot(A, np.linalg.matrix_power(self.matrix, k))

	def Par_3(self, k, i, j):

		def Making_a_step (buf_matrix_1):
			buf_matrix_2 = np.zeros(self.matrix.shape)
			for i in range(self.matrix.shape[0]):
				for j in range(self.matrix.shape[1]):
					buf_matrix_2[i, j] = sum(
						[self.matrix[i, m] * buf_matrix_1[m, j] if m != j else 0 for m in range(self.matrix.shape[0])]
					)
			return buf_matrix_2

		buf_matrix_1 = np.copy(self.matrix)
		for _ in range(2, k+1):
			buf_matrix_1 = Making_a_step(buf_matrix_1)
		return buf_matrix_1[i-1, j-1]

	def Par_4(self, i, j, k):

		def Making_a_step_modif (buf_matrix_1, buf_prev_matrix):
			cur_len = buf_matrix_1.shape[0]
			buf_matrix_2 = np.zeros((cur_len, cur_len))
			for i in range(cur_len):
				for j in range(cur_len):
					buf_matrix_2[i, j] = sum(
						[buf_matrix_1[i, m] * buf_prev_matrix[m, j] if m != j else 0 for m in range(cur_len)]
					)
			return buf_matrix_2
		
		buf_matrix_1 = np.copy(self.matrix)
		buf_prev_matrix = np.copy(self.matrix)
		result = np.copy(self.matrix)
		for _ in range(1, k):
			buf_prev_matrix = Making_a_step_modif(buf_matrix_1, buf_prev_matrix)
			result += buf_prev_matrix
		return result[i-1, j-1]
	 
	def Par_5(self, i, j):

		def Making_a_step (buf_matrix_1):
			buf_matrix_2 = np.zeros(self.matrix.shape)
			for i in range(self.matrix.shape[0]):
				for j in range(self.matrix.shape[1]):
					buf_matrix_2[i, j] = sum(
						[self.matrix[i, m] * buf_matrix_1[m, j] if m != j else 0 for m in range(self.matrix.shape[0])]
					)
			return buf_matrix_2

		buf_matrix = self.matrix.copy()
		result = buf_matrix[i-1, j-1]
		for k in range(2, 10000):
			buf_matrix = Making_a_step(buf_matrix)
			result += k * buf_matrix[i-1, j-1]
		return result

	def Par_6(self, j, k):
		buf_matrix = np.zeros(self.matrix.shape)
		for i in range(1, k):
			buf_matrix += self.Par_6(j, i) * np.linalg.matrix_power(self.matrix, k-i)
		return ((np.linalg.matrix_power(self.matrix, k) - buf_matrix)[j-1, j-1])

	def Par_7(self, j, k):
		return sum(
			self.Par_6(j-1, n) for n in range(1, k+1)
		)
	
	def Par_8(self, j, Q):
		return sum(
			k*self.Par_6(j-1, k) for k in range(1, Q)
		)

	def Par_9(self):
		M_matrix = self.matrix.T - self.E_matrix
		M_matrix[-1, :] = 1
		B = np.append(np.zeros(M_matrix.shape[0]-1), 1)
		return np.dot(np.linalg.inv(M_matrix), B)

if __name__ == "__main__":
	print("Задание 1")
	Task1 = Task_1(np.array([[0, 0, 0, 0.41, 0.18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
							[0, 0, 0.31, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
							[0, 0.46, 0, 0.48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
							[0.2, 0.18, 0.26, 0, 0, 0, 0.1, 0.24, 0, 0, 0, 0, 0, 0, 0],
							[0.05, 0.07, 0, 0, 0, 0.3, 0.32, 0, 0, 0, 0, 0, 0, 0, 0],
							[0, 0.4, 0, 0, 0.52, 0, 0.01, 0, 0, 0, 0, 0, 0, 0, 0],
							[0, 0, 0, 0.21, 0, 0.1, 0, 0.21, 0.21, 0, 0.25, 0, 0, 0, 0],
							[0, 0, 0, 0, 0, 0, 0, 0, 0.19, 0, 0.68, 0, 0, 0, 0],
							[0, 0, 0, 0, 0, 0, 0.29, 0, 0, 0.15, 0, 0, 0.35, 0, 0],
							[0, 0, 0, 0, 0, 0, 0.46, 0, 0, 0, 0, 0, 0, 0, 0],
							[0, 0, 0, 0, 0, 0, 0, 0, 0, 0.34, 0, 0.03, 0.05, 0.21, 0.08],
							[0, 0, 0, 0, 0, 0, 0, 0.28, 0, 0, 0.04, 0, 0.13, 0.31, 0.2],
							[0, 0, 0, 0, 0, 0, 0, 0, 0.19, 0.24, 0, 0, 0, 0.49, 0],
							[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.25, 0, 0],
							[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.65, 0, 0, 0, 0]]))
	print('1) вероятность того, что за 7 шагов система перейдет из состояния 2 в состояние 7: ', Task1.Par_1(7, 2, 7))
	print('2) вероятности состояний системы спустя 6 шагов, если в начальный момент вероятность состояний были следующими \n   A=(0,06;0,01;0,14;0,1;0,14;0,06;0,06;0,1;0,05;0,05;0,08;0,05;0,01;0,01;0,08):\n', Task1.Par_2(6, (0.06, 0.01, 0.14, 0.1, 0.14, 0.06, 0.06, 0.1, 0.05, 0.05, 0.08, 0.05, 0.01, 0.01, 0.08)))
	print('3) вероятность первого перехода за 6 шагов из состояния 13 в состояние 1: ', Task1.Par_3(6, 13, 1))
	print('4) вероятность перехода из состояния 1 в состояние 6 не позднее чем за 6 шагов: ', Task1.Par_4(1, 6, 6))
	print('5) среднее количество шагов для перехода из состояния 2 в состояние 1: ', Task1.Par_5(2, 1))
	print('6) вероятность первого возвращения в состояние 4 за 7 шагов: ', Task1.Par_6(4, 7))
	print('7) вероятность возвращения в состояние 5 не позднее чем за 7 шагов: ', Task1.Par_7(5, 7))
	print('8) среднее время возвращения в состояние 7: ', Task1.Par_8(7, 10000)) #Долго выполняется
	print('9) установившиеся вероятности:\n', Task1.Par_9())