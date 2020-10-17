! pip install html-to-csv
! html2csv table.html -o table.csv

# converting csv to required form
import pandas
import csv
 
with open('table.csv', 'r') as csv_file: 
 from pandas import DataFrame
 result = pandas.read_csv('table.csv')
 result.to_csv('output.html.csv', sep='#', index=False)
