import requests
from html.parser import HTMLParser
from html.entities import name2codepoint
class LocationHandler(HTMLParser):
    """docstring for ClassName"""
    def __init__(self):
        HTMLParser.__init__(self)
        self.location = False
        self.date = False
        self.most_recent_event = False
        self.event_title = False
        self.event = False
        self.events = {}
    def handle_starttag(self, tag, attrs):
        def check_attrs(attrs,name):
             for x in attrs:
                 if x[1]==name:
                     return True
             return None
        if tag == 'div' and check_attrs(attrs,'most-recent-events'):
            self.most_recent_event = True
        if tag == 'h3' and check_attrs(attrs,'event-title') and self.most_recent_event:
            self.event_title = True
        if tag == 'a' and self.event_title and check_attrs(attrs,'/events/python-events/465/'):
            self.event = True
        if tag == 'span' and self.most_recent_event and check_attrs(attrs,'event-location'):
            self.location = True
        if tag == 'time' and self.most_recent_event and check_attrs(attrs,'2017-05-17T00:00:00+00:00'):
            self.date = True

        # if tag == 'a' and check_attrs(attrs,'/events/python-events/465/'):
        #     print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        #     self.event = True

    def handle_data(self, data):
        if self.event:
            print('..............',data)
            self.events['title'] = data
            self.event = False
        if self.date:
            print('..............',data)
            self.events['date'] = data
            self.date = False
        if self.location:
            print('..............',data)
            self.events['location'] = data
            self.location = False
            self.most_recent_event = False


def readLocation(url):
    headers = {}
    req = requests.get(url)
    s = req.text
    myparser = LocationHandler()
    myparser.feed(s)
    myparser.close()
    print(myparser.events)

if __name__=='__main__':
    readLocation('https://www.python.org/events/python-events/')
