library(tidyverse)
library(readr)
library(ggplot2)
library(stringr)

character_list <- read_csv("dictionary_fictional_characters_gender.csv")

filtered_gender <- character_list|>
  mutate(gender = case_when(gender == 'Boy' ~ 'Male',
                            gender == 'Female' ~'Female',
                            gender == 'Hermaphrodite' ~ 'Intersex',
                            gender == 'Girl'~ 'Female',
                            gender == 'Man'~ 'Male',
                            gender == 'Male'~ 'Male',
                            TRUE~ NA)) |>
  na.omit() |>
  filter(gender == 'Male'| gender== 'Female'| gender == 'Intersex')
  

ggplot(data = filtered_gender) + 
  aes(x = gender, y = '')+
  geom_col(position = 'stack')+
  labs(title = 'Gender Ratio of Fictional Characters') +
  xlab('Genders') +
  ylab('Number of Characters')+
  theme_minimal()+
  theme(panel.grid.major.x = element_blank(),
        panel.grid.minor.x = element_blank())

ggsave('character_bar.pdf')

