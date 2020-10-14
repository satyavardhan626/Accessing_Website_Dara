from urllib.request import urlopen
import re
import xlwt
from xlwt import Workbook

def main():
# open a connection to a URL using urllib2
   webUrl = urlopen("https://play.google.com/store/apps/details?id=com.monito&showAllReviews=true")

#get the result code and print it
   print("result code: " + str(webUrl.getcode()))

# read the data from the URL and print it
#    data = webUrl.read().decode("utf-8")
   data = webUrl.read()
   count =0;
   print("dddd",data)
   # paragraphs = re.findall(r'"(.*?)"',str(data))
   # print("paragraphs",paragraphs);




if __name__ == "__main__":
  main()