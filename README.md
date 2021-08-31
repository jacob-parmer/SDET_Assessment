# SDET_Assessment
A test suite example

## Requirements
- Python 3.8.5
- pytest 6.2.5
- selenium 3.141.0
- Google chrome and matching [chromedriver installed to PATH](https://sites.google.com/a/chromium.org/chromedriver/downloads)
 
## Running the test suite
To run the full test suite:
> python3 -m pytest test/ --browser Chrome

To run a specific file:
> python3 -m pytest test/test_registration.py --browser Chrome \
> OR \
> python3 -m pytest test/test_webtables.py --browser Chrome

To run a specific test:
> python3 -m pytest test/test_registration.py --browser Chrome -k 'test_registration_valid' \
> OR \
> python3 -m pytest test/test_registration.py --browser Chrome -k 'test_registration_invalid' 
