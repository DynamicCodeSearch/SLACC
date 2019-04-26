# Title     : TODO
# Objective : TODO
# Created by: panzer
# Created on: 3/26/19

library("base")

gen_func_r_dim <- function(df) {
    return(dim(df));
}


gen_func_r_col_names <- function(df) {
    index <- df$Group == 'Control'
    df[index,]$BloodPressure
}


gen_func_r_select <- function(df) {
 return(df[, c("col1", "col2")])
}