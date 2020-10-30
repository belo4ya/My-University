source("utils.R", encoding = "UTF-8")


PURCHASE_PRICE <- 18
SALE_PRICE <- 55
UTILIZATION_PRICE <- 10

ALL <- "ALL"
REVENUE <- "REVENUE"
PROFIT <- "PROFIT"
SELLING <- "SELLING"
UTILIZATION <- "UTILIZATION"
PROFITABILITY <- "PROFITABILITY"
UNIFORMITY <- "UNIFORMITY"


create.custom.table <- function(title,
                                rows,
                                cols,
                                ex_rows = c(),
                                ex_cols = c()) {
  n_stores <- length(rows)
  n_goods <- length(cols)
  matrix_table <- matrix(nrow = n_stores + length(ex_rows),
                         ncol = n_goods + 1 + length(ex_cols))
  matrix_table <- as.data.frame(matrix_table)
  
  colnames(matrix_table) <- c(title, cols, ex_cols)
  matrix_table[1] <- c(rows, ex_rows)
  
  return(matrix_table)
}


# =============================== GRAB DATA =============================== #

get.data.in <- function(path) {
  files <- dir(path)
  data_in <-
    read.tables(paste0(path, "/", files[grep("*in.txt", files)]))
  
  return(data_in)
}


get.data.out <- function(path) {
  files <- dir(path)
  data_out <-
    read.tables(paste0(path, "/", files[grep("*out.txt", files)]))
  
  return(data_out)
}


get.stores <- function(path) {
  files <- dir(path)
  stores <- unique(unlist(strsplit(files, "_")))
  stores <- stores[grep("store*", stores)]
  stores <- sub("store", "магазин ", stores)
  
  return(stores)
}


get.goods <- function(store_data) {
  goods <- colnames(store_data[[1]])
  goods <- goods[2:length(goods)]
  
  return(goods)
}


get.days <- function(store_data) {
  days <- store_data[[1]][, 1]
  
  return(days)
}

# ========================================================================== #


# ========================== ТАБЛИЦЫ ПО ПАРАМЕТРУ ========================== #

set.footer.param <- function(table, n_stores, n_goods) {
  for (i in 1:n_goods) {
    item <- table[, i + 1][1:n_stores]
    table[n_stores + 1, i + 1] <- sum(item)
    table[n_stores + 2, i + 1] <- round(mean(item))
    table[n_stores + 3, i + 1] <- round(median(item))
  }
  
  for (i in 1:n_stores) {
    store <- table[i,][(1 + 1):(n_goods + 1)]
    table[i, n_goods + 2] <- sum(store)
  }
  
  table[n_stores + 1, n_goods + 2] <-
    sum(table[n_stores + 1,][(1 + 1):(n_goods + 1)])
  
  return(table)
}


get.revenue.table <- function(data_in, data_out, stores, goods) {
  title = "ВЫРУЧКА"
  n_stores <- length(stores)
  n_goods <- length(goods)
  revenue_table <- create.custom.table(title,
                                       stores,
                                       goods,
                                       c("ИТОГ", "СРЕДНЕЕ", "МЕДИАНА"),
                                       c("ИТОГ"))
  
  for (i in 1:n_stores) {
    for (j in 1:n_goods) {
      revenue_table[i, j + 1] <- sum(data_out[[i]][j + 1]) * SALE_PRICE
    }
  }
  
  revenue_table <-
    set.footer.param(revenue_table, n_stores, n_goods)
  
  return(revenue_table)
}


get.profit.table <- function(data_in, data_out, stores, goods) {
  title = "ПРИБЫЛЬ"
  n_stores <- length(stores)
  n_goods <- length(goods)
  profit_table <- create.custom.table(title,
                                      stores,
                                      goods,
                                      c("ИТОГ", "СРЕДНЕЕ", "МЕДИАНА"),
                                      c("ИТОГ"))
  
  for (i in 1:n_stores) {
    for (j in 1:n_goods) {
      profit_table[i, j + 1] <-
        (
          sum(data_out[[i]][j + 1]) * SALE_PRICE -             # Будем считать,
            sum(data_in[[i]][j + 1]) * PURCHASE_PRICE -       # что это просто
            (sum(data_in[[i]][j + 1]) -                       # страшная регулярка
               sum(data_out[[i]][j + 1])) * UTILIZATION_PRICE
        )
    }
  }
  
  profit_table <- set.footer.param(profit_table, n_stores, n_goods)
  
  return(profit_table)
}


