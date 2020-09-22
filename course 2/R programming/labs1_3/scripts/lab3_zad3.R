# возводит a в степень b
exp_ <- function(a, b) {
    res <- a ^ b
    print(paste0(a, " ^ ", b, " = ", res))
    return(res)
}

# делит a на b
div <- function(a, b) {
    res <- a / b
    print(paste0(a, " / ", b, " = ", res))
    return(res)
}

main <- function() {
    a <- NA; b <- NA
    while (is.na(a)) {
        a <- as.double(readline("a = "))
    }
    while (is.na(b)) {
        b <- as.double(readline("b = "))
    }
    exp_(a, b)
    exp_(b, a)
    div(a, b)
    div(a, 0)
}

main()
