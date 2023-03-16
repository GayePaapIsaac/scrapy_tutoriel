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

[Spiders]: These are the main components of Scrapy that define how to navigate websites and extract data. They are responsible for sending HTTP requests, processing the responses, and storing the extracted data.

[Item Pipeline]: Once the data is extracted by the spider, it is passed to the Item Pipeline, which is a series of processing steps that can modify or filter the data before it is stored.

[Downloader]:This component is responsible for sending HTTP requests and handling responses. It is used by the spiders to make requests to websites and APIs.

[Scheduler]: This component manages the queue of requests and ensures that the spiders don't overload the target website.
### Heading
Tutoriel  framework scrapy on python 
voir le sommaire
