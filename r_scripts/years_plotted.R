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

#filtering out years before 1919 and after 2019. using 'summar_bin' to 
#add the counts per 25 years. Although it says 4 bins, the graph displays 5. 
number |> filter(start_year >= 1919, start_year<=2019) |>
  ggplot()+ 
  aes(x=start_year, y=n,fill = gender) +
  geom_bar(stat= 'summary_bin', fun = sum, position = 'dodge',bins=4)+
  theme_minimal()+
  xlab('Year') +
  ylab('Cummulative number of gender')+
  scale_fill_manual(values = c('#9dc190','#ffc594'))

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

#plotting the cummulative value of each gender throughout the years. 
ggplot(data = number_years)+
  aes(x= start_year, y=number, color = gender)+
  geom_point()+
  guides(color = guide_legend('Gender'))+
  xlab('Year')+
  ylab('Cummulative Number')+
  scale_color_manual(values = c('#9dc190','#ffc594'))+
  theme_minimal()
  
ggsave('Cummulative_number_gender_per_year.pdf')

#calculating the ratio by dividing the cummulative Man by the Woman.
ratio_data <- number_years1 |>
  mutate(ratio = Man / Woman)|>
  filter(start_year>=1920,start_year<=2019)

#creating scatterplot and connecting the points with a line.
ggplot(data = ratio_data)+
  aes(x=start_year,y=ratio)+
  geom_point()+
  geom_line()+
  theme_minimal()+
  xlab('Debut Year of Characters')+
  ylab('Ratio of Man to Woman')

ggsave('Ratio_Man_to_Woman.pdf')
