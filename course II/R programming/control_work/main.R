setwd("./")
source("generate_data.R", encoding = "utf-8")
source("analysisV2.R", encoding = "utf-8")
source("visualizationV2.R", encoding = "utf-8")


# -------------- SETTINGS --------------- #
setwd("./BSTBreadITWRLD")

store_name = "Магазин"
store_count = 8
days = 30
goods = c("хлеб_ч",
          "хлеб_ч_н",
          "хлеб_б",
          "хлеб_б_н")


# ------------- CREATE DATA ------------- #
for (i in 1:store_count) {
  store = paste0("./", store_name ,i)
  dir.create(store)
  
  gen.supply(paste0(store, "/"), days = days, goods = goods)
  
  sale_level = tryhard.random(60, 95, length(goods))
  print(paste0("sale_level: ", paste0(sale_level, collapse = ", ")))
  gen.sale(paste0(store, "/"), days = days, goods = goods, sale_level = sale_level)
}


# -------------- GRAB DATA -------------- #
# cmd.exe
# select.bat store_count


# ------------ ANALYSIS DATA ------------ #
analysis <- get.analysis.by.param("./Анализ", w = T)
store5 <- get.analysis.by.store(5, "./Анализ", w = T)
store6 <- get.analysis.by.store(6, "./Анализ", w = T)
store7 <- get.analysis.by.store(7, "./Анализ", w = T)


# ------------ VISUALIZATION DATA ------------ #
plot.scatter.plot.by.params(store5, 
                            goods[1],
                            path_to_save = "./Анализ/магазин005/")
plot.scatter.plot.by.params(store6,
                            goods[2],
                            c(REVENUE, PROFIT),
                            path_to_save = "./Анализ/магазин006/")
plot.scatter.plot.by.params(store7,
                            goods[4],
                            c(SELLING, UTILIZATION),
                            path_to_save = "./Анализ/магазин007/")

plot.trend.lines.by.store(store5$PROFIT, 
                          path_to_save = "./Анализ/магазин005/", 
                          goods = goods[2],
                          v = T)
plot.trend.lines.by.store(store5$SELLING, 
                          path_to_save = "./Анализ/магазин005/", 
                          goods = goods[c(1, 3)])
plot.trend.lines.by.store(store5$UTILIZATION, 
                          path_to_save = "./Анализ/магазин005/", 
                          goods = goods[c(1, 4)])

plot.trend.lines.by.store(store6$SELLING, 
                          path_to_save = "./Анализ/магазин006/", 
                          goods = goods[1:4])

plot.trend.lines.by.store(store7$UTILIZATION, 
                          path_to_save = "./Анализ/магазин007/", 
                          goods = goods[1:2])


plot.trend.lines.by.product(store5, 
                            goods[3],
                            path_to_save = "./Анализ/магазин005/")
plot.trend.lines.by.product(store5, 
                            goods[1],
                            path_to_save = "./Анализ/магазин005/",
                            c(SELLING, UTILIZATION, PROFITABILITY))
plot.trend.lines.by.product(store5, 
                            goods[1],
                            path_to_save = "./Анализ/магазин005/",
                            c(PROFIT, REVENUE))

plot.trend.lines.by.product(store6, 
                            goods[1],
                            path_to_save = "./Анализ/магазин006/",
                            c(PROFIT, REVENUE))

plot.trend.lines.by.product(store7, 
                            goods[4],
                            path_to_save = "./Анализ/магазин007/",
                            c(SELLING, UTILIZATION))


plot.store.sum(store5, "./Анализ/магазин005/")
plot.store.sum(store6, "./Анализ/магазин006/")
plot.store.sum(store7, "./Анализ/магазин007/")

plot.revenue.stores(analysis$SELLING, 1, "./Анализ/итог/")

stores <- list()
for (i in 1:store_count) {
  stores[i] <- list(get.analysis.by.store(i, "./Анализ", filters = SELLING))
}

plot.revenue.stores.goods(stores, c(1:4), "./Анализ/итог/")
plot.revenue.stores.goods(stores, c(1:3), "./Анализ/итог/")
