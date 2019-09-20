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

gen_func_r_3 <- function() {

    a = c(1.0, NaN, 3.0)
    b = c(4,5,6)
    df = data.frame(a, b)
    return(df[, -2]);
}
print(gen_func_r_3())
