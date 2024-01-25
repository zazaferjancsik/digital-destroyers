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
  select(-start_year)|>
  filter(gender == 'Man'| gender== 'Woman') |>
  mutate(method = 'broadened sample')

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

together <- rbind(old_filtered_gender,filtered_gender)

# ggplot(data =together) +
#   aes(x= gender)+
#   geom_bar(aes(y = after_stat(prop), group = method, fill = gender)) +
#   scale_y_continuous(labels = scales::percent)+
#   xlab('Genders') +
#   ylab('Percentage of Characters')+
#   facet_wrap(~method)+
#   theme_minimal() +
#   scale_fill_manual(values = c('#9dc190','#ffc594'))+
#   theme(legend.position = "none")

counts <- together |>
  group_by(method, gender) |>
  summarise(count = n())

method_counts <- together |>
  group_by(method) |>
  summarise(group_count = n())

counts <- counts |> 
  left_join(method_counts) |>
  mutate(percentage = count / group_count)

ggplot(data = counts) +
  aes(x = gender, y = percentage, fill = gender) +
  geom_col()+
  scale_y_continuous(labels = scales::percent)+
  xlab('Genders') +
  ylab('Percentage of Characters')+
  facet_wrap(~method)+
  theme_minimal() +
  scale_fill_manual(values = c('#9dc190','#ffc594'))+
  theme(legend.position = "none")