get.selling.table <- function(data_in, data_out, stores, goods) {
  title = "ОБЪЕМ_ПРОДАЖ"
  n_stores <- length(stores)
  n_goods <- length(goods)
  selling_table <- create.custom.table(title,
                                       stores,
                                       goods,
                                       c("ИТОГ", "СРЕДНЕЕ", "МЕДИАНА"),
                                       c("ИТОГ"))
  
  for (i in 1:n_stores) {
    for (j in 1:n_goods) {
      selling_table[i, j + 1] <- sum(data_out[[i]][j + 1])
    }
  }
  
  selling_table <-
    set.footer.param(selling_table, n_stores, n_goods)
  
  return(selling_table)
}


get.utilization.table <-
  function(data_in, data_out, stores, goods) {
    title = "СПИСАНИЕ"
    n_stores <- length(stores)
    n_goods <- length(goods)
    utilization_table <- create.custom.table(title,
                                             stores,
                                             goods,
                                             c("ИТОГ", "СРЕДНЕЕ", "МЕДИАНА"),
                                             c("ИТОГ"))
    
    for (i in 1:n_stores) {
      for (j in 1:n_goods) {
        utilization_table[i, j + 1] <- (sum(data_in[[i]][j + 1]) -
                                          sum(data_out[[i]][j + 1]))
      }
    }
    
    utilization_table <-
      set.footer.param(utilization_table, n_stores, n_goods)
    
    return(utilization_table)
  }


get.profitability.table <-
  function(data_in, data_out, stores, goods) {
    title = "РЕНТАБЕЛЬНОСТЬ"
    n_stores <- length(stores)
    n_goods <- length(goods)
    profitability_table <- create.custom.table(title,
                                               stores,
                                               goods,
                                               c("СРЕДНЕЕ", "МЕДИАНА"),
                                               c("СРЕДНЕЕ", "МЕДИАНА"))
    
    for (i in 1:n_stores) {
      for (j in 1:n_goods) {
        profit <- (
          sum(data_out[[i]][j + 1]) * SALE_PRICE -
            sum(data_in[[i]][j + 1]) * PURCHASE_PRICE -
            (sum(data_in[[i]][j + 1]) -
               sum(data_out[[i]][j + 1])) * UTILIZATION_PRICE
        )
        revenue <- sum(data_out[[i]][j + 1]) * SALE_PRICE
        profitability_table[i, j + 1] <-
          round(profit / revenue * 100, 1)
      }
    }
    
    for (i in 1:n_goods) {
      item <- profitability_table[, i + 1][1:n_stores]
      # СРЕДНЕЕ
      profitability_table[n_stores + 1, i + 1] <- round(mean(item))
      # МЕДИАНА
      profitability_table[n_stores + 2, i + 1] <- round(median(item))
    }
    
    for (i in 1:n_stores) {
      store <- as.numeric(profitability_table[i,][(1 + 1):(n_goods + 1)])
      # СРЕДНЕЕ
      profitability_table[i, n_goods + 1 + 1] <- round(mean(store))
      # МЕДИАНА
      profitability_table[i, n_goods + 2 + 1] <- round(median(store))
    }
    
    return(profitability_table)
  }


get.uniformity.sales.table <-
  function(data_in, data_out, stores, goods) {
    title = "РАВНОМЕРНОСТЬ ПРОДАЖ (SD)"
    n_stores <- length(stores)
    n_goods <- length(goods)
    uniformity_sales_table <-
      create.custom.table(title,
                          stores,
                          goods,
                          c("СРЕДНЕЕ", "МЕДИАНА"),
                          c("СРЕДНЕЕ", "МЕДИАНА"))
    
    for (i in 1:n_stores) {
      for (j in 1:n_goods) {
        uniformity_sales_table[i, j + 1] <-
          round(sd(data_out[[i]][j + 1][, 1]), 1)
      }
    }
    
    for (i in 1:n_goods) {
      item <- uniformity_sales_table[, i + 1][1:n_stores]
      # СРЕДНЕЕ
      uniformity_sales_table[n_stores + 1, i + 1] <- round(mean(item))
      # МЕДИАНА
      uniformity_sales_table[n_stores + 2, i + 1] <-
        round(median(item))
    }
    
    for (i in 1:n_stores) {
      store <-
        as.numeric(uniformity_sales_table[i,][(1 + 1):(n_goods + 1)])
      # СРЕДНЕЕ left
      uniformity_sales_table[i, n_goods + 1 + 1] <- round(mean(store))
      # МЕДИАНА left
      uniformity_sales_table[i, n_goods + 2 + 1] <-
        round(median(store))
    }
    
    return(uniformity_sales_table)
  }

