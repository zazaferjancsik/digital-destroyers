library(tidyverse)
library(readr)
library(ggplot2)
library(dplyr)
library(lubridate)

character_years <- read_csv("dictionary_fictional_characters_gender.csv")

#replacing girl and female with woman, male and boy with man. filtering out 
#other terms such as: cat.
filtered_years <- character_years|>
  mutate(gender = case_when(gender == 'Boy' ~ 'Man',
                            gender == 'Female' ~'Woman',
                            gender == 'Girl'~ 'Woman',
                            gender == 'Man'~ 'Man',
                            gender == 'Male'~ 'Man',
                            TRUE~ NA)) |>
  filter(gender == 'Man'| gender== 'Woman')

#groping by gender and year to be able to count the amount of instances of 
#each gender per year
number <- filtered_years |>
  ungroup() |>
  group_by(gender,start_year) |>
  count(wt = NULL,sort = FALSE) |>
  filter(start_year>1900, start_year<2020)

#filtering out years before 1919 and after 2019. Stacking the proportion of 
#instances of each gender per decade.  
number |> filter(start_year >= 1919, start_year<=2019) |>
  mutate(decade = round(start_year / 10) * 10) |>
  group_by(decade, gender) |>
  summarize(n = sum(n)) |>
  mutate(prop = n / sum(n)) |>
  ggplot() + 
  aes(x=decade, y=prop, fill = gender) +
  geom_bar(position = position_stack(), stat= 'identity')+
  geom_hline(yintercept =0.5)+
  theme_minimal()+
  guides(fill = guide_legend('Gender'))+
  xlab('Year') +
  ylab('Proportion of Gender per Decade')+
  scale_fill_manual(values = c('#9dc190','#ffc594'))

ggsave('Proportion_gen_dec.pdf')

#moving the Man and Woman under gender to become their own columns. Replacing 
# NA values with 0 to be able to later on do the cumulative sum. Arrange the 
#years so that they go from oldest to most recent. After getting the cum. sum.
# moving Man and Woman back to the column gender. 
number_years1 <- number |>
  pivot_wider(names_from = gender,values_from = n )|>
  mutate(
    Man = if_else(is.na(Man), 0, Man),
    Woman = if_else(is.na(Woman), 0, Woman)
  )|>
  ungroup() |>
  arrange(start_year)|>
  na.omit()|>
  mutate(Man=cumsum(Man),
         Woman=cumsum(Woman))
  
number_years <- number_years1 |>
  pivot_longer(cols = c('Man','Woman'),names_to = 'gender',values_to = 'number') 

#plotting the cumulative value of each gender throughout the years. 
ggplot(data = number_years)+
  aes(x= start_year, y=number, color = gender)+
  geom_point()+
  guides(color = guide_legend('Gender'))+
  xlab('Year')+
  ylab('Cummulative Number')+
  scale_color_manual(values = c('#9dc190','#ffc594'))+
  theme_minimal()
  
ggsave('Cummulative_number_gender_per_year.pdf')

#calculating the ratio by dividing the cumulative Woman by the Man.
ratio_data <- number_years1 |>
  mutate(ratio =  Woman /Man)|>
  filter(start_year>=1920,start_year<=2019)

#creating scatterplot and connecting the points with a line.Adding a horizontal 
#line at ypoint 1 to show where man and woman would be equal.
ggplot(data = ratio_data)+
  aes(x=start_year,y=ratio)+
  ylim(0,1.1)+
  geom_point()+
  geom_line()+
  geom_hline(yintercept = 1)+
  theme_minimal()+
  xlab('Debut Year of Characters')+
  ylab('Ratio of Woman to Man')

ggsave('Ratio_Man_to_Woman.pdf')
