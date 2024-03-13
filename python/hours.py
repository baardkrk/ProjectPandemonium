#!/usr/bin/env python3
#
# Program that calculates the amount of hours I've worked, in case
# I forget to use the time-clock 

import datetime as dt
import argparse
from dateutil import tz


parser = argparse.ArgumentParser(description='Calculate hours since given time')
parser.add_argument('timestring', type=str, help='ISO formatted time or HH:MM')
parser.add_argument('--timezone', required=False, type=str, help='Current timezone')   #default='Europe/Oslo',

args = parser.parse_args()

try:
    a = dt.datetime.strptime(args.timestring, '%H:%M')
    a = dt.datetime.now().replace(hour=a.hour, minute=a.minute)
except ValueError:
    a = dt.datetime.fromisoformat(args.timestring)

if not args.timezone:
    t = dt.datetime.now(dt.timezone.utc).astimezone().tzinfo
else:
    t = tz.gettz(args.timezone)

a = a.astimezone(t).astimezone(dt.timezone.utc)
b = dt.datetime.utcnow().replace(tzinfo=dt.timezone.utc)
t = (b - a).total_seconds() / 3600
print(f'{t:.2f} (7.5 + {t-7.5:.2f})')
