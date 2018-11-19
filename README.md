# MonetDB Visualizer

MonetDB Visualizer is a tool for exploring monetdb column store database along with multiple functionalities of Data Manipulation & Data Creation.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
Install requires below dependecies to be installed before getting started with software
* Linux - Ubuntu 16.04 LTS
* Python3
* PyQt5
* PyQt5-sip
* pymonetdb

### Installing

A step by step series of commands to install all the prerequisites, skip this step as everything will be installed by 
* Add Monetdb Repository
	```
	sudo apt-add-repository "deb http://dev.monetdb.org/downloads/deb/ xenial monetdb"
	```
* Download Monetdb GPG KEY
	```
	wget --output-document=- https://www.monetdb.org/downloads/MonetDB-GPG-KEY | sudo apt-key add -
	```
* Update System
	```
	sudo apt-get update
	```
* Install MonetDB SQL & MonetDB-Client Linux Daemon
	```
	sudo apt-get install -y --allow-unauthenticated monetdb5-sql monetdb-client
	```
* Install pymonetdb
	```
	sudo pip3 install pymonetdb, pyqt5
	```
###Reference Link
	https://www.monetdb.org/Documentation/UserGuide/Tutorial


## Directory Structure

* **src**
	- **main** : Main File containing application code  
 	- **lib** : Lib files for Monetdb interface & PyQt Files
		- **ddlalter.py** : GUI Page for DDL --> Alter
		- **ddlcreate.py** : GUI Page for DDL --> Create
		- **ddldrop.py** : GUI Page for DDL --> Drop
		- **dmlinsert.py** : GUI Page for DML --> Insert
		- **dmlupdate** : GUI Page for DML --> Update
		- **dmldelete** : GUI Page for DML --> Delete
		- **monetdb_interface** : Library module for MonetDB Database communication
		
### Additional Information

* Programming language - Python
* Language Vesion - Python3.6
* MonetDB Python Library - pymonetdb
* User Interface- PyQt5

## Deployment

* Download source code git repo
	```
	git clone https://github.com/.......git
	cd ethernetip
	python3 setup.py install 
	```

### Executing Application
* Enter in to the directory where software is installed
	```
	python3 main.py
	```

### Important Notes
> When executing by command terminal will show logs and debug messages
> Log files are created at '/var/log/dattus/'  
 	- 'mdvisual_logger.log' - Debug and Info logging file
	- 'mdvisual_error.log' - Error logging file
> Refer to documentation in /doc direcotry, for detailed description on software

### Documentation
For detailed information regarding software refer the link below
[Documentation](./docs/html/index.html)


## Versioning
* Firmware Version - 1.0.0

## Authors

* **Nisarg Pandya** - *Initial work*

See also the list of [URL](https://github.com/...) who contributed in this project.

## License
* LGPL




