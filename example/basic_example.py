# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 20:11:34 2017

@author: smechaab
"""
#from CurrencyViewer import CurrencyViewer as cv
from currency_viewer import currency_viewer as cv

a = cv.CurrencyViewer()
a.processCViewer(log=True, currency="USD", time="rfc1123") #time format: unixtime or rfc1123
a.displayResults()
