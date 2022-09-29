#https://github.com/saldejummi/norwegian_txt2csv
import re

FILENAME_SOURCE = '2019.txt'
FILENAME_DESTINATION = '2019.csv'

with open(FILENAME_SOURCE, 'r') as source:
    with open(FILENAME_DESTINATION, 'w') as destination:
        destination.write('text, date, amount, points')
        csvLinesToWrite = 0
        for line in source:
            searchObject = re.search('Purchase', line)
            if csvLinesToWrite:
                punctuated = re.sub(',', '.', line.strip())
                destination.write(', ' + punctuated)
                csvLinesToWrite -= 1
            if searchObject:
                destination.write('\n' + line.strip())
                csvLinesToWrite += 3

with open(FILENAME_DESTINATION, 'r') as f:
    points = 0
    for line in f:
        searchObject = re.search(',.*,.*, (.*)', line)
        if searchObject.group(1) == 'points':
            continue
        else:
            try:
                points += int(float(searchObject.group(1)) * 100)
            except:
                #points += int(float(searchObject.group(1).replace('\U00002013', '-')) * 100)
                replacedAllNonASCCIIchars = re.sub(r'[^\x00-\x7F]+','-', searchObject.group(1))
                points += int(float(replacedAllNonASCCIIchars) * 100)
    print(points / 100)