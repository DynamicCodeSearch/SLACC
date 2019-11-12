# Title     : TODO
# Objective : TODO
# Created by: panzer
# Created on: 4/4/19

library("dplyr")
library("plyr")

abc = rep(c(2, NA, 5), 10)
s = rep(c("aa", "bb", "aa"), 10)
b = rep(c(TRUE, FALSE, TRUE), 10)
def = rep(c(4.1, 2.22, 3.4), 10)
df = data.frame(abc, s, b, def)
# print(df)
# print(head(df, 5))
# print(df[,'s'][1])
# print(substr(df$s, 0, 1))
# print(prop.table(table(df$abc)))
print(table(df$s))

