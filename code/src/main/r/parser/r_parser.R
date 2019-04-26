# Title     : TODO
# Objective : TODO
# Created by: panzer
# Created on: 3/26/19

library(base)

global_funcs <- c("arrange","auto_copy","all_equal","add_rownames","compute","copy_to","coalesce","case_when","bind","common_by","between","cumall","dim_desc","explain","desc","distinct","failwith","group_by_prepare","filter","id","groups","group_indices","if_else","join","join.tbl_df","group_size","grouped_df","group_by","lead-lag","make_tbl","mutate","n","n_distinct","lazy_ops","na_if","location","named_commas","nth","ranking","partial_eval","recode","query","order_by","near","slice","rowwise","select","select_vars","sample","select_if","tbl_df","summarise_each","tally","summarise_all","src_tbls","summarise","with_order","tbl","vars","top_n","bind_rows","MathFun","Reserved","Foreign","Last.value","NumericConstants","Ops.Date","ISOdatetime","RdUtils","Recall","Hyperbolic","Sys.glob","Sys.info","Cstack_info","UseMethod","Rhome","DateTimeClasses","Extract.data.frame","Extract.factor","log","Sys.localeconv","Sys.readlin","Memory-limits","Memory","Primitive","Logic","Quotes","Internal","Constants","Paren","NA",".Platform","Round","agrep","NULL","Sys.sleep","Sys.time","Special","all","Sys.getenv","Syntax","Sys.getpid","as.Date","Startup","append","assignOps","apply","Sys.which","Control","Vectorize","as.POSIX*","as.function","all.equal","attr","Trig","all.names","Extremes","attributes","attach","assign","any","as.environment","as.data.frame","basename","base-defunct","base-deprecated","aperm",".bincode","base-internal","base-package","Foreign-internal","chol2inv","cat","class","browserText","browser","cbind","bindenv","bitwise","Random","Random.user","Sys.setFileTime","Sys.setenv","contributors","connections","char.expand","R.Version","abbreviate","character","args","array","callCC","autoload","backsolve","date","conditions","dcf","conflicts","deparse","data.matrix","deparseOpts","capabilities","dataframeHelpers","builtins","body","do.call","bquote","dontCheck","eapply","by","c","duplicated","call","dyn.load","chkDots","chol","eigen","file.info","debug","delayedAssign","col","charmatch","chartr","dim","dimnames","files2","colSums","eval","exists","row+colnames","file.path","find.package","getDLLRegisteredRoutines","comment","copyright","complex","commandArgs","formatC","data.class","function","crossprod","funprog","data.frame","file.show","files","findInterval","diff","gc","force","cumsum","difftime","dots","getLoadedDLLs","groupGeneric","curlGetHeaders","cut.POSIXt","interaction","interactive","grouping","double","identical","gc.time","gctorture","expand.grid","identity","cut","kappa","grep","grepRaw","expression","extSoftVersion","factor","det","kronecker","lapply","forceAndCall","lazyLoad","is.function","list2env","formals","is.language","detach",".Device","dput","drop","encodeString","is.object","isSymmetric","diag","jitter","is.recursive","get","load","levels","mat.or.vec","match.fun","libPaths","getCallingDLL","match","list","mean","environment","droplevels","file.access","memCompress","list.files","matmult","file.choose","gzcon","names","noquote","nargs","hexmode","make.names","pmatch","is.R","make.unique","isS4","polyroot","memory.profile","dump","format.pval","norm","formatDL","ns-topenv","l10n_info","merge","prop.table","getwd","normalizePath","numeric","NotYet","labels","ns-hooks","ns-internals","pushBack","license","print","gl","parse","match.arg","match.call","format","ifelse","paste","quit","format.info","range","regex","regmatches","print.data.frame","mode","remove","integer","readChar","round.POSIXt","getNativeSymbolInfo","rowsum","seq.Date","readLines","rev","seq.POSIXt","rle","gettext","is.single","sQuote","is.unsorted","row","iconv","row.names","icuSetCollate","libcurlVersion","invisible","is.finite","name","length","lengths","search","sprintf","seq","locales","logical","on.exit","srcfile","seek","sequence","mapply","lower.tri","options","sys.parent","split","strwrap","source","writeLines","margin.table","ls","matrix","subset","weekdays","switch","message","xtfrm","nrow","maxCol","system.time","tempfile","missing","nchar","solve","sort","textConnection","unlist","nlevels","ns-dblcolon","numeric_version","ns-load","ns-reflect.Rd","traceback","pos.to.env","tracemem","octmode","unname","path.expand","userhooks","pcre_config","pretty","order","outer","qr","QR.Auxiliaries","print.default","proc.time","utf8Conversion","prmatrix","rawConversion","readBin","raw","rawConnection","prod","readRDS","which","rep","replace","readRenviron","rank","zutils","sample","rapply","save","readline","stop","reg.finalizer","stopifnot","scale","sets","sink","scan","shQuote","slice.index","strsplit","serialize","sum","setTimeLimit","strptime","summary","slotOp","tabulate","table","showConnections","sign","socketSelect","standardGeneric","trace","unique","startsWith","warnings","zapsmall","tilde",".Machine","tapply","substitute","timezones","substr","unlink","zpackages","taskCallback","svd","structure","warning","strtrim","strtoi","toString","try","trimws","sys.source","withVisible","write","strrep","validUTF8","transform","typeof","sweep","which.min","taskCallbackNames","t","taskCallbackManager","vector","with","Comparison","Deprecated","median","IQR")
column_names <- c('PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked')


