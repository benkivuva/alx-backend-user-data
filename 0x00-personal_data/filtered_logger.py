#!/usr/bin/env python3
"""
This project module contains several fucntions
to work with the personal data
"""
import re

def filter_datum(fields, redaction, message, separator):
    #result = re.sub(fields, redaction, message)
    for f in fields:
        result = re.sub(f, redaction, message) 
    """print(fields)
    print(type(fields))
    print(redaction)
    print(type(redaction))
    print(message)
    print(type(message))
    print(separator)
    print(type(separator))
    #return message"""
    return result
