import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


import re

from utils import lib, cache
from misconceptions.common import helper


_DPLYR_FUNC_STR = "arrange|auto_copy|all_equal|add_rownames|compute|copy_to|coalesce|case_when|bind|common_by|" \
                  "between|cumall|dim_desc|explain|desc|distinct|failwith|group_by_prepare|filter|id|groups|" \
                  "group_indices|if_else|join|join\.tbl_df|group_size|grouped_df|group_by|lead\-lag|make_tbl|" \
                  "mutate|n|n_distinct|lazy_ops|na_if|location|named_commas|nth|ranking|partial_eval|recode|query|" \
                  "order_by|near|slice|rowwise|select|select_vars|sample|select_if|tbl_df|summarise_each|tally|" \
                  "summarise_all|src_tbls|summarise|with_order|tbl|vars|top_n|bind_rows"

_BASE_FUNC_STR = "MathFun|Reserved|Foreign|Last\.value|NumericConstants|Ops\.Date|ISOdatetime|RdUtils|Recall|" \
                 "Hyperbolic|Sys\.glob|Sys\.info|Cstack_info|UseMethod|Rhome|DateTimeClasses|Extract\.data\.frame|" \
                 "Extract\.factor|log|Sys\.localeconv|Sys\.readlin|Memory\-limits|Memory|Primitive|Logic|Quotes|" \
                 "Internal|Constants|Paren|NA|\.Platform|Round|agrep|NULL|Sys\.sleep|Sys\.time|Special|all|" \
                 "Sys\.getenv|Syntax|Sys\.getpid|as\.Date|Startup|append|assignOps|apply|Sys\.which|Control|" \
                 "Vectorize|as\.POSIX\*|as\.function|all\.equal|attr|Trig|all\.names|Extremes|attributes|attach|" \
                 "assign|any|as\.environment|as\.data\.frame|basename|base\-defunct|base\-deprecated|aperm|\.bincode|" \
                 "base\-internal|base\-package|Foreign\-internal|chol2inv|cat|class|browserText|browser|cbind|" \
                 "bindenv|bitwise|Random|Random\.user|Sys\.setFileTime|Sys\.setenv|contributors|connections|" \
                 "char\.expand|R\.Version|abbreviate|character|args|array|callCC|autoload|backsolve|date|conditions|" \
                 "dcf|conflicts|deparse|data\.matrix|deparseOpts|capabilities|dataframeHelpers|builtins|body|" \
                 "do\.call|bquote|dontCheck|eapply|by|c|duplicated|call|dyn\.load|chkDots|chol|eigen|file\.info|" \
                 "debug|delayedAssign|col|charmatch|chartr|dim|dimnames|files2|colSums|eval|exists|row+colnames|" \
                 "file\.path|find\.package|getDLLRegisteredRoutines|comment|copyright|complex|commandArgs|formatC|" \
                 "data\.class|function|crossprod|funprog|data\.frame|file\.show|files|findInterval|diff|gc|force|" \
                 "cumsum|difftime|dots|getLoadedDLLs|groupGeneric|curlGetHeaders|cut\.POSIXt|interaction|" \
                 "interactive|grouping|double|identical|gc\.time|gctorture|expand\.grid|identity|cut|kappa|grep|" \
                 "grepRaw|expression|extSoftVersion|factor|det|kronecker|lapply|forceAndCall|lazyLoad|is\.function|" \
                 "list2env|formals|is\.language|detach|\.Device|dput|drop|encodeString|is\.object|isSymmetric|diag|" \
                 "jitter|is\.recursive|get|load|levels|mat\.or\.vec|match\.fun|libPaths|getCallingDLL|match|list|" \
                 "mean|environment|droplevels|file\.access|memCompress|list\.files|matmult|file\.choose|gzcon|names|" \
                 "noquote|nargs|hexmode|make\.names|pmatch|is\.R|make\.unique|isS4|polyroot|memory\.profile|dump|" \
                 "format\.pval|norm|formatDL|ns\-topenv|l10n_info|merge|prop\.table|getwd|normalizePath|numeric|" \
                 "NotYet|labels|ns\-hooks|ns\-internals|pushBack|license|print|gl|parse|match\.arg|" \
                 "match\.call|format|ifelse|paste|quit|format\.info|range|regex|regmatches|print\.data\.frame|mode|" \
                 "remove|integer|readChar|round\.POSIXt|getNativeSymbolInfo|rowsum|seq\.Date|readLines|rev|" \
                 "seq\.POSIXt|rle|gettext|is\.single|sQuote|is\.unsorted|row|iconv|row\.names|icuSetCollate|" \
                 "libcurlVersion|invisible|is\.finite|name|length|lengths|search|sprintf|seq|locales|logical|" \
                 "on\.exit|srcfile|seek|sequence|mapply|lower\.tri|options|sys\.parent|split|strwrap|source|" \
                 "writeLines|margin\.table|ls|matrix|subset|weekdays|switch|message|xtfrm|nrow|maxCol|" \
                 "system\.time|tempfile|missing|nchar|solve|sort|textConnection|unlist|nlevels|ns\-dblcolon|" \
                 "numeric_version|ns\-load|ns\-reflect\.Rd|traceback|pos\.to\.env|tracemem|octmode|unname|" \
                 "path\.expand|userhooks|pcre_config|pretty|order|outer|qr|QR\.Auxiliaries|print\.default|proc\.time|" \
                 "utf8Conversion|prmatrix|rawConversion|readBin|raw|rawConnection|prod|readRDS|which|rep|replace|" \
                 "readRenviron|rank|zutils|sample|rapply|save|readline|stop|reg\.finalizer|stopifnot|scale|sets|sink|" \
                 "scan|shQuote|slice\.index|strsplit|serialize|sum|setTimeLimit|strptime|summary|slotOp|" \
                 "tabulate|table|showConnections|sign|socketSelect|standardGeneric|trace|unique|startsWith|warnings|" \
                 "zapsmall|tilde|\.Machine|tapply|substitute|timezones|substr|unlink|zpackages|taskCallback|" \
                 "svd|structure|warning|strtrim|strtoi|toString|try|trimws|sys\.source|withVisible|write|strrep|" \
                 "validUTF8|transform|typeof|sweep|which\.min|taskCallbackNames|t|taskCallbackManager|vector|with|" \
                 "Comparison|Deprecated"


