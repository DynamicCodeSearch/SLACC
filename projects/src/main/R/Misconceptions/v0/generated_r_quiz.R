# Title     : TODO
# Objective : TODO
# Created by: panzer
# Created on: 4/2/19

library("dplyr")

gen_func_r_q1 <- function(df) {
    return(df[1:3]);
}

gen_func_r_q2a <- function(df) {
    return(df[0:3]);
}

gen_func_r_q2b <- function(df) {
    return(df[1:3, ]);
}

gen_func_r_q2c <- function(df) {
    return(df[0:2]);
}

# gen_func_r_q2d <- function(df) {
#     return(df[1:3, :]);
# }

gen_func_r_q3 <- function(df) {
    return(select(df, A:E));
}

gen_func_r_q4 <- function(df) {
    return(df[0:3, 1:2])
}

# gen_func_r_q5a <- function(df) {
#     return(df[:, 'A':'B'])
# }

gen_func_r_q5b <- function(df) {
    return(df[1:3, c('A','B')])
}

gen_func_r_q5c <- function(df) {
    return(df[['A', 'B']])
}

# gen_func_r_q5d <- function(df) {
#     return(df[:, c('A','B')])
# }

gen_func_r_q6 <- function(df) {
    return(df[['C']])
}

gen_func_r_q7a <- function(df) {
    return(df[!is.na(df$A)])
}

gen_func_r_q7b <- function(df) {
    return(df[~df.A.isna()])
}

gen_func_r_q7c <- function(df) {
    return(df[!is.na(df$A), ])
}

gen_func_r_q7d <- function(df) {
    return(df[, !is.na(df$A)])
}

gen_func_r_q8 <- function(df) {
    return(df[0:1])
}

gen_func_r_q9_1 <- function(df) {
    return(head(df))
}

gen_func_r_q9_2 <- function(df) {
    return(df$A)
}

gen_func_r_q9_3 <- function(df) {
    return(df[['A']])
}

gen_func_r_q9_2 <- function(df) {
    return(df$foo)
}
