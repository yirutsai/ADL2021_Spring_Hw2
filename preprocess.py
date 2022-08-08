import json
import sys
import os

with open(sys.argv[1],"r") as f:
    data = json.load(f)

os.makedirs(os.path.dirname(sys.argv[2]),exist_ok=True)
with open(sys.argv[2],"w") as f:
    json.dump({"data":data},f,ensure_ascii=False,indent=2)
