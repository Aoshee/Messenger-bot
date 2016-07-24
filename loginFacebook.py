import urllib2
import urllib
from bs4 import BeautifulSoup
import cookielib
import re


def getInfoPhone(uid):

   email = 'yuri.ivonorf@gmail.com'
   passw = 'Huyen1408'

   cj = cookielib.CookieJar()
   opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
   opener.addheaders = [('User-agent', 'Mozilla/5.0')]

   auth = urllib.urlencode({'email':email,'pass':passw})

   link = 'https://m.facebook.com/login.php'
   data = opener.open(link,data=auth)
   link2 = "https://m.facebook.com/profile.php?v=info&id=" + uid + "&nocollections=1"
   data2 = opener.open(link2).read()
   if "ltr" in data2:
       print "ok"

   page_source = BeautifulSoup(data2, "lxml")
   num in page_source.findAll('span', attrs={'dir': 'ltr'})
   phone = re.sub(r'\D', "", str(num))
   return phone
