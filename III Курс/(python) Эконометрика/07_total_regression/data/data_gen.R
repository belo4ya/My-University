library('MASS')

options(digits = 4)

n <- 13  # позиция в списке

set.seed(n * 10)

sigma <- matrix(
  c(
    1, 0.8, 0.4, -0.6,
    0.8, 1, 0.7, -0.4,
    0.4, 0.7, 1, -0.1,
    -0.6, -0.4, -0.1, 1
  ),
  nrow = 4,
  ncol = 4
)
mu <- c(n * 15, n^2, n + 20, 60 - n)

data <- mvrnorm(300, mu, sigma)
data <- as.data.frame(data, col.names = c('y', 'x1', 'x2', 'x3'))

head(data)
