#!/usr/bin/env python
import argparse

parser = argparse.ArgumentParser(description='Convert from CSV file to markdown text')
parser.add_argument('file', type=str, help='the CSV file')
parser.add_argument('--delimiter', default=",",
                   help='delimiter character')
parser.add_argument('--hasHeader', action='store_true', default=False,
                   help='CSV content has header row?')

args = parser.parse_args()
csv_path = args.file
delimiter = args.delimiter
hasHeader = args.hasHeader

with open(csv_path, 'rU') as f_obj:
  csvContent = f_obj.read()
if delimiter != '\t' :
  csvContent = csvContent.replace('\t', '    ')
columns = csvContent.split('\n')
tabularData = []
maxRowLen = []
for i, e in enumerate(columns):
  try:
    tabularData[i]
  except IndexError:
    tabularData.append([])
  row = e.split(delimiter)
  for ii, ee in enumerate(row):
    try:
      maxRowLen[ii]
    except IndexError:
      maxRowLen.append(0)
    maxRowLen[ii] = max(maxRowLen[ii], len(ee))
    try:
      tabularData[i][ii]
    except IndexError:
      tabularData[i].append([])
    tabularData[i][ii] = ee
headerOutput = ''
seperatorOutput = ''
for length in maxRowLen:
  spacer = '-'.join(['']*(length + 1 + 2))
  seperatorOutput += '|' + spacer
  spacer = ' '.join(['']*(length + 1 + 2))
  headerOutput += '|' + spacer

headerOutput += '| \n'
seperatorOutput += '| \n'

if hasHeader:
  headerOutput =''

rowOutput = ""
initHeader = True
for col in tabularData:
  for y, length in enumerate(maxRowLen):
    try:
      row = col[y]
    except IndexError:
      row = ""
    spacing = " ".join(['']*(length - len(row) + 1))
    if hasHeader and initHeader:
      headerOutput += "| " + row + spacing + " "
    else:
      rowOutput += "| " + row + spacing + " "

  if hasHeader and initHeader:
    headerOutput += "| \n"
  else:
    rowOutput += "| \n"

  initHeader = False

print (headerOutput + seperatorOutput + rowOutput)
