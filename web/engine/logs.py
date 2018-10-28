import datetime
from inspect import currentframe, getframeinfo
import inspect
"""Write to logs database.log"""
def writeLogs(what: str):
    try:
        f = open("../logs.log", "a")
    except FileNotFoundError as e:
        return e
    # frameinfo = getframeinfo(currentframe())
    frame = inspect.stack()[1]
    frameinfo = inspect.getframeinfo(frame[0])
    f.write(str(datetime.datetime.now())+str(what)+"\n")
    d = {'time': datetime.datetime.now(), 'file': frameinfo.filename, 'line': frameinfo.lineno, 'what': what }
    f.write("{d[time]!s} {d[file]!s}:{d[line]!s} {d[what]!s}  \n".format(d=d))