_STAT_FUNC_STR = "median|IQR"


class DataFrameParser(lib.O):
  def __init__(self):
    self.SPACE = ' '
    self.VAR_NAME = '%s*\w[0-9a-zA-Z\.\-_]*%s*' % (self.SPACE, self.SPACE)
    self.QUOTED_VAR_NAME = "%s*[\'\"]%s[\'\"]%s*" % (self.SPACE, self.VAR_NAME, self.SPACE)
    self.NUMBER = "%s*[0-9]+%s*" % (self.SPACE, self.SPACE)
    self.DIRECT_ACCESS = "(%s\[.*,.*\].*)" % self.VAR_NAME
    self.COL_ACCESS = "(%s\$%s.*)" % (self.VAR_NAME, self.VAR_NAME)
    self.FUNCTION_ACCESS = '(.*(?:^|\W+?)(?:%s)\(.+)' % "|".join([_DPLYR_FUNC_STR, _BASE_FUNC_STR, _STAT_FUNC_STR])
    lib.O.__init__(self)

  def parse_direct_access(self, s):
    matched = re.search(self.DIRECT_ACCESS, s.strip())
    matched_str = None if not matched else matched.group(0).strip()
    if matched_str and helper.is_bracket_balanced(matched_str):
      return matched_str
    return None

  def parse_col_access(self, s):
    matched = re.search(self.COL_ACCESS, s.strip())
    matched_str = None if not matched else matched.group(0).strip()
    if matched_str and helper.is_bracket_balanced(matched_str):
      return matched_str
    return None

  def parse_function_access(self, s):
    matched = re.search(self.FUNCTION_ACCESS, s.strip())
    matched_str = None if not matched else matched.groups()[0].strip()
    if matched_str and helper.is_bracket_balanced(matched_str):
      return matched_str
    return None

  def parse(self, s):
    def _helper(latest):
      return None if latest and "plot" in latest else latest

    def _update_matched(current, latest):
      latest = _helper(latest)
      if (not current) or (latest and len(latest) > len(current)):
        current = latest
      return current
    matched = _update_matched(None, self.parse_direct_access(s))
    matched = _update_matched(matched, self.parse_col_access(s))
    matched = _update_matched(matched, self.parse_function_access(s))
    return matched

  def parse_file(self, file_path):
    stmts = []
    source = cache.read_file(file_path)
    for line in source.split("\n"):
      line = line.strip()
      if line and not line.startswith("#"):
        matched = self.parse(line)
        if matched:
          stmts.append(matched)
    return stmts


def _test():
  parser = DataFrameParser()
  str = "Male_Ages <- full[ which(is.na(full$Age)) & full$Sex == 'male' , ]"
  str = "full$Fare[1044] <- median(thirdclass$Fare , na.rm = TRUE)"
  str = "which(is.na(full$Fare))"
  str = "ggplot(train , aes(x = Survived)) + geom_bar()"
  # str = "test <- bind_rows(test,train)"
  # str = 'count_nan_age_titanic = titanic_df["Age"].isnull().sum()'
  print(parser.parse_function_access(str))
  print("\"%s\"" % "|".join([_DPLYR_FUNC_STR, _BASE_FUNC_STR, _STAT_FUNC_STR]).replace("|", "\",\"").replace("\\", ""))


if __name__ == "__main__":
  _test()
