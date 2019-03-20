# Title     : Dimension of DF
# Created by: panzer
# Created on: 3/14/19


library("dplyr")

gen_func_r_1 <- function(df) {
    return(dim(df));
}

gen_func_r_2 <- function(df) {
    return(select(df, col1, col2));
}
# print(f())
