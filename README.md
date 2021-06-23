# BlueBuilding

## Objectives
BlueBuilding is a web application that aims to apply various concepts of web development in practice, especially the use of APIs. This web application intends to collect various data about cryptocurrencies and transform them into an updated report.

## Description
One of the highlights of this application is the use of APIs to get data. Another is the possibility for the user to register and be able to save their cryptocurrencies and view reports more easily. Reports are updated whenever the user requests the view.

When the user chooses a cryptocurrency and requests the creation of the report, the web application uses the coinmarketcap.com API to get the updated data. After get all the data, the web application formats this data generating a report with all the information available on the coinmarketcap.com website.

![image](https://user-images.githubusercontent.com/34349410/123152714-c4470300-d45c-11eb-9ccb-159b370c4346.png)

There are two different ways for a user to view reports. If the user is not registered, he must provide his name and select the cryptocurrency. If the user is registered, he accesses his dashboard that contains the list of all the user's cryptocurrencies.

One of the biggest challenges of this project was the development of functions to request the data, extract it from the corresponding JSON and then format it correctly.

## Features
-	Detailed information on the Top 100 Cryptocurrencies;
-	Reporting with updated data in real time;
-	User space with selected cryptocurrencies;
-	Responsive design adapting to PC, Tablet or Mobile screens.

Technical Features:
-	Responsive design developed with Bootstrap & HTML, CSS and JavaScript.
-	Server side developed in Python, using Django Framework;
-	For the database, SQLite3 was used;
-	The Web App uses the Heroku platform for Deployment;
-	API designed to get data from coinmarketcap.com website..

## How to Use
To use BlueBuilding just access https://bluebuilding.herokuapp.com/ and follow the guidelines on the home page.

## Credits
This web application was entirely developed by me, using my knowledge acquired along my journey as a software developer.

## Project Status
The development of this web application can be considered finished. The project fulfilled the expected objectives. Eventually the project can be resumed based on new goals for the web application.
