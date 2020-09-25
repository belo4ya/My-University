# setwd("D:\\RProjects\\control-work\\BestMilkITWRLD\\Анализ")
setwd("./BestMilkITWRLD/Анализ")
files <- dir()

PURCHASE_PRICE <- 5500
SALE_PRICE <- 8000
UTILIZTION_PRICE <- 400

# читает сразу МНОГО файлов
read_tables <- function(files) {
  tables_list = list()
  for (i in 1:length(files)) {
    tables_list[i] <- list(read.table(files[i], header = TRUE, sep = ",", encoding = "UTF-8"))
  }
  return(tables_list)
}

# создает таблицу с ПЕРЕДАННЫМИ именами столбцов и строк
create_table <- function(columns, rows) {
  new_table = data.frame(check.names = F)
  for (i in 1:length(columns)) {
    for (j in 1:length(rows)) {
      new_table[j, i] <- NA
    }
  }
  colnames(new_table) <- columns
  rownames(new_table) <- rows
  return(new_table)
}


# ============ вспомогательные функции для week_table ============ #

get_selling <- function(store_out) {
  return(sum(as.data.frame(store_out)[2]))
}

get_arrival <- function(store_in) {
  return(sum(as.data.frame(store_in)[2]))
}

get_utilization <- function(store_in, store_out) {
  return(get_arrival(store_in)- get_selling(store_out))
}

get_revenue <- function(store_out) {
  return(get_selling(store_out) * SALE_PRICE)
}

get_expenses <- function(store_in, store_out) {
  purchase_expenses <- get_selling(store_in) * PURCHASE_PRICE
  utilization_expenses <- get_utilization(store_in, store_out) * UTILIZTION_PRICE
  return(purchase_expenses + utilization_expenses)
}

get_profit <-function(store_in, store_out) {
  return(get_revenue(store_out) - get_expenses(store_in, store_out))
}

# рассчитывает колонку "Выручка"
calc_revenue <- function(data_table, data_out) {
  for (i in 1:length(data_out)) {
    data_table[i, 1] <- get_revenue(data_out[i])
  }
  
  revenue <- data_table[1:10, 1]
  data_table[11, 1] <- sum(revenue)
  data_table[12, 1] <- mean(revenue)
  return(data_table)
}

# рассчитывает колонку "Прибыль"
calc_profit <- function(data_table, data_in, data_out) {
  for (i in 1:length(data_in)) {
    data_table[i, 2] <- get_profit(data_in[i], data_out[i])
  }
  
  profit <- data_table[1:10, 2]
  data_table[11, 2] <- sum(profit)
  data_table[12, 2] <- mean(profit)
  return(data_table)
}

# рассчитывает колонку "Реализация"
calc_selling <- function(data_table, data_out) {
  for (i in 1:length(data_out)) {
    data_table[i, 3] <- get_selling(data_out[i])
  }
  
  selling <- data_table[1:10, 3]
  data_table[11, 3] <- sum(selling)
  data_table[12, 3] <- mean(selling)
  return(data_table)
}

# рассчитывает колонку "Списание"
calc_utilization <- function(data_table, data_in, data_out) {
  for (i in 1:length(data_out)) {
    data_table[i, 4] <- get_utilization(data_in[i], data_out[i])
  }
  
  utilization <- data_table[1:10, 4]
  data_table[11, 4] <- sum(utilization)
  data_table[12, 4] <- mean(utilization)
  return(data_table)
}

# рассчитывает колонку "Равномерность продаж (sd)"
calc_uniformity_sales <- function(data_table, data_out) {
  for (i in 1:length(data_out)) {
    data_table[i, 5] <- sd(as.data.frame(data_out[i])[,2])
  }
  
  uniformity <- data_table[1:10, 5]
  data_table[11, 5] <- sum(uniformity)
  data_table[12, 5] <- mean(uniformity)
  return(data_table)
}

# ============ вспомогательные функции для week_table ============ #


# ============ вспомогательные функции для day_table ============ #

find_max_sales <- function(data_table, data_out) {
  for (i in 1:length(data_out)) {
    data_frame = as.data.frame(data_out[i])
    data_table[i, 1] <- max(data_frame[2])
    data_table[i, 2] <- data_frame[[1]][data_frame[2] == data_table[i, 1]]  # true-шный способ!
  }
  
  return(data_table)
}

find_min_sales <- function(data_table, data_out) {
  for (i in 1:length(data_out)) {
    data_frame = as.data.frame(data_out[i])
    data_table[i, 3] <- min(data_frame[2])
    data_table[i, 4] <- data_frame[[1]][data_frame[2] == data_table[i, 3]]  # true-шный способ!
  }
  
  return(data_table)
}

find_max_utilization <- function(data_table, data_in, data_out) {
  for (i in 1:length(data_out)) {
    utilization <- as.data.frame(data_in[i])[2] - as.data.frame(data_out[i])[2]
    data_table[i, 5] <- max(utilization)
    data_table[i, 6] <- which.max(utilization[[1]])  # оказывается можно было так...
  }
  
  return(data_table)
}

# ============ вспомогательные функции для day_table ============ #


week_table <- create_table(c("Выручка", "Прибыль", "Реализация", "Списание", "Равномерность продаж (sd)"), 
                           c("Магазин 1", "Магазин 2", 
                             "Магазин 3", "Магазин 4", 
                             "Магазин 5", "Магазин 6", 
                             "Магазин 7", "Магазин 8",
                             "Магазин 9", "Магазин 10", 
                             "Итого", "Среднее"))

day_table <- create_table(c("Продажи макс", "День",
                            "Продажи мин", "День",
                            "Списание макс", "День"),
                          c("Магазин 1", "Магазин 2", 
                            "Магазин 3", "Магазин 4", 
                            "Магазин 5", "Магазин 6", 
                            "Магазин 7", "Магазин 8",
                            "Магазин 9", "Магазин 10"))

data_in <- read_tables(files[grep("*in.txt", files)])
data_out <- read_tables(files[grep("*out.txt", files)])

week_table <- calc_revenue(week_table, data_out)
week_table <- calc_profit(week_table, data_in, data_out)
week_table <- calc_selling(week_table, data_out)
week_table <- calc_utilization(week_table, data_in, data_out)
week_table <- calc_uniformity_sales(week_table, data_out)

day_table <- find_max_sales(day_table, data_out)
day_table <- find_min_sales(day_table, data_out)
day_table <- find_max_utilization(day_table, data_in, data_out)

print(week_table)
print(day_table)

day_table_copy <- day_table
day_table_copy[11, 1] <- NA
day_table_copy[12, 1] <- NA
join <- cbind(week_table, day_table_copy)
print(join)

write.csv2(week_table, "week_table.csv")
write.csv2(day_table, "day_table.csv")
write.csv2(join, "join.csv")
