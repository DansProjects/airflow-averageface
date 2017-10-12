# Airflow pipeline

Project will use Airflow and Scrapy to build out a data pipeline to:
 1. Scrape HTML from a website
 2. Extract profile pictures from HTML
 3. Determine the average face of all pictures using OpenCV
 4. Save average face to HTML file
 
Landmark library will detect facial features (68 points) as shown below and save the points into a text file.
Pictures without any faces in it will be removed.  
<img src="/averageface/images/barak-obama-landmarks.png" height="450" width="450"/>

(simplified) Points will be averaged to produce an composition of all of the profile images. Below is the actual 
output for the averaged face of a Princeton CS graduate student.  
<img src="/averageface/images/averageface-csgrad.jpg" height="450" width="450"/>
