library(tidyverse)
library(readr)
library(ggplot2)

character_years <- read_csv("dictionary_fictional_character_years.csv")

ggplot(data = character_year, aes(x=year, y=gender,  fill = gender)) +
  geom_point() +
  theme_ipsum()+
  labs(title ='Gender Ratio Over the Years')+
  xlab('Year') +
  ylab('Gender')+
  scale_fill_manual(values = c('#b3c5f4','#ffc6c1','#b57edc'))

#geom_smooth(method=lm , color="red", se=FALSE) +