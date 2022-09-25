# Tv_Series_Analysis
This is a basic analysis of Tv-Series released till now.


**Data collection:**

Collected the Tv-Series data on Sep 11, 2022.
The scraper is written in Python language. 
And I have used the below modules
1) requests - To make the request 
2) BeautifulSoup - To parse the html page returned from response
3) etree - To search for an object in the parsed html page. 
4) sleep 
5) random

Flow of the scraper:
Initally, i have collected all the required home page urls manually (total 49 urls) and hardcoded one url in the scraper.
I have ran the scraper with one home page url only each time. Like this i have ran around 12 processes (based on memory consumption) at a time. (No blocking faced)
1) The scraper takes the home page url and fetches the page with requests module. (timeout = 10sec, attempts = 3)
2) After fetching the page correctly, it will parse the page with beautifulsoup and extract the required details. 
3) For extracting particular fields it will use etree to convert the page to DOM and use xpath.
4) After successfully extracting required details from a page, it will check whether the next page is available or not. (More Tv-Series to collect)
5) If the next page is available then it will do step 1-4 again.
6) After exracting 1,000 TV-series details, it will write the data to a file. This way we don't need to store all the data in memory. This will reduce the load and memory consumption on system.


**Data cleaning**

After collecting all the required data i have imported the data into SQL.
For this basic analysis project, Tv-Series released year is one of the important field
1) Here, i have removed the rows where year field is null.
2) Removing duplicate fields
3) Changing encoded characters
4) Cleaning year field
5) Cleaning runtime field
6) Added new columns (start_year, end_year, genre related columns) - to make the analysis part easy


**Analysing the data**

I have used Power BI to analyse the data.
These are the few points that i have observed

![page1](https://user-images.githubusercontent.com/54261591/192135784-9dabce9f-5b44-4652-9829-433554181a87.png)

"Total series released in each year" 
1) After 1990, there is a steady growth in no.of series by each year. (Around 100 per each year)
2) After 2000, there is a significantly growth in no.of series by each year. (Around 20% each year)
3) But on 2019, there is a small drop and the drop again came on 2021.

"Top 5 Genres by year (released)"
Drama, Comedy, Documentary, Reality-Tv, Animation - Top 5 genres released on year 2021.
1) On 2021, Drama is the most released Genre.
2) (Drama, Documentary, Reality-Tv, Animation) - the growth of these series started on 1997 with individual growth rate.
3) If we clearly observe, Comedy is top genre till 2021. This genre is the major contributor for the significant growth and for the drop in recent years in the "Total series released in each year" graph.
4) Based on 2022 stats (till Aug), drop of "total Tv-Series by each year" and comedy genre will continue.

"Total series released" tree
1) This tree also says the same thing. Comedy genre is the most released Tv-series genre. The drop in comedy genre will create a significant impact.
2) The top 5 genres alone contribute more Tv-series than all the other genres combined.
3) Because of this any drop or rise in the top 5 genres will impact the total TV-series significantly.

"Total Runtime by certificates" - minutes
1) It will take 7.83 years to watch a single episode from each series
The certificate column may not be accurate

![page2](https://user-images.githubusercontent.com/54261591/192135793-262935e0-575a-4768-a8e2-e19eda0a5380.png)

"Aveerage Rating" (out of 10)
1) Average rating is b/w 3-3.5 only most of the time.
2) But from 2006 onwards, it is decreased a lot. On 2021 it is 2.49 only.
3) This might be due to the overall increase in series and voters
4) We can check this from "Total series released in each year" and "Total votes by year". Total voters are almost double when we compare 2006 and 2021. With the increased no.of tv-series the quality of tv-series is decreased a lot.
