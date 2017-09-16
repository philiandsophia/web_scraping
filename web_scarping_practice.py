# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import webbrowser
import sys
import pyperclip
import requests
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#webbrowser.open('http://google.ca')
#opens the given url

#this program will get street address from the comman lin arguments or clipboard
#and open the web browser to the Google Maps for the address

#sys.argv is a list in python, which contains the command-line arguemnts passed to the sciprt


#if len(sys.argv) > 1:
    #get address from commnad line.
    #address = ' '.join(sys.argv[1:])
    #join all the element of list
#else:
    #get address from clipboard
    #address = pyperclip.paste()

#you will need to put in somthing like C:\> web_scarping_practice Valencia St, San Francisco, CA 94110

#address = pyperclip.paste()
#I couldn't get the sys.argv thing to work
#webbrowser.open('http://www.google.ca/maps/place/' +address)

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
#print (type(res))
#returns <class 'requests.models.Response'>

#res.status_code == requests.codes.ok
#check request for this web page succeeded

#print (res.text) the web page is stored as string in Reponse's object text variable
#print the text of the webpage

#reddit = requests.get('https://www.reddit.com/r/Showerthoughts/comments/6xmu62/the_other_day_someone_said_newtons_rolling_over/')
#print (reddit.text[:250]) #print first 250 characters

#res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
#res.raise_for_status()
#raise exception if there is an error downlaoding file

##res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
##try:
##    res.raise_for_status()
##except Exception as exc:
##    print('There was a problem: %s' % (exc))
#the program doesn't crash but the output will say there was a client error

##res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
##res.raise_for_status()
##playFile = open('RomeoAndJuliet.txt','wb')
##for chunk in res.iter_content(100000):
##    playFile.write(chunk)
##
##playFile.close()

#1.Call requests.get() to download the file
#2.Call open() with 'wb' to create a new file in write binary mode
#3.Loop over the response object's iter_content() method
#4.Call write() on each iteration to write the content to the file
#5.Call close() to close the file
#one hundred thousand byte is generally a good size to pass into iter_content

#res = requests.get('http://nostarch.com')
#res.raise_for_status()
#noStarchSoup = BeautifulSoup(res.text)
#exampleFile = open('example.html')
#exampleSoup = BeautifulSoup(exampleFile.read())
#elems = exampleSoup.select('#author')
#print (elems[0].getText())
#print (str(elems[0]))
#print (elems[0].attrs)

#pElems = exampleSoup.select('p')
#print (str(pElems[0]))
#print (pElems[1].getText())

#getText gets the text in between the tags, and str gets the text and the tags
#some example of selector:
##soup.select('div')
##
##All elements named <div>
##
##soup.select('#author')
##
##The element with an id attribute of author
##
##soup.select('.notice')
##
##All elements that use a CSS class attribute named notice
##
##soup.select('div span')
##
##All elements named <span> that are within an element named <div>
##
##soup.select('div > span')
##
##All elements named <span> that are directly within an element named <div>, with no other element in between
##
##soup.select('input[name]')
##
##All elements named <input> that have a name attribute with any value
##
##soup.select('input[type="button"]')
##
##All elements named <input> that have an attribute named type with value button

#spanElem = exampleSoup.select('span')[0]
#print (str(spanElem))
#print (spanElem.get('id'))

#use get to access attribute values

#browser = webdriver.Firefox()
#print (type(browser))
#browser.get('http://inventwithpython.com')

##browser.find_element_by_class_name(name)
##browser.find_elements_by_class_name(name)
##Elements that use the CSS class name
##
## browser.find_element_by_css_selector(selector)
##browser.find_elements_by_css_selector(selector)
##Elements that match the CSS selector
##
## browser.find_element_by_id(id)
##browser.find_elements_by_id(id)
##Elements with a matching id attribute value
##
## browser.find_element_by_link_text(text)
##browser.find_elements_by_link_text(text)
##<a> elements that completely match the text provided
##
## browser.find_element_by_partial_link_text(text)
##browser.find_elements_by_partial_link_text(text)
##<a> elements that contain the text provided
##
## browser.find_element_by_name(name)
##browser.find_elements_by_name(name)
##Elements with a matching name attribute value
##
## browser.find_element_by_tag_name(name)
##browser.find_elements_by_tag_name(name)
##Elements with a matching tag name (case insensitive; an <a> element is matched by 'a' and 'A')


##Attribute or method
##
##Description
##
##tag_name
##
##The tag name, such as 'a' for an <a> element
##
##get_attribute(name)
##
##The value for the element’s name attribute
##
##text
##
##The text within the element, such as 'hello' in <span>hello</span>
##
##clear()
##
##For text field or text area elements, clears the text typed into it
##
##is_displayed()
##
##Returns True if the element is visible; otherwise returns False
##
##is_enabled()
##
##For input elements, returns True if the element is enabled; otherwise returns False
##
##is_selected()
##
##For checkbox or radio button elements, returns True if the element is selected; otherwise returns False
##
##location
##
##A dictionary with keys 'x' and 'y' for the position of the element in the page

##browser.get('http://inventwithpython.com')
##try:
##    elem-browser.find_element_by_class_name("bookcover")
##    print ('Found {} element with that class name!'.format(elem.tag_name))
##
##except:
##    print ('was not able to find an element with that name')

#browser = webdriver.Firefox()
#browser.get('http://inventwithpython.com')
#linkElem = browser.find_element_by_link_text('Read It Online')
#linkElem.click()
#this clicks the elemnt with link Read it Online

##browser = webdriver.Firefox()
##browser.get('http://mail.yahoo.com')
##emailElem = broswer.find_element_by_id('login-singin')
##emailELem.send_keys('not_my_real_email')


##Attributes
##
##Meanings
##
##Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT
##
##The keyboard arrow keys
##
##Keys.ENTER, Keys.RETURN
##
##The ENTER and RETURN keys
##
##Keys.HOME, Keys.END, Keys.PAGE_DOWN, Keys.PAGE_UP
##
##The home, end, pagedown, and pageup keys
##
##Keys.ESCAPE, Keys.BACK_SPACE, Keys.DELETE
##
##The ESC, BACKSPACE, and DELETE keys
##
##Keys.F1, Keys.F2,..., Keys.F12
##
##The F1 to F12 keys at the top of the keyboard
##
##Keys.TAB
##
##The TAB key

##browser = webdriver.Firefox()
##browser.get('http://nostarch.com')
##htmlElem = browser.find_element_by_tag_name('html')
##htmlElem.send_keys(Keys.END)
##htmlElem.send_keys(Keys.HOME)

##browser.back(). Clicks the Back button.
##
##browser.forward(). Clicks the Forward button.
##
##browser.refresh(). Clicks the Refresh/Reload button.
##
##browser.quit(). Clicks the Close Window button.
##
