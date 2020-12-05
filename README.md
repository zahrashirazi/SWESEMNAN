# SWESEMNAN

##  Overview  
This Project Has three main Part: <br/>
- WebSite<br/>
- API<br/>
- WebScraper<br/>


##  Website https://pypiapp.ir
This website is based on one of the most powerful python framework called Django.<br>
Django follows a Model-View-Controller(MVC) architecture, which is split up into three different parts: The Model is the logical data structure behind the entire application and is represented by a database.<br>
The front end of this website is made with Bootstrap version 4.
and the web server of this site is apache tomcat.

### How does this website get data?
When you enter the https://pypiapp.ir you will see an input. This input will get a number and post 
it on Django view and view will request to api as the range of 0 to the entered number and get data 
from API then puts it as a context and passes it to template to show user.

## WebScraper
The data from kaggle website is scraped by using Selenium and Beautiful soap,
and it is posted to the API to show on website.
This scraper, scraped 9660 Application from kaggle website and posts it to API (https://pythonapp.ir/api/add).


## API 
This API is implemented with Django Rest Framework and has posted and gets methods to save scraped data from kaggle website and sends it to the website to show to users.
The API has 2 main Views:
1) Add Data <br>
2) SendData <br>

Add data view should be used to post data to api using following URL: https://pythonapp.ir/api/add <br>
Send data view should be used to get data from api using following URL: https://pythonapp.ir/api/get <br>
you should pass one parameter as data to send data view and that's the number of Applications that you want to get from API.