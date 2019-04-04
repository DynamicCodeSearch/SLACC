# Title     : TODO
# Objective : TODO
# Created by: panzer
# Created on: 3/26/19

library(base)
library(codetools)
library(rlang)

file_path = "/Users/panzer/Raise/ProgramRepair/CodeSeer/code/src/main/r/examples/sample_functions.R"

parse_library <- function(expression) {
  return(expression[[2]])
};


parse_assignment <- function(expression) {
    var_name = expression[[2]]
    # print(expression[[3]][[1]])
    func_obj = eval(expression[[3]])
    func_args = formals(func_obj)
    func_body = body(func_obj)
    print(findFuncLocals(func_args, func_body))
    print(typeof(func_obj))
}



parse_file <- function(f_path) {
    parsed = parse(f_path)
    for (i in as.list(parsed)) {
        if(i[[1]] == 'library') {
            print(parse_library(i))
        } else if (i[[1]] == '<-') {
            parse_assignment(i)
        }
        # walkCode(i)
        # print(expr(eval(i)))
        # print(typeof(expr(i)))
    }
}

parse_file(file_path)