# ========================================================================= #


# ========================== ТАБЛИЦЫ ПО МАГАЗИНУ ========================== #

set.footer.store <- function(table, n_days, n_goods) {
  for (i in 1:n_goods) {
    item <- table[, i + 1][1:n_days]
    table[n_days + 1, i + 1] <- round(sum(item))
    table[n_days + 2, i + 1] <- round(mean(item))
    table[n_days + 3, i + 1] <- round(median(item))
  }
  
  for (i in 1:n_days) {
    store <- as.numeric(table[i,][(1 + 1):(n_goods + 1)])
    table[i, n_goods + 1 + 1] <- round(sum(store))
    table[i, n_goods + 2 + 1] <- round(mean(store))
    table[i, n_goods + 3 + 1] <- round(median(store))
  }
  
  table[n_days + 1, n_goods + 2] <-
    sum(table[n_days + 1,][(1 + 1):(n_goods + 1)])
  
  return(table)
}


get.revenue.table.by.store <- function(n, path_to_data) {
  data_in <- get.data.in(path_to_data)
  data_out <- get.data.out(path_to_data)
  
  days <- get.days(data_out)
  goods <- get.goods(data_out)
  
  data_in <- data_in[[n]]
  data_out <- data_out[[n]]
  
  n_days <- length(days)
  n_goods <- length(goods)
  
  stores <- get.stores(path_to_data)
  title = paste0(stores[n], " & ", "ВЫРУЧКА")
  
  revenue_table <-
    create.custom.table(
      title,
      paste("день", days),
      goods,
      c("ИТОГ", "СРЕДНЕЕ", "МЕДИАНА"),
      c("ИТОГ", "СРЕДНЕЕ", "МЕДИАНА")
    )
  
  for (i in 1:n_days) {
    for (j in 1:n_goods) {
      revenue_table[i, j + 1] <- data_out[i, j + 1] * SALE_PRICE
    }
  }
  
  revenue_table <- set.footer.store(revenue_table, n_days, n_goods)
  
  return(revenue_table)
}


get.profit.table.by.store <- function(n, path_to_data) {
  data_in <- get.data.in(path_to_data)
  data_out <- get.data.out(path_to_data)
  
  days <- get.days(data_out)
  goods <- get.goods(data_out)
  
  data_in <- data_in[[n]]
  data_out <- data_out[[n]]
  
  n_days <- length(days)
  n_goods <- length(goods)
  
  stores <- get.stores(path_to_data)
  title = paste0(stores[n], " & ", "ПРИБЫЛЬ")
  
  profit_table <-
    create.custom.table(
      title,
      paste("день", days),
      goods,
      c("ИТОГ", "СРЕДНЕЕ", "МЕДИАНА"),
      c("ИТОГ", "СРЕДНЕЕ", "МЕДИАНА")
    )
  
  for (i in 1:n_days) {
    for (j in 1:n_goods) {
      profit_table[i, j + 1] <- (
        data_out[i, j + 1] * SALE_PRICE -
          data_in[i, j + 1] * PURCHASE_PRICE -
          (data_in[i, j + 1] -
             data_out[i, j + 1]) * UTILIZATION_PRICE
      )
    }
  }
  
  profit_table <- set.footer.store(profit_table, n_days, n_goods)
  
  return(profit_table)
}


get.selling.table.by.store <- function(n, path_to_data) {
  data_in <- get.data.in(path_to_data)
  data_out <- get.data.out(path_to_data)
  
  days <- get.days(data_out)
  goods <- get.goods(data_out)
  
  data_in <- data_in[[n]]
  data_out <- data_out[[n]]
  
  n_days <- length(days)
  n_goods <- length(goods)
  
  stores <- get.stores(path_to_data)
  title = paste0(stores[n], " & ", "ОБЪЕМ_ПРОДАЖ")
  
  selling_table <-
    create.custom.table(
      title,
      paste("день", days),
      goods,
      c("ИТОГ", "СРЕДНЕЕ", "МЕДИАНА"),
      c("ИТОГ", "СРЕДНЕЕ", "МЕДИАНА")
    )
  
  for (i in 1:n_days) {
    for (j in 1:n_goods) {
      selling_table[i, j + 1] <- data_out[i, j + 1]
    }
  }
  
  selling_table <- set.footer.store(selling_table, n_days, n_goods)
  
  return(selling_table)
}


