# import tidyverse etc.
library(tidyverse)
library(readr)
library(ggplot2)
library(stringr)

# read in broadened sample and original sample csv files

character_list <- read_csv("dictionary_fictional_characters_gender.csv")
old_character_list <- read_csv("old_gender_data.csv")

# set all gender labels labeled as something other than Man or Woman to Man or Woman
filtered_gender <- character_list|>
  mutate(gender = case_when(gender == 'Boy' ~ 'Man',
                            gender == 'Female' ~'Woman',
                            gender == 'Girl'~ 'Woman',
                            gender == 'Woman'~ 'Woman',
                            gender == 'Man'~ 'Man',
                            gender == 'Male'~ 'Man',
                            TRUE~ NA)) |>
  # For NA values --> leave out
  select(-start_year)|>
  filter(gender == 'Man'| gender== 'Woman') |>
  mutate(method = 'broadened sample')

# set all gender labels labeled as something other than Man or Woman to Man or Woman
old_filtered_gender <- old_character_list|>
  mutate(gender = case_when(gender == 'Boy' ~ 'Man',
                            gender == 'Female' ~'Woman',
                            gender == 'Girl'~ 'Woman',
                            gender == 'Woman'~ 'Woman',
                            gender == 'Man'~ 'Man',
                            gender == 'Male'~ 'Man',
                            TRUE~ NA)) |>
  na.omit() |>
  filter(gender == 'Man'| gender== 'Woman') |>
  unique() |>
  mutate(method = 'sample') 

# use rbind to create side by side bargraph (faceted)
together <- rbind(old_filtered_gender,filtered_gender)

# set counts and summarize grouped by method and gender (total)
counts <- together |>
  group_by(method, gender) |>
  summarise(count = n())

# set a group count
method_counts <- together |>
  group_by(method) |>
  summarise(group_count = n())

#create a percentage of counts per total group count (group = both genders and method is sample or broadened sample)
counts <- counts |> 
  left_join(method_counts) |>
  mutate(percentage = count / group_count)

# create a side by side bar graph using ggplot
ggplot(data = counts) +
# set x-axis as gender, y-axis as the percentage and fill color per gender
  aes(x = gender, y = percentage, fill = gender) +
  geom_col()+
  scale_y_continuous(labels = scales::percent)+
# label x- and y-axis
  xlab('Genders') +
  ylab('Percentage of Characters')+
# facet_wrap to put the bar graph for sample and broadened sample in same graph
  facet_wrap(~method)+
  theme_minimal() +
# set theme of our research as fill colors
  scale_fill_manual(values = c('#9dc190','#ffc594'))+
# delete legend as it does not add to clarification
  theme(legend.position = "none")

# in 'Plots' graph is exported as pdf to Overleaf LaTex paper
