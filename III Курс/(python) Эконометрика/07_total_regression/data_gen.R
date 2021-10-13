library('MASS')

options(digits = 4)

set.seed(13 * 10)

n <- 13  # позиция в списке

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
sigma

mu <- c(n * 15, n^2, n + 20, 60 - n)
?mvrnorm(300, mu, sigma)
