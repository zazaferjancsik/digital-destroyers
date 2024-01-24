library(tidyverse)
library(readr)
library(ggplot2)

character_years <- read_csv("dictionary_fictional_characters_gender.csv")

filtered_years <- character_years|>
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

number <- filtered_years |>
  ungroup() |>
  group_by(gender,start_year) |>
  count(wt = NULL,sort = FALSE) |>
  print()

percentage <- number |>
  arrange(start_year) |>
  group_by(gender) |>
  summarize(sum(n))
  
ggplot(data = percentage)+ 
  aes(x=start_year,y = n, color = gender) +
  geom_point() +
  theme_minimal()+
  labs(title ='Gender Ratio Over the Years')+
  xlab('Year') +
  ylab('Gender')+
  scale_color_manual(values = c('#b3c5f4','#ffc6c1','#b57edc'))

#geom_smooth(method=lm , color="red", se=FALSE) +