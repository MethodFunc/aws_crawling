import re
from datetime import datetime, timedelta

pattern = r'[-=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’·\s]'

date_pattern = {
    8: '%Y%m%d',
    10: '%Y%m%d%H',
    12: '%Y%m%d%H%M',
    14: '%Y%m%d%H%M%S',
}


def calc_daterange(args) -> list:
    start_date = re.sub(pattern, '', args.start_date)
    start_date = datetime.strptime(start_date, date_pattern[len(start_date)])

    end_date = re.sub(pattern, '', args.end_date)
    end_date = datetime.strptime(end_date, date_pattern[len(end_date)])

    date_diff = end_date - start_date
    date_range = int(date_diff.days * 24 + date_diff.seconds / 3600) + 1

    date_list = [
        (start_date + timedelta(hours=i)).strftime("%Y%m%d%H%M")
        for i in range(date_range)
    ]

    return date_list