find_vars_helper <- function(x) {
    if (is.atomic(x)) {
        character()
    } else if (is.name(x)) {
        # print(x)
        var_name = as.character(x)
        is_valid = grepl('[a-zA-Z][0-9a-zA-Z.-_]*', var_name, perl=TRUE)
        if (is_valid && !is.element(var_name, global_funcs)) {
            var_name
        } else {
            character()
        }
    } else if (is.call(x)) {
        # print("Call")
        if (identical(x[[1]], quote(`<-`)) && is.name(x[[2]])) {
            lhs <- character()
            rhs <- tail(x, -2)
        } else if (identical(x[[1]], quote(`$`)) && is.name(x[[2]])) {
            lhs <- as.character(x[[2]])
            rhs <- tail(x, -3)
        } else {
            lhs <- character()
            rhs <- x
        }
        unique(c(lhs, unlist(lapply(rhs, find_vars_helper))))
    } else if (is.pairlist(x)) {
        unique(unlist(lapply(x, find_vars_helper)))
    } else {
        stop("Don't know how to handle type ", typeof(x),
        call. = FALSE)
    }
}

find_vars <- function (x) {
    return(find_vars_helper(parse(text=x)[[1]]))
}

find_assign <-  function(stmt) {
    x <- parse(text=stmt)[[1]]
    if (is.call(x) && identical(x[[1]], quote(`<-`))) {
        deparse(x[[2]])
    } else {
        character()
    }
}

RENAMED_VARIABLE = "slacc"

replace_variable_name_helper <- function(x, var_name){
    if (is.atomic(x)) {
        x
    } else if (is.name(x)) {
        name = as.character(x)
        if (name == var_name) {
            parse(text=RENAMED_VARIABLE)[[1]]
        } else {
            x
        }
    } else if (is.call(x) || is.pairlist(x)) {
        for (i in 1:length((x))) {
            x[[i]] <- replace_variable_name_helper(x[[i]], var_name=var_name)
        }
        x
    } else {
        stop("Don't know how to handle type ", typeof(x),
        call. = FALSE)
    }
}


replace_variable_name <- function(stmt, var_name) {
    print(var_name)
    x <- replace_variable_name_helper(parse(text=stmt)[[1]], var_name)
    deparse(x)
}


# print(find_assign('table(hello$bbc == common, two)'))
# print(find_assign("full_data$Title[full_data$Title == 'Mlle'] <- 'Miss'"))

# print(find_vars('qwe <- table(hello$bbc == common, two)'))
# print(find_vars("x<-df"))

# print(replace_variable_name('full_data$Embarked <- factor(full_data$Embarked)', 'full_data'))
# print(replace_variable_name("x<-df", "df"))