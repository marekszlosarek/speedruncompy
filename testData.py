from speedruncompy.data_structures import *
from speedruncompy.enums import *
from speedruncompy import *

import json

time = RuntimeTuple({"hour":0, "minute":1, "second": 0, "millisecond": 50})

print(time)
print(repr(time))

print(json.dumps({"help": eventType.CATEGORY_CREATED}))