get.utilization.table.by.store <- function(n, path_to_data) {
  data_in <- get.data.in(path_to_data)
  data_out <- get.data.out(path_to_data)
  
  days <- get.days(data_out)
  goods <- get.goods(data_out)
  
  data_in <- data_in[[n]]
  data_out <- data_out[[n]]
  
  n_days <- length(days)
  n_goods <- length(goods)
  
  stores <- get.stores(path_to_data)
  title = paste0(stores[n], " & ", "СПИСАНИЕ")
  
  utilization_table <-
    create.custom.table(
      title,
      paste("день", days),
      goods,
      c("ИТОГ", "СРЕДНЕЕ", "МЕДИАНА"),
      c("ИТОГ", "СРЕДНЕЕ", "МЕДИАНА")
    )
  
  for (i in 1:n_days) {
    for (j in 1:n_goods) {
      utilization_table[i, j + 1] <-
        data_in[i, j + 1] - data_out[i, j + 1]
    }
  }
  
  utilization_table <-
    set.footer.store(utilization_table, n_days, n_goods)
  
  return(utilization_table)
}


get.profitability.table.by.store <- function(n, path_to_data) {
  data_in <- get.data.in(path_to_data)
  data_out <- get.data.out(path_to_data)
  
  days <- get.days(data_out)
  goods <- get.goods(data_out)
  
  data_in <- data_in[[n]]
  data_out <- data_out[[n]]
  
  n_days <- length(days)
  n_goods <- length(goods)
  
  stores <- get.stores(path_to_data)
  title = paste0(stores[n], " & ", "РЕНТАБЕЛЬНОСТЬ")
  
  profitability_table <-
    create.custom.table(title,
                        paste("день", days),
                        goods,
                        c("СРЕДНЕЕ", "МЕДИАНА"),
                        c("СРЕДНЕЕ", "МЕДИАНА"))
  
  for (i in 1:n_days) {
    for (j in 1:n_goods) {
      profit <- (
        data_out[i, j + 1] * SALE_PRICE -
          data_in[i, j + 1] * PURCHASE_PRICE -
          (data_in[i, j + 1] -
             data_out[i, j + 1]) * UTILIZATION_PRICE
      )
      revenue <- data_out[i, j + 1] * SALE_PRICE
      profitability_table[i, j + 1] <-
        round(profit / revenue * 100, 1)
    }
  }
  
  for (i in 1:n_goods) {
    item <- profitability_table[, i + 1][1:n_days]
    profitability_table[n_days + 1, i + 1] <- round(mean(item))
    profitability_table[n_days + 2, i + 1] <- round(median(item))
  }
  
  for (i in 1:n_days) {
    store <- as.numeric(profitability_table[i,][(1 + 1):(n_goods + 1)])
    profitability_table[i, n_goods + 1 + 1] <- round(mean(store))
    profitability_table[i, n_goods + 2 + 1] <- round(median(store))
  }
  
  return(profitability_table)
}

# ========================================================================= #

