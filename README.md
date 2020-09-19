This project focuses on predicting APPLE stock price on real time data. I used past 10 years worth of historical APPLE stock data for training and built an effective model for predicting stock prices and displayed the predictions on webpage using Flask, Kafka and Highcharts.


After creating and uploading my CSV file, I fetched the file from my S3 bucket with the help of Pandas. Since no data is clean and has missing values, it needs to be cleaned.

The model building process has been done using PySpark’s mlib Library.

~PySpark
I used Linear Regression to train the model and used the Regression Evaluator to give the accuracy of my model.


~Alpha Vantage Inc. is a company that provides realtime and historical stock APIs.

~Kafka is a distributed publish-subscribe messaging system and a robust queue that can handle a high volume of data and enables you to pass messages from one end-point to another
To display the prediction in real time, we first need to start the Zookeeper server and then start the Kafka server.
I created the Producer and Consumer scripts in Python3 and ran them through Flask app.

~Flask is a web application framework written in Python
To display the graph I used Highcharts JS in my HTML file and styled it through CSS.

~S3FS is a PyFilesystem interface to Amazon S3 cloud storage 
~The abstraction offered by FS objects means that you can write code that is agnostic to where your files are physically located. For instance, if you wrote a function that searches a directory for duplicates files, it will work unaltered with a directory
~As long as an FS object exists for your chosen filesystem (or any data store that resembles a filesystem), you can use the same API. This means that you can defer the decision regarding where you store data to later. If you decide to store configuration in the cloud, it could be a single line change and not a major refactor.

_ createBucket.py file. This will create the bucket in the AWS S3.
_ uploadFile.py file. This will upload the CSV file in my bucket.
_  fetchFile.py file. This will fetch the CSV file from my bucket.
-  dataCleanser.py file. This is clean the data in CSV file.
- buildingmodel.py file. This will build the model based on the data and save the model. It will be saved in the project folder named AppleStockModel.