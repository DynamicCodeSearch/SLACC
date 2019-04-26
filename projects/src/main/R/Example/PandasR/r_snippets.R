# Title     : Dimension of DF
# Created by: panzer
# Created on: 3/14/19


library("dplyr")

gen_func_r_dim <- function(df) {
    return(dim(df));
}

gen_func_r_head <- function(df) {
    return(head(df));
}

gen_func_r_slice <- function(df) {
    return(slice(df, 'col1':'col2'))
}

gen_func_r_filter <- function(df, a, b) {
    return(filter(df, col1 == a, col2 == b))
}

gen_func_r_and <- function(df) {
    return(df[df$col1 == 1 & df$col2 == 1,])
}

gen_func_r_select1 <- function(df) {
    return(select(df, "col1", "col2"));
}

gen_func_r_select2 <- function(df) {
    return(select(df, col1:col3));
}

gen_func_r_select3 <- function(df) {
    return(df[0:15, c("col1", "col2")])
}

gen_func_r_drop <- function(df) {
    return(select(df, -(col1:col3)));
}

gen_func_r_distinct1 <- function(df) {
    return(distinct(select(df, col1)));
}

gen_func_r_distinct2 <- function(df) {
    return(distinct(select(df, col1, col2)));
}

gen_func_r_sample <- function(df) {
    return(sample_n(df, 10));
}

gen_func_r_frac <- function(df) {
    return(sample_frac(df, 0.2));
}

gen_func_r_3 <- function(df) {
    return(df[1:2]);
}

gen_func_r_4 <- function(df) {
    return(select(df, 1:2))
}


gen_func_r_0_1_index <- function(df) {
    return(df[0:1])
}


#
#
# gen_func_r_x <- function() {
#     abc = c(2, 3, 5)
#     s = c("aa", "bb", "cc")
#     b = c(TRUE, FALSE, TRUE)
#     df = data.frame(abc, s, b)
#     print(df$abc)
#     # print(select(df, 1:2))
# }
#
# gen_func_r_x()