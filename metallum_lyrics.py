from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import ActionChains
import re
import urllib.request as urllib
import time
opt = Options()
opt.headless = True
#plik = open("prof2.html","r")
#fragment = plik.readlines()
#string_fr = str(fragment)
regexpHandler = re.compile('<td class=" sorting_1">(.*?)</td>')
#result = regexpHandler.findall(string_fr)
bandf = re.compile('<dt>Lyrical themes:</dt>\\\\n<dd>(.*?)</dd>')
genre_f = re.compile('<dt>Genre:</dt>\\\\n<dd>(.*?)</dd>')
extURL = re.compile('"(.*?)"')
regexBandName = re.compile('">(.*?)</a>')
#max_counter = len(regexpHandler.findall(string_fr))
znalezione = open("filtered_bands.txt","w")
driver = webdriver.Firefox(options=opt)
#driver = webdriver.Firefox()
driver.get("https://www.metal-archives.com/lists/black")
time.sleep(3)

html_source = driver.page_source
#print (html_source)
#print(type(html_source))
counter = 0
max = 73
while counter < max:
 counter2 = 0
 html_source = driver.page_source
 result = regexpHandler.findall(html_source)
 while counter2 < 500:
      result2 = extURL.findall(result[counter2])
      url = result2[0]
      req = urllib.Request(url, headers={'User-Agent' : "Magic Browser"})
      con = urllib.urlopen(req)
      band = str(con.read())
      bandname = regexBandName.findall(result[counter2])
      th = str(bandf.findall(band))
      genre =  genre_f.findall(band)
      counter2 = counter2 + 1
      if any(re.findall(r'Misanthropy|Nihilism|Blasphemy|Profanation|Profanity',th, re.IGNORECASE)):
       print ("-----------------")
       print ("Band: ", bandname)
       print ("Genre: ", genre)
       print ("Lyrical theme: ", th)
       znalezione.write( "----------------------------------------------" +"\n")
       znalezione.write( "Band: " +str(bandname)  +"\n")
       znalezione.write( "Genre: " +str(genre)  +"\n")
       znalezione.write( "Lyrical theme: " +str(th)  +"\n")
      else:
       c = 0
 counter = counter + 1
 driver.find_element_by_xpath('//*[@id="bandListGenre_next"]').click()
 time.sleep(5)
