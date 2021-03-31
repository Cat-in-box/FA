import numpy as np

class Task_2 ():
	def __init__(self, l, u, m, n):
		self.l = l
		self.u = u
		self.m = m
		self.n = n
		self.matrix = np.zeros((m+n+1, m+n+1))
		for i in range(self.m + self.n):
			self.matrix[i, i+1] = l
			if i < m:
				self.matrix[i+1, i] = (i+1) * self.u
			else:
				self.matrix[i+1, i] = self.m * self.u
	
	def Par_A(self):
		D = np.zeros(self.matrix.shape)
		for i in range (self.m + self.n + 1):
			D[i, i] = sum(self.matrix[i])
		M = self.matrix.T - D
		M_ = np.copy(M)
		M_[-1, :] = 1
		B = np.append(np.zeros(M_.shape[0]-1), 1)
		self.X = np.dot(np.linalg.inv(M_), B)
		return self.X

	def Par_B(self):
		return self.X[-1]

	def Par_C(self):
		return (1 - self.X[-1], (1 - self.X[-1]) * self.l)

	def Par_D(self):
		return sum(
			[i * self.X[self.m + i] for i in range (1, self.n + 1)]
		)

	def Par_E(self):
		return sum(
			[(i + 1)/(self.m * self.u) * self.X[self.m + i] for i in range(self.n)]
		)

	def Par_F(self):
		return sum([
			sum(
				[i * self.X[i] for i in range(1, self.m + 1)]
			),
			sum(
				[self.m * self.X[i] for i in range(self.m + 1, self.m + self.n + 1)]
			)
		])

	def Par_G(self):
		return sum(
			self.X[:self.m]
		)

	def Par_H(self):
		return 1/self.l

if __name__ == "__main__":
	print("Задание 2")
	Task2 = Task_2(14, 10, 2, 19)
	print('a) найдите установившиеся вероятности состояний:\n', Task2.Par_A())
	print('b) найдите вероятность отказа в обслуживании:\n', Task2.Par_B())
	print('c) найдите относительную и абсолютную интенсивность обслуживания:\n', Task2.Par_C())
	print('d) найдите среднюю длину в очереди:\n', Task2.Par_D())
	print('e) найдите среднее время в очереди:\n', Task2.Par_E())
	print('f) найдите среднее число занятых каналов:\n', Task2.Par_F())
	print('g) найдите вероятность того, что поступающая заявка не будет ждать в очереди:\n', Task2.Par_G())
	print('h) найти среднее время простоя системы массового обслуживания:\n', Task2.Par_H())