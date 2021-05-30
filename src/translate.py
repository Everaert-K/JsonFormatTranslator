from Format import OldFormat
from Format import NewFormat

import datetime

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

        created = datetime.datetime.strptime(formatOld.getCreated(), '%Y-%m-%dT%H:%M:%S%z')
        created_date = str(created.date())
        formatNew.setCreatedDate(created_date)
        created_time = str(created.time())
        formatNew.setCreatedTime(created_time)
        
        updated = datetime.datetime.strptime(formatOld.getUpdated(), '%Y-%m-%dT%H:%M:%S%z')
        updated_date = str(updated.date())
        formatNew.setUpdatedDate(updated_date)
        updated_time = str(updated.time())
        formatNew.setUpdatedTime(updated_time)

        formatNew.setCountersTotal(formatOld.getCounters_A()+formatOld.getCounters_B())
        return formatNew

    