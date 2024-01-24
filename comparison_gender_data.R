library(tidyverse)
library(readr)
library(ggplot2)
library(stringr)

character_list <- read_csv("dictionary_fictional_characters_gender.csv")
old_character_list <- read_csv("old_gender_data.csv")

filtered_gender <- character_list|>
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
  mutate(method = 'inferred')

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
  mutate(method = 'original') 

together <- rbind(old_filtered_gender,filtered_gender)

ggplot(data = together) +
  aes(x= gender)+
  geom_bar(aes(y = after_stat(prop), group = method, fill = gender)) +
  scale_y_continuous(labels = scales::percent)+
  xlab('Genders') +
  ylab('Percentage of Characters')+
  facet_wrap(~method)+
  theme_minimal() +
  scale_fill_manual(values = c('#9dc190','#ffc594'))+
  theme(legend.position = "none")

