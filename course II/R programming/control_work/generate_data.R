source("utils.R", encoding = "UTF-8")

SUPPLY_IN <- 1
SALE_OUT <- 2


tryhard.random <- function(min, max, n=1) {
  return(floor((runif(n) * ((max - min) + 1)) + min))
}


.gen.sale.level.distribution <- function(sale_level, data_in) {
  max_sum <- round(sum(data_in) * sale_level / 100)
  data_out <- c()

  for (i in 1:length(data_in)) {
    data_out[i] <- tryhard.random(0, data_in[i])  # тут можно оптимизировать
  }

  step <- 1
  if (sum(data_out) > max_sum) {
    step <- -step
  }

  n <- 0
  start <- tryhard.random(1, length(data_in))
  while ((sum(data_out) <= max_sum - abs(step) * 2) || (sum(data_out) >= max_sum + abs(step) * 2)) {
    if ((data_out[start] > 0 + abs(step)) && 
        (data_out[start] < data_in[start] - abs(step))) {
      data_out[start] <- data_out[start] + step
    }
    start <- ifelse(start == length(data_in), 1, start + 1)
    
    if (n > 20000) break
    n <- n + 1
  }
  # print(paste0("Подбор значений за ", n, " итераций"))
  return(data_out)
}


.generate.data.supply <- function(days, goods, path, min, max, headers) {
  filename <- paste0(path, "/in.txt")
  
  in_table <- create.table(c("день", goods), 1:days)
  in_table[, 1] <- 1:days
  
  for (i in 2:length(in_table)) {
    in_table[, i] <- tryhard.random(min, max, days)
  }
  
  write.table(in_table, file = filename, sep = ",",
              row.names = F, col.names = headers)
}


.generate.data.sale <- function(days, goods, sale_level, path, min, headers) {
  filename <- paste0(path, "/out.txt")
  
  if (length(dir(paste0(path, "/"), "in.txt")) != 1) {
    stop("Error: file not found - in.txt")
  }
  in_table <- read.table(paste0(path, "/in.txt"), header = T, sep = ",")
  
  out_table <- create.table(c("день", goods), 1:days)
  out_table[, 1] <- 1:days
  
  if (sale_level[1] != -1) {
    # заполнение с saleLevel параметром
    for (i in 2:length(out_table)) {
        out_table[i] <- .gen.sale.level.distribution(sale_level[i-1], in_table[, i])
    }
  } else {
    # рандомное заполнение
    for (i in 2:length(out_table)) {
      for (j in 1:length(out_table[, 1])) {
        out_table[, i][j] <- tryhard.random(min, in_table[, i][j])
      }
    }
  }
  
  write.table(out_table, file = filename, sep = ",",
              row.names = F, col.names = headers)
}


generate.supply.sale <- function(path = ".",
                                 type = SUPPLY_IN,
                                 min = 50,
                                 max = 200,
                                 headers = T) {
  if (max < 1) stop("Error: invalid value - max < 1")
  if (min < 0) stop("Error: invalid value - min < 0")
  if ((max - min) < 1) stop("Error: invalid value - (max - min) < 1")
  days <- 7
  goods <- "молоко"
  sale_level <- F
  
  switch(
    type,
    .generate.data.supply(days, goods, path, min, max, headers),
    .generate.data.sale(days, goods, sale_level, path, min, headers)
  )
}


generate.supply.sale.many <- function(path = ".",
                                      type = SUPPLY_IN,
                                      days = 7,
                                      goods = c("молоко"),
                                      min = 50,
                                      max = 200,
                                      headers = T) {
  if (days < 1) stop("Error: invalid value - days < 1")
  if (max < 1) stop("Error: invalid value - max < 1")
  if (min < 0) stop("Error: invalid value - min < 0")
  if ((max - min) < 1) stop("Error: invalid value - (max - min) < 1")
  sale_level <- F

  switch(
    type,
    .generate.data.supply(days, goods, path, min, max, headers),
    .generate.data.sale(days, goods, sale_level, path, min, headers)
  )
}


generate.sale.level <- function(path = ".",
                                days = 7,
                                goods = c("молоко"),
                                sale_level = list(c(50, 50)),
                                headers = T) {
  if (days < 1) stop("Error: invalid value - days < 1")
  if (length(sale_level) != length(goods)) {
    stop("Error: invalid value - length(sale_level) != length(goods)")
  }
  
  .generate.data.sale(days, goods, sale_level, path, NULL, headers)
}


gen.supply <- function(path = ".",
                       days = 7,
                       goods = c("молоко"),
                       min = 50,
                       max = 200,
                       headers = T) {

  generate.supply.sale.many(path,
                            type = SUPPLY_IN,
                            days,
                            goods,
                            min,
                            max,
                            headers)
}


gen.sale <- function(path = ".",
                     days = 7,
                     goods = c("молоко"),
                     sale_level = list(c(50, 50)),
                     headers = T) {
  
  generate.sale.level(path,
                      days,
                      goods,
                      sale_level,
                      headers)
}
