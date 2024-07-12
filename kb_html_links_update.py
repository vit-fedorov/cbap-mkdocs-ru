#!/usr/bin/env python3
from getpass import getpass
import mysql.connector
import bs4
import html
import re
import json

conn = mysql.connector.connect(host='ssh:192.168.255.7', database='phpkbv9',
	user='html_import',
	password=getpass("Password for phpkbv9:"))

