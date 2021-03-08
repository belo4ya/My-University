source("utils.R", encoding = "UTF-8")

PURCHASE_PRICE <- 100
SALE_PRICE <- 250
UTILIZTION_PRICE <- 20


# ============ вспомогательные функции для week_table ============ #

get_selling <- function(store_out) {
  return(sum(as.data.frame(store_out)[2:length(as.data.frame(store_out))]))
}

get_arrival <- function(store_in) {
  return(sum(as.data.frame(store_in)[2:length(as.data.frame(store_in))]))
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
  revenue <- data_table[1:length(data_out), 1]
  data_table[length(data_out) + 1, 1] <- sum(revenue)
  data_table[length(data_out) + 2, 1] <- mean(revenue)
  return(data_table)
}

# рассчитывает колонку "Прибыль"
calc_profit <- function(data_table, data_in, data_out) {
  for (i in 1:length(data_in)) {
    data_table[i, 2] <- get_profit(data_in[i], data_out[i])
  }
  
  profit <- data_table[1:length(data_out), 2]
  data_table[length(data_out) + 1, 2] <- sum(profit)
  data_table[length(data_out) + 2, 2] <- mean(profit)
  return(data_table)
}

# рассчитывает колонку "Реализация"
calc_selling <- function(data_table, data_out) {
  for (i in 1:length(data_out)) {
    data_table[i, 3] <- get_selling(data_out[i])
  }
  
  selling <- data_table[1:length(data_out), 3]
  data_table[length(data_out) + 1, 3] <- sum(selling)
  data_table[length(data_out) + 2, 3] <- mean(selling)
  return(data_table)
}

# рассчитывает колонку "Списание"
calc_utilization <- function(data_table, data_in, data_out) {
  for (i in 1:length(data_out)) {
    data_table[i, 4] <- get_utilization(data_in[i], data_out[i])
  }
  
  utilization <- data_table[1:length(data_out), 4]
  data_table[length(data_out) + 1, 4] <- sum(utilization)
  data_table[length(data_out) + 2, 4] <- mean(utilization)
  return(data_table)
}

# рассчитывает колонку "Равномерность продаж (sd)"
calc_uniformity_sales <- function(data_table, data_out) {
  for (i in 1:length(data_out)) {
    data_table[i, 5] <- round(sd(as.data.frame(data_out[i])[,2]), 1)
  }
  
  uniformity <- data_table[1:length(data_out), 5]
  data_table[length(data_out) + 1, 5] <- sum(uniformity)
  data_table[length(data_out) + 2, 5] <- round(mean(uniformity), 1)
  return(data_table)
}

# ============ вспомогательные функции для week_table ============ #


# ============ вспомогательные функции для day_table ============ #

find_max_sales <- function(data_table, data_out) {
  for (i in 1:length(data_out)) {
    data_frame = as.data.frame(data_out[i])
    data_table[i, 1] <- max(data_frame[2])
    data_table[i, 2] <- which.max(data_frame[[2]])
  }
  
  return(data_table)
}

find_min_sales <- function(data_table, data_out) {
  for (i in 1:length(data_out)) {
    data_frame = as.data.frame(data_out[i])
    data_table[i, 3] <- min(data_frame[2])
    data_table[i, 4] <- which.min(data_frame[[2]])
  }
  
  return(data_table)
}

find_max_utilization <- function(data_table, data_in, data_out) {
  for (i in 1:length(data_out)) {
    utilization <- as.data.frame(data_in[i])[2] - as.data.frame(data_out[i])[2]
    data_table[i, 5] <- max(utilization)
    data_table[i, 6] <- which.max(utilization[[1]])
  }
  
  return(data_table)
}

# ============ вспомогательные функции для day_table ============ #

if (F) {"
Выполняет анализ на основе in и out файлов и сохраняет итог в файле .csv

Для корректной работы функции данные должны быть в формате:
  store\\d+_in.txt и store\\d+_out.txt; count(*in.txt) == count(*out.txt)
  
params:
  path_to_data: путь к директории, в которой хранятся файлы *in.txt, *out.txt
  path_to_save: путь к директории, в которой будет сохранен итог анализа
  joined: если TRUE - сохраняет большую таблицу
  week: если TRUE - сохраняет таблицу за неделю
  day: если TRUE - сохраняет таблицу по дням
  "}
do_analysis_to_csv <- function(path_to_data, path_to_save = path_to_data,
                               joined = T, week = F, day = F) {
  
  files <- dir(path = path_to_data)
  store_names <- unique(unlist(strsplit(files, "_")))
  store_names <- store_names[grep("store*", store_names)]
  store_names <- sub("store", "Магазин ", store_names)
  
  data_in <- read.tables(paste0(path_to_data, "/", files[grep("*in.txt", files)]))
  data_out <- read.tables(paste0(path_to_data, "/", files[grep("*out.txt", files)]))
  
  week_table <- create.table(
    c("Выручка", "Прибыль", "Реализация",
      "Списание", "Равномерность продаж (sd)"),
    c(store_names, c("Итого", "Среднее"))
  )
  
  day_table <- create.table(
    c("Продажи макс", "День", "Продажи мин", "День",
      "Списание макс", "День"), store_names
  )
  
  week_table <- calc_revenue(week_table, data_out)
  week_table <- calc_profit(week_table, data_in, data_out)
  week_table <- calc_selling(week_table, data_out)
  week_table <- calc_utilization(week_table, data_in, data_out)
  week_table <- calc_uniformity_sales(week_table, data_out)
  
  day_table <- find_max_sales(day_table, data_out)
  day_table <- find_min_sales(day_table, data_out)
  day_table <- find_max_utilization(day_table, data_in, data_out)
  
  day_table_copy <- day_table
  day_table_copy[length(store_names) + 1, 1] <- NA
  day_table_copy[length(store_names) + 2, 1] <- NA
  joined_table <- cbind(week_table, day_table_copy)
  
  if (week) write.csv2(
    week_table, paste0(path_to_save, "/week_table.csv"))
  if (day) write.csv2(
    day_table, paste0(path_to_save, "/day_table.csv"))
  if (joined || (!week && !day && !joined)) write.csv2(
    joined_table,paste0(path_to_save, "/join.csv"))
}

do_analysis_to_csv("D:/RProjects/control-work/BSTBreadITWRLD/Анализ")