if (F) {
  "
Пользовательский интерфейс для получения подробного анализа по указанным параметрам

Для корректной работы функции данные должны быть в формате:
  store\\d+_in.txt и store\\d+_out.txt; count(*in.txt) == count(*out.txt)

params:
  path_to_data: путь к директории, в которой хранятся файлы *in.txt, *out.txt
  path_to_save: путь к директории, в которой будет сохранен итог анализа.
  По умолчанию path_to_save = path_to_data
  filters: позволяет указать только определенные параметры анализа.
  По умолчанию filters = 'all' ('REVENUE', 'PROFIT', 'SELLING',
  'UTILIZATION', 'PROFITABILITY', 'UNIFORMITY') - регистр игнорируется
  w: если TRUE - записывает итог анализа на диск и возвращает, полученные таблицы.
  Если w = FALSE - возвращает, полученные таблицы.
  "
}
get.analysis.by.param <-
  function(path_to_data,
           path_to_save = path_to_data,
           filters = ALL,
           w = F) {
    tables <- list()
    filters <- toupper(filters)
    if (filters[1] == ALL) {
      filters[1:6] <-
        c(REVENUE,
          PROFIT,
          SELLING,
          UTILIZATION,
          PROFITABILITY,
          UNIFORMITY)
    }
    
    data_in <- get.data.in(path_to_data)
    data_out <- get.data.out(path_to_data)
    
    stores <- get.stores(path_to_data)
    goods <- get.goods(data_out)
    
    if (REVENUE %in% filters) {
      tables[REVENUE] <-
        list(get.revenue.table(data_in, data_out, stores, goods))
    }
    
    if (PROFIT %in% filters) {
      tables[PROFIT] <-
        list(get.profit.table(data_in, data_out, stores, goods))
    }
    
    if (SELLING %in% filters) {
      tables[SELLING] <-
        list(get.selling.table(data_in, data_out, stores, goods))
    }
    
    if (UTILIZATION %in% filters) {
      tables[UTILIZATION] <-
        list(get.utilization.table(data_in, data_out, stores, goods))
    }
    
    if (PROFITABILITY %in% filters) {
      tables[PROFITABILITY] <-
        list(get.profitability.table(data_in, data_out, stores, goods))
    }
    
    if (UNIFORMITY %in% filters) {
      tables[UNIFORMITY] <-
        list(get.uniformity.sales.table(data_in, data_out, stores, goods))
    }
    
    if (!w) {
      return(tables)
    }
    
    path_to_save = paste0(path_to_save, "/", "итог")
    dir.create(path_to_save)
    
    for (i in 1:length(tables)) {
      write.csv2(tables[[filters[i]]],
                 paste0(path_to_save, "/", tolower(filters[i]), ".csv"),
                 row.names = F)
    }
    
    return(tables)
  }


if (F) {
  "
Пользовательский интерфейс для получения подробного анализа по магазину

Для корректной работы функции данные должны быть в формате:
  store\\d+_in.txt и store\\d+_out.txt; count(*in.txt) == count(*out.txt)

params:
  n: номер магазина
  path_to_data: путь к директории, в которой хранятся файлы *in.txt, *out.txt
  path_to_save: путь к директории, в которой будет сохранен итог анализа.
  По умолчанию path_to_save = path_to_data
  filters: позволяет указать только определенные параметры анализа.
  По умолчанию filters = 'all' ('REVENUE', 'PROFIT', 'SELLING',
  'UTILIZATION', 'PROFITABILITY') - регистр игнорируется
  w: если TRUE - записывает итог анализа на диск и возвращает, полученные таблицы.
  Если w = FALSE - возвращает, полученные таблицы.
  "
}
get.analysis.by.store <-
  function(n,
           path_to_data,
           path_to_save = path_to_data,
           filters = ALL,
           w = F) {
    tables <- list()
    filters <- toupper(filters)
    if (filters[1] == ALL) {
      filters[1:5] <-
        c(REVENUE, PROFIT, SELLING, UTILIZATION, PROFITABILITY)
    }
    
    if (REVENUE %in% filters) {
      tables[REVENUE] <- list(get.revenue.table.by.store(n, path_to_data))
    }
    
    if (PROFIT %in% filters) {
      tables[PROFIT] <- list(get.profit.table.by.store(n, path_to_data))
    }
    
    if (SELLING %in% filters) {
      tables[SELLING] <- list(get.selling.table.by.store(n, path_to_data))
    }
    
    if (UTILIZATION %in% filters) {
      tables[UTILIZATION] <-
        list(get.utilization.table.by.store(n, path_to_data))
    }
    
    if (PROFITABILITY %in% filters) {
      tables[PROFITABILITY] <-
        list(get.profitability.table.by.store(n, path_to_data))
    }
    
    if (!w) {
      return(tables)
    }
    
    store_name <- unlist(strsplit(colnames(tables[[1]])[1], " "))
    store_name <- paste0(store_name[1], store_name[2])
    path_to_save = paste0(path_to_save, "/", store_name)
    dir.create(path_to_save)
    
    for (i in 1:length(tables)) {
      write.csv2(tables[[filters[i]]],
                 paste0(path_to_save, "/", tolower(filters[i]), ".csv"),
                 row.names = F)
    }
    
    return(tables)
  }
