"""
Created on Fri Nov 17 20:11:34 2017

@author: smechaab
"""

from currency_viewer import currency_viewer as cv

a = cv.CurrencyViewer()
a.process_c_viewer(log=True, currency="USD", time="rfc1123")  # time format: unixtime or rfc1123
