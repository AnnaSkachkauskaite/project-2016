

import pandas as pd
from collections import defaultdict
import sys

# <codecell>
in_file = sys.argv[1]
data = pd.read_csv(in_file)
#data = pd.read_csv("00000_0.csv")



document_ret_1 = defaultdict(int)
document_ret_0 = defaultdict(int)
unique_1 = defaultdict(int)
unique_0 = defaultdict(int)
used_ = set()
for x in data.values:    
    type_ = x[3]
    val = x[0]
    user = x[1]    
    document_ret_1[type_] += val
    #document_ret_0[type_] += 1 - val
    #if (user, type_) in used_:
    #    continue
    #used_.add((user, type_))
    #unique_1[type_] += val
    #unique_0[type_] += 1 - val    


types = ["CREATE_DOCUMENT", "DOCUMENT_DELETED", "GUEST", "LIKE", "LINK_CLICK","MARK_PHOTO","PHOTO_TEXT","RE_SHARE","SEND_PRESENT","VIDEO_CALL_INCOMING","VIDEO_CALL","VOTE","VOTE_PHOTO"]
for i in (types):
    print("{},{}".format(i, document_ret_1[i]))

