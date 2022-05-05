Needed to start the Django project :
Django 3.2.2 or more --> python -m pip install Django
mysqlclient --> pip install mysqclient
An SQL database, the name of the database has to be the same as the database name in Dj_Genevis/settings.py
This site  was designed to work with a database modeled similarly to Geneview(2018).

To create the GeneView database and the few modifications needed for this project :
ALTER TABLE `abbreviations` ADD id int NOT NULL AUTO_INCREMENT primary key;
ALTER TABLE `cells` ADD id int NOT NULL AUTO_INCREMENT primary key;
ALTER TABLE `chemicals` ADD id int NOT NULL AUTO_INCREMENT primary key;
ALTER TABLE `dates` ADD id int NOT NULL AUTO_INCREMENT primary key;
ALTER TABLE `diseases` ADD id int NOT NULL AUTO_INCREMENT primary key;
ALTER TABLE `enzymes` ADD id int NOT NULL AUTO_INCREMENT primary key;
ALTER TABLE `genes` ADD id int NOT NULL AUTO_INCREMENT primary key;
ALTER TABLE `histones` ADD id int NOT NULL AUTO_INCREMENT primary key;
ALTER TABLE `mutations` ADD id int NOT NULL AUTO_INCREMENT primary key;
ALTER TABLE `species` ADD id int NOT NULL AUTO_INCREMENT primary key;
ALTER TABLE `tissues` ADD id int NOT NULL AUTO_INCREMENT primary key;

To start the server : 
Open the terminal and move into the root folder of this project, you should see manage.py in this folder.
$ python manage.py runserver

URL to access the homepage : 
http://127.0.0.1:8000/genevis/
