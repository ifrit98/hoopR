# Assume get the pd dataframe and convert to an R dataframe
library(reticulate)
library(readr)
library(dplyr)


#' Load a csv file into a tibble for examination
#' @export
load_data <- function(file = "data/nba-2019-data.csv") {
  suppressWarnings(readr::read_csv(file))
}



# TODO: Read through R4DS and AdvR for help with data cleaning and prep
# What do do with NA values upon import/read?
# What to do with NA values introduced by coercion?


players <- function(df) {
  dplyr::distinct(df, Player)
}

#' @importFrom magrittr %>%
#' @importFrom dyplr filter
player <- function(df, name) {
  df %>% dplyr::filter(Player == name)
}

#' Remove column(s) of dataframe
#' @export
rm_cols <- function(df, cols) {
  # within(df, rm(cols)) # Want to keep original dl
  # subset(df, select = -cols) #invalid arg to unary operator?
  df[!names(df) %in% cols]
}


#' Pull a specific statistic for all players
#' @importFrom rlang ensym as_string
#' @importFrom dplyr select
#' @export
stat <- function(df, stat) {
  str <- as_string(ensym(stat))
  stopifnot(str %in% names(df))
  select(df, str)
}


#' Pull a specific player statistic from the dataframe
#' @export
player_stat <- function(df, name, stat) {
  str <- rlang::as_string(rlang::ensym(stat))
  plr <- player(df, name)
  dplyr::select(plr, str)
}


