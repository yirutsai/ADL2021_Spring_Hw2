import json
import sys
import pandas as pd

assert len(sys.argv)==3
in_file = sys.argv[1]
out_file = sys.argv[2]

with open(in_file,"r",encoding="utf-8") as f:
    preds = json.load(f)
print(len(preds))
# df  = pd.DataFrame.from_dict(preds,index = preds.keys())
df = pd.DataFrame(list(preds.items()))
df.columns=["id","answer"]
df.to_csv(out_file,encoding="utf_8_sig",index=False)

# writer = csv.writer(open(out_file,"w"))
# writer.writerow(["id","answers"])
# for key,val in preds.items():
#     writer.writerow([key,val])

# with open(out_file,"w",encoding="utf-8")as f2:
#     f2.write("id,answer\n")
#     for key,val in preds.items():
#         f2.write(f'{key},{val}')
#         f2.write("\n")

with open(out_file,"r",encoding="utf-8")as f:
    L = f.readlines()
print(len(L))
for i in range(len(L)):
    tmp = L[i].split(",")
    if(len(tmp)!=2):
        print(i,tmp)
        
