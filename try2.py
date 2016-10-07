import pandas as pd
from collections import defaultdict
import sys

# <codecell>

data = pd.read_csv("actions1.csv")



document_ret = defaultdict(int)
for x in data.values:    
    type_ = x[0]
    val = x[1] 
    #document_ret_1[type_] += val
    document_ret[type_] += val
    #if (user, type_) in used_:
    #    continue
    #used_.add((user, type_))
    #unique_1[type_] += val
    #unique_0[type_] += 1 - val    


types = ["CREATE_DOCUMENT", "DOCUMENT_DELETED", "GUEST", "LIKE", "LINK_CLICK","MARK_PHOTO","PHOTO_TEXT","RE_SHARE","SEND_PRESENT","VIDEO_CALL_INCOMING","VIDEO_CALL","VOTE","VOTE_PHOTO"]
for i in (types):
    print("{},{}".format(i, document_ret[i]))
