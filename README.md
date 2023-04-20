# Google Maps: Unsupervised Learning on Restaurants in PA
## _Zimeng Liu_
> As students at Dickinson College, we have gone to many local restaurants. But do we really know about the general scene of Carlisle's food service industry? In this research, profiles for restaurants in Carlisle, Pittsburgh, Harrisburg, and Philadelphia, are created using the information on all restaurants in these cities on Google Maps. The result shows that Carlisle has more restaurants with a rating between 3.5 and 4.0 than the other three cities. Based on the result of the regression, there is no correlation between rating, number of ratings, and category of restaurants. Moreover, by doing text analysis on the reviews of restaurants in Carlisle, the patterns of comments with good ratings and bad ratings are shown. 

### Data Dictionary
#### `PA0413.csv`
Dataset of information on all restaurants in Carlisle, Pittsburgh, Harrisburg, and Philadelphia on Google Maps.
- 650 rows x 6 columns
- 118 restaurants in Carlisle, 191 restaurants in Pittsburgh, 160 restaurants in Harrisburg, 181 restaurants in Philadelphia
- Data is collected from Google Maps by 03/30/2023

|variable           |class     |description        |
|:------------------|:---------|:------------------|
|userid             |character |Name of each restaurant |
|rating             |float     |Rating of each restaurant (with one decimal place)|
|rating_number      |integer   |Number of reviews of each restaurant |
|category           |character |Category of each restaurant set by the business |
|address            |character |Address of each restaurant |
|city               |character |City in each restaurant is located |

#### `CarlisleReview0413new.csv`
Dataset of information on restaurant reviews in Carlisle.
- 16897 rows x 9 columns
- data of 32 restaurants in Carlisle (118 in total)
- Data is collected from Google Maps by 04/12/2023

|variable           |class     |description        |
|:------------------|:---------|:------------------|
|restaurant         |character |Name of the restaurant |
|name               |character |Name of the reviewer of each review |
|rating             |float     |Rating of each review |
|time               |character |Length of time since each review was left |
|comment            |character |Content of each review (empty if only the reviewer only left rating) |
|before             |boolean   |If the review is given approximately before COVID-19 (before April 2020) |
|covid              |boolean   |If the review is given approximately during COVID-19 (after April 2020 & before April 2021*) |
|after              |boolean   |If the review is given approximately after COVID-19 (after April 2021) |
|period             |character |Period of each review was left (before, during, or after COVID-19)
*Governor Wolf announced that the indoor dining capacity raises to 75% for those restaurants that are self-certified on 03/16/2021, effective on 04/04/2021.

