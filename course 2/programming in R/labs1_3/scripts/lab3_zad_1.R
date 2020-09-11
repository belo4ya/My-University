library(stringi)  # использовал для конкатенации строк

a <- 7
b <- 3
c <- 5
d <- 10

print(stri_c("(a + b) * c) = ", (a + b) * c))
print(stri_c("(a + b) * (c - d)) = ", (a + b) * (c - d)))
print(stri_c("a / b * c = ", d / c * 7))
print(stri_c("a / b * c ^ d = ", a / b * c ^ d))
print(stri_c("d * a %% b = ", d * a %% b))
print(stri_c("(d * a) %% b = ", (d * a) %% b))
print(stri_c("d * a %/% b = ", d * a %/% b))
print(stri_c("(d * a) %/% b = ", (d * a) %/% b))
print(stri_c("(d * a) ^ 2 %/% b = ", (d * a) ^ 2 %/% b))
print(stri_c("((d * a) ^ 2) %/% b = ", ((d * a) ^ 2) %/% b))
print(stri_c("a %% b = ", a %% b))
print(stri_c("a %/% b = ", a %/% b))
