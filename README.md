# hpdf - Week 1

This repository contains the solution of tasks for week 1 of hasura product development fellowship.

## Getting Started
Follow these instructions to setup your environment to test the app.
#### Install Git
To check if git is installed.
```
$ git --version
```
If not installed.
##### For MacOs
Download latest [Git for MacOs Installer](https://sourceforge.net/projects/git-osx-installer/files/)
##### For Windows
Download the latest [Git for Windows installer](https://git-for-windows.github.io/).
##### For Linux
 Debian / Ubuntu (apt-get)
```
$ sudo apt-get update
$ sudo apt-get install git
```
Fedora (dnf/yum)
```
$ sudo dnf install git
```
or for older versions
```
$ sudo yum install git
```
#### Cloning the repository
To clone the repository enter the following command in your terminal or command prompt
```
$ git clone https://github.com/AkshayRaman97/hpdf-week1.git
```
A local clone of the repository will be done in the current working directory.
### Prerequisites
The packages needed to run the app are :
* Python 3.x
* pip3
* Flask
* requests - python library

### Installations
##### 1. Python
Check if python3 is already installed using the following command.
```
$ python3 --version
```
If installed proceed with next installation, else follow below instructions for the appropriate OS.

###### For Linux
Enter following commands in terminal.
```
$ sudo apt-get update
$ sudo apt-get install python3.6
```
###### For MacOS
Enter following commands in terminal.
To install brew
```
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
Now, we can install Python 3:
```
$ brew install python3
```
###### For Windows
Use the following link to download Python3.6
https://www.python.org/downloads/
##### 2. pip3
Check if pip3 is installed using by entering following command in the terminal
```
$ pip3 --version
```
If not installed, perform the installations accordingly.
###### For Linux
Enter following commands in terminal.
```
$ sudo apt-get update
$ sudo apt-get install python3-pip
```
###### For MacOs
pip3 is installed along with python3 when using brew.
```
$ brew install python3
```
##### For Windows
pip3 is installed along with python3 installation.

#### 3. Flask
Once python3 and pip3 are installed we can proceed with installing Flask.
```
$ pip3 install flask
```
All the necessary dependencies are installed along with Flask.
You can check for all installed packages using.
```
$ pip3 freeze
```
#### 4. requests library
In order for the app to work properly the requests library is needed to be installed. Install using 
```
$ pip3 install requests
```

## Running the App
In order to run the app make sure you are in the hpdf-week1 directory and run the following command in the terminal or command prompt:
```
$ python3 app.py
```
You should the following in your terminal
```
 * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 175-751-846
```
If not, make sure you followed the installation procedure properly.
To test the app open the browser and type the url.
```
http://127.0.0.1:8080/
```
Click on provided links to view each task.
### Authors
* **Akshay Raman** - [*GitHub Profile*](https://github.com/AkshayRaman97)
###### Thank you!









