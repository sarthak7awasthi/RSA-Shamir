# RSA-Shamir

## Introduction:
This is a CLI program that creates an RSA key pair and shards (breaks up into pieces) the private key into k of n pieces using Shamir's secret sharing algorithm.

## Getting Started:
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Python3 and pip
You can download and find the instructions to install them through these links:

* [Python3](https://www.python.org/downloads/)
* [Pip](https://pip.pypa.io/en/stable/installing/)

### Installing
To install the other necessary packages: 
* Navigate to the repository on your terminal
```bash
cd RSA-Shamir
```
* Install all other dependencies:
```bash
pip install -r requirements.txt
```
* In case of failure of above command due to version mismatch of any dependency, comment out the particular dependency in 'requirements.txt' and install manually using the command below and re run the above command:
```bash
pip install <failed-dependency-name>
```

## Running the project

### Navigate to root folder
```bash
cd root
```
### run the program

```bash
python cliTool.py run app
```

## Run Test

```bash
python unitTest.py
```
