from bs4 import BeautifulSoup
import urllib2

response = urllib2.urlopen('https://webb-site.com/dbpub/listed.asp?exch=main&d=8/18/2015&sort1=codeup')

bsres = BeautifulSoup(response.read(), "html.parser")


