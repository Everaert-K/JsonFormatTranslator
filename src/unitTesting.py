import unittest

from Format import OldFormat
from Format import NewFormat
from translate import TranslatorOldToNew
from db import database
from AbsentError import AbsentError


class TestTranslatingMethods(unittest.TestCase):

    def testJsonReading(self):
        # checking if JSON file is read correctly
        old = OldFormat(
            '''{"address" : "https://www.google.com","content" : {"seasons" : [{"text": "winter"},{"text": "spring"},{"text":  "summer"},{"text": "autumn"}],"description" : "All seasons"},"updated" : "2021-02-26T08:21:20+00:00","author" :  {"username" : "Bob","id" : "68712648721648271"},"id" : "543435435","created" : "2021-02-25T16:25:21+00:00","counters" : {"A" : 3,"B" : 0},"type" : "main"}''')
        self.assertEqual(old.getAddress(), 'https://www.google.com')
        self.assertEqual(old.getContentSeasonsText(), [
                         "winter", "spring", "summer", "autumn"])
        self.assertEqual(old.getContentDescription(), "All seasons")
        self.assertEqual(old.getId(), "543435435")
        self.assertEqual(old.getAuthorUsername(), "Bob")
        self.assertEqual(old.getAuthorId(), "68712648721648271")
        self.assertEqual(old.getCreated(), "2021-02-25T16:25:21+00:00")
        self.assertEqual(old.getUpdated(), "2021-02-26T08:21:20+00:00")
        self.assertEqual(old.getCounters_A(), 3)
        self.assertEqual(old.getCounters_B(), 0)

    def testIncompleteJsonReading(self):
        old = OldFormat('''{"content" : {"seasons" : [{"text": "winter"},{"text": "spring"},{"text":  "summer"},{"text": "autumn"}],"description" : "All seasons"},"updated" : "2021-02-26T08:21:20+00:00","author" :  {"username" : "Bob","id" : "68712648721648271"},"id" : "543435435","created" : "2021-02-25T16:25:21+00:00","counters" : {"A" : 3,"B" : 0},"type" : "main"}''')
        self.assertEqual(old.getAddress(), 'None')
        self.assertEqual(old.getContentSeasonsText(), [
                         "winter", "spring", "summer", "autumn"])
        self.assertEqual(old.getContentDescription(), "All seasons")
        self.assertEqual(old.getId(), "543435435")
        self.assertEqual(old.getAuthorUsername(), "Bob")
        self.assertEqual(old.getAuthorId(), "68712648721648271")
        self.assertEqual(old.getCreated(), "2021-02-25T16:25:21+00:00")
        self.assertEqual(old.getUpdated(), "2021-02-26T08:21:20+00:00")
        self.assertEqual(old.getCounters_A(), 3)
        self.assertEqual(old.getCounters_B(), 0)

    def testTranslatingJson(self):
        old = OldFormat('''{"address" : "https://www.google.com","content" : {"seasons" : [{"text": "winter"},{"text": "spring"},{"text":  "summer"},{"text": "autumn"}],"description" : "All seasons"},"updated" : "2021-02-26T08:21:20+00:00","author" :  {"username" : "Bob","id" : "68712648721648271"},"id" : "543435435","created" : "2021-02-25T16:25:21+00:00","counters" : {"A" : 3,"B" : 0},"type" : "main"}''')
        new = TranslatorOldToNew.translate(old)
        self.assertEqual(new.path, "https://www.google.com")
        self.assertEqual(new.seasons, [
                         "winter", "spring", "summer", "autumn"])
        self.assertEqual(new.body, "All seasons")
        self.assertEqual(new.id, "543435435")
        self.assertEqual(new.author_name, "Bob")
        self.assertEqual(new.author_id, "68712648721648271")
        self.assertEqual(new.created_date, "2021-02-25")
        self.assertEqual(new.created_time, "16:25:21")
        self.assertEqual(new.updated_date, "2021-02-26")
        self.assertEqual(new.updated_time, "08:21:20")
        self.assertEqual(new.counters_total, 3)

    def testTranslatingIncompleteJson(self):
        oldNoDescription = OldFormat('''{"address" : "https://www.google.com","content" : {"seasons" : [{"text": "winter"},{"text": "spring"},{"text":  "summer"},{"text": "autumn"}]},"updated" : "2021-02-26T08:21:20+00:00","author" :  {"username" : "Bob","id" : "68712648721648271"},"id" : "543435435","created" : "2021-02-25T16:25:21+00:00","counters" : {"A" : 3,"B" : 0},"type" : "main"}''')
        new = TranslatorOldToNew.translate(oldNoDescription)
        self.assertEqual(new.path, "https://www.google.com")
        self.assertEqual(new.seasons, [
                         "winter", "spring", "summer", "autumn"])
        self.assertEqual(new.body, "None")
        self.assertEqual(new.id, "543435435")
        self.assertEqual(new.author_name, "Bob")
        self.assertEqual(new.author_id, "68712648721648271")
        self.assertEqual(new.created_date, "2021-02-25")
        self.assertEqual(new.created_time, "16:25:21")
        self.assertEqual(new.updated_date, "2021-02-26")
        self.assertEqual(new.updated_time, "08:21:20")
        self.assertEqual(new.counters_total, 3)

    def testInsertingMissing(self):
        oldNoDescription = OldFormat('''{"content" : {"seasons" : [{"text": "winter"},{"text": "spring"},{"text":  "summer"},{"text": "autumn"}]},"updated" : "2021-02-26T08:21:20+00:00","author" :  {"username" : "Bob","id" : "68712648721648271"},"id" : "543435435","created" : "2021-02-25T16:25:21+00:00","counters" : {"A" : 3,"B" : 0},"type" : "main"}''')
        new = TranslatorOldToNew.translate(oldNoDescription)
        db = database()
        with self.assertRaises(AbsentError):
            db.insert(new)

    

if __name__ == '__main__':
    unittest.main()
