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
`virtualenv install ditenv`

Enable ditenv :
`source/ditenv/bin/activate`

 We can now install scrapy using pip by running the following command in the terminal:
 `pip install Scrapy`
 
 To check if it is well installed let's execute the command : `scrapy version `
 ![alt text](https://github.com/GayePaapIsaac/scrapy_tutoriel/blob/tuto/img/activationvirtualenv.png)
 
This proves that scrapy is well installed in our virtual environment

### 4. Creating a Scrapy project
Next, you can create a Scrapy spider by running the following command: 
`scrapy startproject scrapy_tutoriel` 
the name of our project will be scrapy_tutoriel
This will create a scrapy_tutoriel directory with the following contents:

![alt text](https://github.com/GayePaapIsaac/scrapy_tutoriel/blob/tuto/img/scrapy_tree.png)
 
### 5. Creating a Scrapy project
The entry point of the project is the spider. We are going to create a new file in the spiders folder that we are going to call "first_scraping.py"

In this file, we will create the class that will inherit from spider
The Spider class is the base class used to create spiders in Scrapy. It provides basic functionality for extracting data from websites. Each spider must be a subclass of the Spider class, and must define at least the name and start_urls attributes. Here is an example definition of the Spider class:

![alt text](https://github.com/GayePaapIsaac/scrapy_tutoriel/blob/tuto/img/spyder_and_parse.png)

The parse() method is the main data extraction method in Scrapy. This method is called for each page downloaded by the spider, and must return scrapy.Request or scrapy.Item objects. Here is an example definition of the parse() method:

```
import scrapy

class fnac_spyder(scrapy.Spider):
    name= 'fnac_scraping'
	   start_urls=['https://www.fnac.com/']

	   def parse(self, response) : 
		      dic_article={
		        'article':response.css('div.name::text').getall(),
		        'article_price':response.css('div.prc::text').getall()
		       }
		
		   yield dic_article
```
### parse fonction detail
The parse() function is a key method of the Scrapy framework, which allows to browse and extract information from a web page using predefined selection rules. This function is important because it allows you to transform the HTML content of the page into a data structure that is easier to manipulate and analyze.

Scrapy's parse() function is an essential tool for extracting data in an efficient and structured way from web pages. It makes it easy to navigate web pages and handle errors, which greatly facilitates the work of developers and data analysts.

### 6. Storage of collected data
##### How to run our spider
To put our spider to work, go to the project’s top level directory and run:
`scrapy crawl fnac_scraping` 
This command runs the spider with the name fnac_scraping we just added.
We will execute this same command by adding the parameter -o response.json
this will automatically create a response.json file containing our extracted data.
we thus obtain :
` scrapy crawl fnac_scraping -O response.json` 

### conclusion
Congratulations on completing your Scrapy tutorial! You should now have a solid understanding of the parse function in this framework, which is one of the key elements for efficiently extracting data from websites. With Scrapy, you can automate the process of data extraction, save time, and get accurate and consistent results. We hope that this tutorial has been helpful to you and that you will be able to apply it in your future data extraction projects.

here is the source of your tutorial:
[documentation]([https://github.com/GayePaapIsaac/scrapy_tutoriel/blob/tuto/DIT_tutoriel_scrapy/DIT_tutoriel_scrapy/spiders/reponse.json](https://docs.scrapy.org/))

This page is the official documentation of Scrapy, which provides comprehensive information about the framework including guides, tutorials, and references. It's a valuable resource for learning how to use Scrapy and for troubleshooting common issues when extracting data from websites.

some useful links for the good understanding of this tutorial:
 
https://youtu.be/BqptmmB3BZY

https://youtu.be/48GDX5_2ebQ
