library(tidyverse)
library(readr)
library(ggplot2)
library(stringr)

character_list <- read_csv("dictionary_fictional_characters_gender.csv")

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
  unique() 
  

ggplot(data = filtered_gender) + 
  aes(x = gender)+
  geom_bar()+
  xlab('Genders') +
  ylab('Number of Characters')+
  theme_minimal()

ggsave('character_bar.pdf')

ggplot(data = filtered_gender) +
  aes(x= gender, fill = gender)+
  geom_bar(aes(y = after_stat(count / sum(count)))) +
  scale_y_continuous(labels = scales::percent)+
  xlab('Genders') +
  ylab('Percentage of Characters')+
  theme_minimal() +
  scale_fill_manual(values = c('#9dc190','#ffc594'))+
  theme(legend.position = "none")
  
ggsave('ratio_gender.pdf')

