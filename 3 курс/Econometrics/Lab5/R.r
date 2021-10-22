#install.packages("lmtest")
library(lmtest)

setwd('C:/Users/anast/Documents/GitHub/FA/3 курс/Econometrics/Lab5')

data <- read.table('GAM.txt', dec=',', header=TRUE)
data

y <- data$y
x1 <- data$x1
x2 <- data$x2
x3 <- data$x3
x4 <- data$x4

m <- lm(y~x1+x2+x3+x4, data = data)
sm <- summary(m); sm
e <- sm$residuals; e

Se <- sm$sigma; Se
R_2 <- sm$r.squared; R_2
Ft <- sm$fstatistic[1]; Ft
A <- (sum(abs(sm$residuals/y))/length(y))*100; A

#GQtest
gq <- gqtest(m, order.by=~y, fraction=0, data=data);gq
# pv<a => присутствует проблема гетероскедастичности

#BPtest
bp <- bptest(m, data = data); bp
# pv<a => присутствует проблема гетероскедастичности

#DWtest
dw <- dwtest(m); dw
# pv>a => H0 принимается, автокорреляция первого порядка отсутствует

#BGtest
bg <- bgtest(m, order = 1); bg
# pv>a => H0 принимается, автокорреляция первого порядка отсутствует

#White_test
wt <- bptest(m, data=data, varformula=~y + I(y^2), studentize=TRUE); wt

e2 <- e^2
plot(data$x1, e2)
plot(data$x2, e2)
plot(data$x3, e2)
plot(data$x4, e2)
