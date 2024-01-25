library(tidyverse)
library(readr)
library(ggplot2)
library(dplyr)
library()

character_years <- read_csv("dictionary_fictional_characters_gender.csv")

filtered_years <- character_years|>
  mutate(gender = case_when(gender == 'Boy' ~ 'Man',
                            gender == 'Female' ~'Woman',
                            gender == 'Girl'~ 'Woman',
                            gender == 'Man'~ 'Man',
                            gender == 'Male'~ 'Man',
                            TRUE~ NA)) |>
  filter(gender == 'Man'| gender== 'Woman')

number <- filtered_years |>
  ungroup() |>
  group_by(gender,start_year) |>
  count(wt = NULL,sort = FALSE)

percentage <- number |>
  arrange(start_year) |>
  group_by(gender) |>
  summarize(sum(n))

ggplot(data = percentage)+ 
  aes(x=start_year,y = n, color = gender) +
  geom_point() +
  theme_minimal()+
  xlab('Year') +
  ylab('Gender Percentage')+
  scale_color_manual(values = c('#9dc190','#ffc594'))

number_years <- number |>
  pivot_wider(names_from = gender,values_from = n ) |>
  mutate(
    Man = if_else(is.na(Man), 0, Man),
    Woman = if_else(is.na(Woman), 0, Woman)
    )|>
  ungroup()|>
  arrange(start_year)|>
  na.omit()|>
  mutate(Man=cumsum(Man),
         Woman=cumsum(Woman))|>
  pivot_longer(cols = c('Man','Woman'),names_to = 'gender',values_to = 'number') |>
  filter(start_year>1900)

ggplot(data = number_years)+
  aes(x= start_year, y= number, color = gender)+
  geom_point()+
  guides(color = guide_legend('Gender'))+
  xlab('Year')+
  ylab('Cummulative Number')+
  scale_color_manual(values = c('#9dc190','#ffc594'))+
  theme_minimal()
  
ggsave('Cummulative_number_gender_per_year.pdf')

ratio_data <- number_years |>
  mutate(ratio = Man / Woman)|>
  filter(start_year>1920)

ggplot(data = ratio_data)+
  aes(x=start_year,y=ratio)+
  geom_point()+
  theme_minimal()+
  xlab('Year')+
  ylab('Ratio of Man to Woman')

ggsave('Ratio_Man_to_Woman.pdf')
