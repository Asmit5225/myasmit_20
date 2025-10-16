import os 
sorteddict= {}
#here we print all the files directories in the given path it...
 # prints in the form of tuple {[main directory], [sub directory in the main directory],[files in the main diectory]}
#for file in os.walk(r'F:\project vs code'):
    #print(file) 

#instead of printing them in tuple form we can sepate them to increase readability..
#for top_dir, directory, files in os.walk(r'F:\project vs code'):
    #print(f"currect directory:{top_dir}")
    #print(f"directory in that diectory:{directory}")
    #print(f"files in that directory:{files}")
#now we are going to print all the files present in all the directories and sub directories..
for top_dir, directory, files in os.walk(r'F:\project vs code'):
    for _files in files:
        abs_path=os.path.join(top_dir,_files) #here we joined the files along with their path mane konta kon directory te ache...
        size= os.path.getsize(abs_path) #here we calculate the size of the files
        sorteddict[abs_path]=size
        #print(sorteddict)
        #print(f"files is :{abs_path}   size:{size}")

items_shown=0
for path, size in sorted(sorteddict.items(), key=lambda x:x[1], reverse=True):
    if items_shown > 19:
             break
    print(f"Size: {size} Path: {path}")
    items_shown += 1        
