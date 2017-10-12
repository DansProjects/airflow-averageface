# Airflow pipeline

Project will use Airflow, Scrapy, and OpenCV to build out a data pipeline to scrape profile images from a website
and create an averaged image representation of all the profiles. Steps are below:
 1. Clear scraped files folder in cspeople/scraped/full  
 2. Scrape images from target site and save in cspeople/scraped/full
 3. Use the facial landmark library to determine 68 key features in a face and save the coordinates in a text file in cspeople/scraped/full
 4. Determine the average face of all pictures using the landmarks and OpenCV, save in averageface/images
 
The Airflow DAG graph is below. "scrape_progress" was added just to experiment with dependencies. 
 
Facial landmark (dlib) library will detect facial features (68 points) as shown below and save the points into a text file. 
Pictures without any faces in it will be removed.
<img src="/averageface/images/barak-obama-landmarks.png" height="450" width="450"/>

(simplified) Points will be averaged to produce an composition of all of the profile images. Below is the actual 
output for the averaged face of a Princeton CS graduate student.
<img src="/averageface/images/averageface-csgrad.jpg" height="450" width="450"/>
