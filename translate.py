from Format import OldFormat
from Format import NewFormat

class TranslatorOldToNew:
    @staticmethod
    def translate(formatOld):
        formatNew = NewFormat()
        formatNew.setPath(formatOld.getAddress())
        formatNew.setSeasons(formatOld.getContentSeasonsText())
        formatNew.setBody(formatOld.getContentDescription())
        formatNew.setId(formatOld.getId())
        formatNew.setAuthorName(formatOld.getAuthorUsername())
        formatNew.setAuthorId(formatOld.getAuthorId())
        # some parsing has to be done add later
        # formatNew.setCreatedDate(self,)
        formatNew.setCountersTotal(formatOld.getCounters_A()+formatOld.getCounters_B())
        return formatNew

j = '''{"address" : "https://www.google.com ","content" : {"seasons" : [{"text": "winter"},{"text": "spring"},{"text": "summer"},{"text": "autumn"}],"description" : "All seasons"},"updated" : "2021-02-26T08:21:20+00:00","author" : {"username" : "Bob","id" : "68712648721648271"},"id" : "543435435","created" : "2021-02-25T16:25:21+00:00","counters" : {"A" : 3,"B" : 0},"type" : "main"}'''
o = OldFormat(j)
n = TranslatorOldToNew.translate(o) 
print(n.path)       