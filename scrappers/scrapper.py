import logging
import requests
from scrappers import coursera
import json

logger = logging.getLogger(__name__)


class Scrapper(object):
    def __init__(self, obj_count=10, skip_objects=None):
        self.skip_objects = skip_objects
        self.obj_count = obj_count

    def scrap_process(self, storage):

        # You can iterate over ids, or get list of objects
        # from any API, or iterate throught pages of any site
        # Do not forget to skip already gathered data
        # Here is an example for you


        storage.write_json(coursera.process_all_courses(self.obj_count))
