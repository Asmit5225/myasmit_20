import os
lamo={}


for root, directories, files in os.walk(r'F:\New folder (2)'):
    #print(f"the root is :{root}")
    #print(f"the directories is:{directories}")
    #print(f"the files is: {files}")
    
    for _files in files:
        path22= os.path.join(root,_files)
        size= os.path.getsize(path22)
       # print(f" file is {path22} it's size is {size}")
        #arranging them by largest 10 files...

        #in order to save this in dict form
        lamo[path22]=size
        #print(lamo)
items_shown=0
for path, size in sorted(lamo.items(), key=lambda x:x[1], reverse=True):
    if items_shown > 9:
             break
    print(f"Size: {size} Path: {path}")
    items_shown += 1

       
    #for asmit in directories:
        #path32=os.path.join(root,asmit)
        #size= os.path.getsize(path32)
        #print(f"directory is f{path32} size is {size}")

                                      