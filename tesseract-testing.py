# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 17:37:20 2021

@author: gar20
"""

import pytesseract
import pkg_resources

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
print(pkg_resources.working_set.by_key['pytesseract'].version)