# scrapy_tutoriel
### Content
###
---
 Introduction to Scrapy: The Data Collection Framework for the Web
1. What is Scrapy?
2. Architecture of Scrapy       
3. Installing Scrapy
     Get started on ubuntu
4. Creating a Scrapy project
5. Creating a Scrapy Spider
6. Storage of collected data
7. conclusion
---
#### let's go
![alt text](https://github.com/GayePaapIsaac/scrapy_tutoriel/blob/tuto/img/logoscrapy.png)

## . Introduction to Scrapy
### 1. What is Scrapy?
Scrapy is an open-source data collection framework used for web scraping and web crawling. It allows developers to easily extract structured data from websites and APIs, and can be used for a variety of purposes such as data mining, information retrieval, and web content monitoring.


### 2. Architecture of Scrapy
The architecture of Scrapy is based on a few key components:

*Spiders*: These are the main components of Scrapy that define how to navigate websites and extract data. They are responsible for sending HTTP requests, processing the responses, and storing the extracted data.

*Item Pipeline*: Once the data is extracted by the spider, it is passed to the Item Pipeline, which is a series of processing steps that can modify or filter the data before it is stored.

*Downloader*:This component is responsible for sending HTTP requests and handling responses. It is used by the spiders to make requests to websites and APIs.

*Scheduler*: This component manages the queue of requests and ensures that the spiders don't overload the target website.

### graphic illustration
![alt text](https://github.com/GayePaapIsaac/scrapy_tutoriel/blob/tuto/img/scrapy_architecture_02.png)

### 3. Installing Scrapy
To get started with Scrapy on Ubuntu, we will first install it in a virtual environment.
##### 
Installation of the virtual environment:
`pip install virtualenv`

Creation of a virtual environment in a desired refectory:
`virtualenv install scrapy_venv`

Enable scrapy_venv
`source/scraoy_venv/bin/activate`

 We can now install scrapy using pip by running the following command in the terminal:
 
