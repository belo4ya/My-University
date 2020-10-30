read.tables <- function(files) {
  tables_list = list()
  for (i in 1:length(files)) {
    tables_list[i] <- list(read.table(files[i], header = TRUE, sep = ","))
  }
  return(tables_list)
}


create.table <- function(columns, rows) {
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
