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
  filter(gender == 'Male'| gender== 'Female'| gender == 'Intersex') |>
  unique() 
  

ggplot(data = filtered_gender) + 
  aes(x = gender)+
  geom_bar()+
  labs(title = 'Gender Ratio of Fictional Characters') +
  xlab('Genders') +
  ylab('Number of Characters')+
  theme_minimal()

ggsave('character_bar.pdf')

ratio_gender <- ggplot(data = filtered_gender) +
  aes(x= gender, fill = gender)+
  geom_bar(aes(y = after_stat(count / sum(count)))) +
  scale_y_continuous(labels = scales::percent)+
  labs(title = 'Gender Ratio of Fictional Characters') +
  xlab('Genders') +
  ylab('Number of Characters')+
  theme_minimal() +
  scale_fill_manual(values = c('#b3c5f4','#ffc6c1','#b57edc'))
  
ggsave('ratio_gender.pdf')

