# Addressline Code Challenge

This is a command line utility using Python standard libraries to parse street addresses in the
country schemes DE, ES, FR, and US.

# Prerequisites
* Python and Pip, minimum version 3.11.4

# Installation
```
pip install -r requirements.txt
```

## Run the cli
Example for parsing an address (simple address profile) - open a command line prompt, change to the
project directory and execute:
```
python main.py "Matias Delgado 1903"
```
### Output
```
{"street": "myaddress", "housenumber": "1903"}
```

## Run Unittest
```
coverage run -m unittest discover
```
## See Coverage
```
coverage report -m
```

# Notes
- According to the Wikipedia and other trustworthy websites 
addresses are written in order from most specific to general but format of address is depend to country and area.
To reach more accurate extracted data from raw address is best to use NLP library.
- Instead of using public libraries to parse address and writing API, 
I created a simple cli command and some classes with using regex (which is not good for performance or maintainability) which can improve by using 
large frameworks like pyspark, pandas and fastapi.

# Additional Notes
- If I had a more time to complete this challenge I would go with https://github.com/openvenues/libpostal library with using containerization. 