# Airflow pipeline

Project will use Airflow, Scrapy, and OpenCV to build out a data pipeline to scrape profile images from a website
and create an averaged image representation of all the profiles. Steps are below:
 1. Clear scraped files folder in cspeople/scraped/full  
 2. Scrape images from target site and save in cspeople/scraped/full
 3. Use the facial landmark library to determine 68 key features in a face and save the coordinates in a text file in cspeople/scraped/full
 4. Determine the average face of all pictures using the landmarks and OpenCV, save in averageface/images
 
The Airflow DAG graph is below. "scrape_progress" was added just to experiment with dependencies.  
<img src="/averageface/images/airflow-dag-tree.png" height="200" width="500"/>
 
Facial landmark (dlib) library will detect facial features (68 points) as shown below and save the points into a text file. 
  
<img src="/averageface/images/barak-obama-landmarks.png" height="450" width="425"/>

(simplified) Points will be averaged to produce an composition of all of the profile images. Below is the actual 
output for the averaged face of a Princeton CS graduate student.
<img src="/averageface/images/averageface-csgrad.jpg" height="450" width="450"/>

 1. Copy the DAG file: ```dags/average_faces_pipeline.py``` to your Airflow directory (wherever you initialized it)
 2. Change the ```cspeople_scraper, cspeople_scraper_path, averageface_path``` variables to target the directory
  that you cloned this project into.

Start Airflow:
```
airflow webserver -p 8080
airflow scheduler
```

Run the AverageFacePipeline task.

##### Customizing data source

Note: Scraper ```cspeople/spiders/cs_grad_people_spider.py``` is current set to scrape ```http://www.cs.princeton.edu/people/grad``` 
and uses xpath to extract images. To average a different data set, change the scrape url and update the xpath (//img/@src - extract all images). The application
will ignore and delete all images that it cannot detect a face in. 
 
