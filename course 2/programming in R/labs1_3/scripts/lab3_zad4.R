# преобразование ввода с клавиатуры по цепочке
# приведения типов: logical – integer – double – character
input <- function(name) {
    x <- readline(paste0(name, " = "))
    t <- as.logical(x)
    if (is.na(t)) {
        t <- as.integer(x)
        if (is.na(t)) {
            t <- as.double(x)
            if (is.na(t)) {
                return(x)
            }
        }
    }
    return(t)
}

main <- function() {
    a <- input("a")
    b <- input("b")

    print('Сравнение через "<":')
    print('Неявное преобразование: logical – integer – double – character')
    print(a)
    print(paste0("a(", typeof(a), ") < ", "b(", typeof(b), ") = ", a < b))
}

main()