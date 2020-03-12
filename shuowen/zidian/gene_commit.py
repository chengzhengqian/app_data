max_idx=25610
min_idx=0
batch_size=1000
current_idx=min_idx
template="""
git add {%d..%d}_{e,b}.json
git commit -m "zidian %d-%d"
git push
"""
with open("./commit.sh","w") as f:
    while(current_idx!=max_idx):
        next_idx=min(current_idx+batch_size,max_idx)
        f.write(template%(current_idx,next_idx,current_idx,next_idx))
        current_idx=next_idx

        
