import threading
from queue import Queue
from spider import Spider
from domain import *
from main import *

PROJECT_NAME = "TheDistrict"
HOMEPAGE = "http://www.menshealth.co.uk/"
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + "/queue.txt"
CRAWLED_FILE = PROJECT_NAME + "/crawled.txt"
NUMBER_OF_THREADS = 8

queue = Queue()

Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)
