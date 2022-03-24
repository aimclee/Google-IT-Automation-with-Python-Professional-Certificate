#!/usr/bin/env python3
import re
from socket import NI_NUMERICSERV
import sys
"""
usage example:
>chmod +x check_cron.py
> ./check_cron.py syslog
[output]
"""

logfile = sys.argv[1]
usernames={}
with open(logfile) as f:
    for line in f:
        if "CRON" not in line:
            continue
        pattern = r"USER \((\w+)\)$"
        result = re.search(pattern, line)
        if result is None:
            continue
        name = result[1]
        # dict.get(name,0) : dictionary의 name이라는 key값의 value값을 가져온다.
        # 이 때의 0은 default로 지정해주는 값이다.
        usernames[name] = usernames.get(name, 0) + 1
print(usernames)
