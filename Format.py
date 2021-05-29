import json


def extract_element_from_json(obj, path):
    '''
    Source: https://bcmullins.github.io/parsing-json-python/
    Extracts an element from a nested dictionary or
    a list of nested dictionaries along a specified path.
    If the input is a dictionary, a list is returned.
    If the input is a list of dictionary, a list of lists is returned.
    obj - list or dict - input dictionary or list of dictionaries
    path - list - list of strings that form the path to the desired element
    '''
    def extract(obj, path, ind, arr):
        '''
            Extracts an element from a nested dictionary
            along a specified path and returns a list.
            obj - dict - input dictionary
            path - list - list of strings that form the JSON path
            ind - int - starting index
            arr - list - output list
        '''
        key = path[ind]
        if ind + 1 < len(path):
            if isinstance(obj, dict):
                if key in obj.keys():
                    extract(obj.get(key), path, ind + 1, arr)
                else:
                    arr.append(None)
            elif isinstance(obj, list):
                if not obj:
                    arr.append(None)
                else:
                    for item in obj:
                        extract(item, path, ind, arr)
            else:
                arr.append(None)
        if ind + 1 == len(path):
            if isinstance(obj, list):
                if not obj:
                    arr.append(None)
                else:
                    for item in obj:
                        arr.append(item.get(key, None))
            elif isinstance(obj, dict):
                arr.append(obj.get(key, None))
            else:
                arr.append(None)
        return arr
    if isinstance(obj, dict):
        return extract(obj, path, 0, [])
    elif isinstance(obj, list):
        outer_arr = []
        for item in obj:
            outer_arr.append(extract(item, path, 0, []))
        return outer_arr


class Format:
    def __init__(self) -> None:
        pass


class OldFormat(Format):
    def __init__(self, json_string):
        obj = json.loads(json_string)
        self.address = str(extract_element_from_json(obj, ['address'])[0])
        self.content_seasons_text = extract_element_from_json(obj, ['content', 'seasons', 'text'])
        self.content_description = str(extract_element_from_json(obj, ['content', 'description'])[0])
        self.id = str(extract_element_from_json(obj, ['id'])[0])
        self.author_username = str(
            extract_element_from_json(obj, ['author', 'username'])[0])
        self.author_id = str(
            extract_element_from_json(obj, ['author', 'id'])[0])
        self.created = str(extract_element_from_json(obj, ['created'])[0])
        self.updated = str(extract_element_from_json(obj, ['updated'])[0])
        self.counters_A = int(
            extract_element_from_json(obj, ['counters', 'A'])[0])
        self.counters_B = int(
            extract_element_from_json(obj, ['counters', 'B'])[0])
    
    def getAddress(self):
        return self.address

    def getContentSeasonsText(self):
        return self.content_seasons_text

    def getContentDescription(self):
        return self.content_description

    def getId(self):
        return self.id

    def getAuthorUsername(self):
        return self.author_username

    def getAuthorId(self):
        return self.author_id

    def getCreated(self):
        return self.created

    def getUpdated(self):
        return self.updated

    def getCounters_A(self):
        return self.counters_A

    def getCounters_B(self):
        return self.counters_B


class NewFormat(Format):
    def __init__(self):
        self.path = None
        self.seasons = None
        self.body = None
        self.id = None
        self.author_name = None
        self.author_id = None
        self.created_date = None
        self.created_time = None
        self.updated_date = None
        self.updated_time = None
        self.counters_total = None

    def setPath(self, path):
        self.path = path

    def setSeasons(self, seasons):
        self.seasons = seasons

    def setBody(self, body):
        self.body = body

    def setId(self, id):
        self.id = id

    def setAuthorName(self, author_name):
        self.author_name = author_name

    def setAuthorId(self, author_id):
        self.author_id = author_id

    def setCreatedDate(self, created_date):
        self.created_date = created_date

    def setCreatedTime(self, created_time):
        self.created_time = created_time

    def setUpdatedDate(self, updated_date):
        self.updated_date = updated_date

    def setUpdatedTime(self, updated_time):
        self.updated_time = updated_time

    def setCountersTotal(self, counters_total):
        self.counters_total = counters_total


j = '''{"address" : "https://www.google.com ","content" : {"seasons" : [{"text": "winter"},{"text": "spring"},{"text": "summer"},{"text": "autumn"}],"description" : "All seasons"},"updated" : "2021-02-26T08:21:20+00:00","author" : {"username" : "Bob","id" : "68712648721648271"},"id" : "543435435","created" : "2021-02-25T16:25:21+00:00","counters" : {"A" : 3,"B" : 0},"type" : "main"}'''
o = OldFormat(j)
print(o.counters_B)
