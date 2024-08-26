# Google Sheets Wrapper for Pyhton (by Antoine Eripret)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Package purpose and content
gspreadeasy is a wrapper around the gspread library to interact with Google Sheets. It provides an easy way to download, manipulate and upload data to Google Sheets. It is based on the gspread library, but it aims at providing a more user-friendly interface to interact with Google Sheets.

## Installation Instructions
First, install the package using:

`pip3 install git+https://github.com/antoineeripret/gspread_easy`

## Quickstart

- Create a service account JSON file
- Create a new project in the Google Developers Console,
- Enable the Google Sheets API under "APIs & Services".
- Create a Service Account in the Credentials tab.
- Download the JSON file containing the credentials of the service account.
- Share the Google Sheet you want to interract with with the email of the service account.

## Usage

1/ Import the package using this simple command:

```python 
import gspreadeasy as gse 
```
2/ Create a GoogleSheetClient object:

```python 
client = (
    gse
    .GoogleSheetClient(
        #path to the service account JSON file
        'service_account.json', 
        #id of the google sheet
        "12ChNlin-QV0-RWlcYLjLhs98wLQ47XNe6EA_WSD8j4o"
    )
) 
```
A spreadsheet ID can be extracted from its URL. For example, the spreadsheet ID in the URL https://docs.google.com/spreadsheets/d/abc1234567/edit#gid=0 is "abc1234567".

3/ Interract with the Google Sheets documents

You can download the data from the Google Sheets document using the get_data_from_googlesheet method:

```python 
#method to get the data from the Google Sheets document
data.get_data_from_googlesheet("Flight Airlines")
#method to show the data downloaded from the Google Sheets document
data.show_data()
```
You can also override the data in the Google Sheets document using the override_data_in_googlesheet method:
```python 
#method to override the data in the Google Sheets document
#if you don't give a dataframe, the data will be the one downloaded from the Google Sheets document
#stored in the GoogleSheetClient object (self.df) 
#The first parameter is the name of the sheet you want to override
data.override_data_in_googlesheet("Data", df)
```