clear.table <- function(table, del_row = c("ИТОГ", "СРЕДНЕЕ", "МЕДИАНА"), 
                           del_col = del_row) {
  
  return(table[!(table[, 1] %in% del_row),
               !(colnames(table) %in% del_col)])
}


# ========================== ПО ОДНОМУ МАГАЗИНУ ========================== # 

plot.trend.lines.by.store <- function(data_table, path_to_save = "./", 
                                      goods = NULL, v = F) {
  data_table <- clear.table(data_table)
  
  main <- unlist(strsplit(colnames(data_table)[1], " "))
  main <- main[length(main)]
  
  data_table <- clear.table(data_table, del_col = colnames(data_table)[1])
  
  if (is.null(goods)) goods <- colnames(data_table)

  days <- c(1:length(data_table[, 1]))
  
  xrange <- range(days)
  yrange <- range(data_table[goods])
  
  png(paste0(path_to_save, "/", tolower(main), "_", paste0(goods, collapse = "_"), ".png"), 
      pointsize = 15)
  
  plot(xrange,
       yrange,
       type="n",
       main=main,
       xlab="День",
       ylab="",
       cex.axis=0.8,
       cex.lab=0.7,
       cex.main=0.9,
       col.lab = "grey50",
       fg = "grey40")
  
  grid()
  pol <- rainbow(length(goods))
  
  for (i in 1:length(goods)) {
    points(days, data_table[goods[i]][, 1], pch=20, col=pol[i])
    lines(days, data_table[goods[i]][, 1], pch=20, col=pol[i])
    
    if (v) {
      text(days, 
           data_table[goods[i]][, 1],
           labels = data_table[goods[i]][, 1],
           cex = 0.75,
           pos = 3)
    }
  }
  
  par(xpd=TRUE)
  legend(x = "topright",
         legend = goods,
         inset = c(-0.0, -0.175),
         title = "Товар",
         fill = pol[1:length(goods)],
         cex = 0.6,
         col = rgb(1, 1, 1, 0),
         border = rgb(1, 1, 1, 0),
         bg = rgb(1, 1, 1, 1),
         box.col = rgb(1, 1, 1, 0))
  
  dev.off()
}


plot.trend.lines.by.product <- function(data_tables, product, path_to_save = "./", 
                                        params = NULL, v = F) {
  if (is.null(params)) {
    params <- c(REVENUE, PROFIT, SELLING, UTILIZATION, PROFITABILITY)
  }
  
  product <- tolower(product)
  data_tables <- data_tables[params]
  
  legend_params <- c()
  product_data <- list()
  for (i in 1:length(data_tables)) {
    data_table <- data_tables[[i]]
    data_table <- clear.table(data_table)
    
    legend_param <- unlist(strsplit(colnames(data_table)[1], " "))
    legend_params[i] <- tolower(legend_param[length(legend_param)])
    
    data_table <- clear.table(data_table, del_col = colnames(data_table)[1])
    
    if (i == 1) days <- c(1:length(data_table[, 1]))
    
    product_data[i] <- data_table[product]
  }
  
  xrange <- range(days)
  yrange <- range(product_data)
  
  png(paste0(path_to_save, "/", tolower(product), "_", paste0(legend_params, collapse = "_"),
             ".png"), pointsize = 15)
  
  plot(xrange,
       yrange,
       type="n",
       main=toupper(product),
       xlab="День",
       ylab="",
       cex.axis=0.8,
       cex.lab=0.7,
       cex.main=0.9,
       col.lab = "grey50",
       fg = "grey40")
  
  grid()
  pol <- rainbow(length(params))
  
  for (i in 1:length(params)) {
    points(days, product_data[[i]], pch=20, col=pol[i])
    lines(days, product_data[[i]], pch=20, col=pol[i])
    
    if (v) {
      text(days, 
           product_data[[i]],
           labels = product_data[[i]],
           cex = 0.75,
           pos = 3)
    }
  }
  
  par(xpd=TRUE)
  legend(x = "topright",
         legend = legend_params,
         inset = c(-0.0, -0.175),
         title = "Параметр", 
         fill = pol[1:length(params)],
         cex = 0.6, 
         col = rgb(1, 1, 1, 0), 
         border = rgb(1, 1, 1, 0),
         bg = rgb(1, 1, 1, 1), 
         box.col = rgb(1, 1, 1, 0))
  
  dev.off()
}


