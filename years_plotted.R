library(tidyverse)
library(readr)
library(ggplot2)

character_years <- read_csv("dictionary_fictional_characters_gender.csv")

filtered_years <- character_years|>
  mutate(gender = case_when(gender == 'Boy' ~ 'Man',
                            gender == 'Female' ~'Woman',
                            gender == 'Girl'~ 'Woman',
                            gender == 'Man'~ 'Man',
                            gender == 'Male'~ 'Man',
                            TRUE~ NA)) |>
  na.omit() |>
  filter(gender == 'Man'| gender== 'Woman') |>
  unique() 

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

ratio_data <- number |>
  group_by(gender, start_year)|>
  pivot_wider(names_from = gender,values_from = n ) |>
  ungroup()|>
  mutate(ratio = Man / Woman)

ggplot(data = ratio_data)+
  aes(x=start_year,y=ratio)+
  geom_path()

#geom_smooth(method=lm , color="red", se=FALSE) +