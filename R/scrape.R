# Assume get the pd dataframe and convert to an R dataframe
library(reticulate)
library(readr)

file <- "nba-2019-data.csv"
df <- readr::read_csv(file)

# TODO: Read through R4DS and AdvR for help with data cleaning and prep
# What do do with NA values upon import/read?
# What to do with NA values introduced by coercion?