plot.scatter.plot.by.params <- function(data_tables, product, 
                                        params = c(UTILIZATION, SELLING),
                                        path_to_save = "./") {
  params <- params[1:2]
  product <- tolower(product)
  data_tables <- data_tables[params]
  
  axis_params <- c()
  axis_data <- list()
  for (i in 1:length(data_tables)) {
    data_table <- data_tables[[i]]
    data_table <- clear.table(data_table)
    
    axis_param <- unlist(strsplit(colnames(data_table)[1], " "))
    axis_params[i] <- tolower(axis_param[length(axis_param)])
    
    data_table <- clear.table(data_table, del_col = colnames(data_table)[1])
    
    axis_data[i] <- data_table[product]
  }
  
  png(paste0(path_to_save, "/", tolower(product), "_", paste0(axis_params, collapse = "_"),
             ".png"), pointsize = 15)
  
  plot(axis_data[[1]],
       axis_data[[2]],
       main = toupper(product),
       xlab = axis_params[1],
       ylab = axis_params[2],
       cex.axis = 0.8,
       cex.lab = 0.7,
       cex.main = 0.9,
       col = "red",
       col.lab = "grey50",
       fg = "grey40")
  
  grid()
  dev.off()
}


plot.store.sum <- function(store, path_to_save = "./") {
  for (i in c(REVENUE, PROFIT, SELLING, UTILIZATION)) {
    param <- store[[i]]
    products <- c()
    results <- c()
    
    main <- unlist(strsplit(colnames(param)[1], " "))
    main <- tolower(main[length(main)]) 
    
    for (j in c(2:(length(param) - 3))) {
      products[j - 1] <- colnames(param[j])
      results[j - 1] <- param[length(param[, 1]) - 2, j]
    }
    png(paste0(path_to_save, "/", tolower(i), ".png"), pointsize = 15)

    barplot(results,
            names.arg = products,
            main = toupper(main),
            col = c(2:(length(products) + 1)),
            space = 2,
            axes = F,
            cex.axis = 0.8,
            cex.lab = 0.7,
            cex.main = 0.9,
            col.lab = "grey50",
            fg = "grey40")
    grid()
    
    if (i %in% c(SELLING, UTILIZATION)) {
      axis(2, at = seq(ifelse(min(results) < 0, min(results), 0), max(results), by = 100),
           labels = seq(ifelse(min(results) < 0, min(results), 0), max(results), by = 100))
    } else {
      axis(2, at = seq(ifelse(min(results) < 0, min(results), 0), max(results), by = 10000),
           labels = seq(ifelse(min(results) < 0, min(results), 0), max(results), by = 10000))
    }
    
    dev.off()
  }
}

# ========================== ПО ОДНОМУ МАГАЗИНУ ========================== #


# ==================== ПО НЕСКОЛЬКИМ (ВСЕМ) МАГАЗИНАМ ==================== #

plot.revenue.stores <- function(revenue, n = 1, path_to_save = "./") {
  stores <- revenue[, 1][1:(length(revenue[, 1]) - 3)]
  results <- c()
  for (i in 1:length(stores)) {
    results[i] <- revenue[i, n + 1]
  }
  png(paste0(path_to_save, "/объем_продаж.png"))
  
  par(mar = c(5, 8, 4, 2))
  barplot(results,
          names.arg = stores,
          main = "Объем продаж",
          col = c(2:(length(stores) + 1)),
          horiz = T,
          las = 1,
          axes = F,
          cex.axis = 0.8,
          cex.lab = 0.7, 
          cex.main = 0.9,
          col.lab = "grey50",
          fg = "grey40")
  axis(1, at = seq(0, max(results), by = 100),
       labels = seq(0, max(results), by = 100))
  grid(15, 0)
  dev.off()
}


plot.revenue.stores.goods <- function(stores, goods = c(1, 2), path_to_save = "./") {
  stores_names <- c()
  goods_names <- c()
  for (i in 1:length(stores)) {
    store <- stores[[i]][[SELLING]]
    stores_names[i] <- paste("магазин", i)
    for (j in 1:length(goods)) {
      goods_names[j] <- colnames(store)[goods[j] + 1]
    }
  }

  m <- matrix(nrow = length(stores_names), ncol = length(goods_names))
  colnames(m) <- goods_names
  row.names(m) <- stores_names
  for (i in 1:length(stores)) {
    store <- stores[[i]][[SELLING]]
    for (j in 1:length(goods)) {
      m[i, j] <- store[length(store[, 1]) - 2,goods[j] + 1]
    }
  }
  m <- t(m)
  png(paste0(path_to_save, "/selling_", paste0(goods_names, collapse = "_"), ".png"))
  
  par(mar = c(5, 8, 4, 2))
  barplot(m,
          beside = TRUE,
          col = topo.colors(length(goods)),
          legend.text = rownames(m),
          xlab = "Продано, шт.",
          ylab = "",
          horiz = T,
          las = 1,
          axes = F,
          cex.axis = 0.8,
          cex.lab = 0.7, 
          cex.main = 0.9,
          col.lab = "grey50",
          fg = "grey40")
  
  axis(1, at = seq(0, max(m) + 1000, by = 100),
       labels = seq(0, max(m) + 1000, by = 100))
  grid(15, 0)
  
  dev.off()
}

# ==================== ПО НЕСКОЛЬКИМ (ВСЕМ) МАГАЗИНАМ ==================== #
