# norwegian_txt2csv

How to get your yearly cash point text file that can be converted into csv and then get the total cash points expiring:
1. Go to Bank Norwegian website
2. Go to My Page tab
3. Click CashPoints
4. Click CashPoints events
5. The URL varies from country to country. You should now be on an URL like this https://www.banknorwegian.??/ownpage/cashback/transactions/cp/
6. Choose the year e.g. 2020 that has cash points that expire at the end of 2022 (cash points expire after two years at the end of that year)
7. Ctrl+a Ctrl+c Ctrl+v the whole page into an empty txt file on same folder where you have norwegian_txt2csv.py
8. Name the txt file 2020.txt
9. Run norwegian_txt2csv.py
10. You will get 2020.csv file as output and a sum of your expiring cash points on python console
