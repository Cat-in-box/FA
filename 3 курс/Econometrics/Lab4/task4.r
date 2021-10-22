#install.packages('lmtest')

library(lmtest)
getwd()
setwd('//vpvserver3/STUDENTS/Факультет ИТиАБД/ПИ19-3/Жевагина Анастасия Владимировна - 191758/Эконометрика/Lab 4')

data <- read.table('AG.txt', dec=',', header=TRUE)
data

m <- lm(y~x, data=data)
sm = summary(m); sm

matrix_coef <- sm$coefficients; matrix_coef

print(paste("y =", matrix_coef[1, 1], "+", matrix_coef[2, 1], "xi"))
print(paste("  (", matrix_coef[1, 2], ")(", matrix_coef[2, 2], ")"))

A <- (sum(abs(sm$residuals/data$y))/length(data$y))*100; A

confint(m)