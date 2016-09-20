#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)

# Production
# sys.path.insert(0,"/var/www/html")
# from akadrone import app as application
#sys.path.insert(0,"/var/www/html/akadrone")
sys.path.insert(0,"/home/k/MySites/akadrone")
from  aka import app as application

application.secret_key = 'akadrone secret key'
