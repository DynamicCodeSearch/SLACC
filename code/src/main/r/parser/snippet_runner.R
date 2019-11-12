# Title     : TODO
# Objective : TODO
# Created by: panzer
# Created on: 6/6/19

library(base)

INPUT_PATH = "/Users/panzer/Raise/ProgramRepair/CodeSeer/code/src/main/python/misconceptions/resources/titanic.csv"
OUTPUT_PATH = "/Users/panzer/Raise/ProgramRepair/CodeSeer/code/results/r_executed.csv"

executor <- function(snippet) {
    df = head(read.csv(INPUT_PATH), 10)
    res = eval(parse(text=snippet))
    # print(res)
    write.csv(res, OUTPUT_PATH)
}

# executor("summary(df)")
# executor("df$Survived")
# executor("df[,]")
# executor("substr(df$Cabin, 1, 1)")
# executor("ifelse(df$Survived > 0.5, 1, 0)")
# executor("table(df$Ticket)[df$Ticket]")
# executor("mean(df)")
# executor("df$Age")
# executor("prop.table(table(df$Survived))")
# executor("levels(df$Sex)")

train = read.csv(INPUT_PATH)
# print(train[is.na(train$Embarked)==TRUE, ])
print(train[train$Embarked == NA ])
# print(train[na.omit(train$Embarked !=NA),])