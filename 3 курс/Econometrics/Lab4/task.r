#install.packages('lmtest')
#install.packages("ggiraphExtra")
library(lmtest)
library(ggiraphExtra)

getwd()
setwd('')

data <- read.table('AG.txt', dec=',', header=TRUE)
data

y <- data$y
x <- data$x

#1) линейная модель
m1 <- lm(y~x, data=data); m1
sm1 = summary(m1); sm1

Se1 <- sm1$sigma; Se1
R_21 <- sm1$r.squared; R_21
Ft1 <- sm1$fstatistic[1]; Ft1
A1 <- (sum(abs(sm1$residuals/y))/length(y))*100; A1

ggPredict(m1, interactive = TRUE)

#2) показательная модель
m2 <- lm(log10(y)~x, data=data); m2
sm2 <- summary(m2); sm2

Se2 <- sm2$sigma; Se2
R_22 <- sm2$r.squared; R_22
Ft2 <- sm2$fstatistic[1]; Ft2
A2 <- (sum(abs(sm2$residuals/log10(y)))/length(log10(y)))*100; A2

ggPredict(m2, interactive = TRUE)

#3) степенная модель
m3 <- lm(log10(y)~log10(x), data=data); m3
sm3 <- summary(m3); sm3

Se3 <- sm3$sigma; Se3
R_23 <- sm3$r.squared; R_23
Ft3 <- sm3$fstatistic[1]; Ft3
A3 <- (sum(abs(sm3$residuals/log10(y)))/length(log10(y)))*100; A3

ggPredict(m2, interactive = TRUE)

#4) гиперболическая модель
X <- 1/x
m4 <- lm(y~X, data=data); m4
sm4 <- summary(m4); sm4

Se4 <- sm4$sigma; Se4
R_24 <- sm4$r.squared; R_24
Ft4 <- sm4$fstatistic[1]; Ft4
A4 <- (sum(abs(sm4$residuals/y))/length(y))*100; A4

ggPredict(m4, interactive = TRUE)