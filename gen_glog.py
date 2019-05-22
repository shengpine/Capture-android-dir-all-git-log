#!/usr/bin/python3

import os
import sys
import shutil

curdir=sys.argv[1]
outdir=sys.argv[2]
gdir = os.path.join(outdir,os.path.basename(curdir))

def gen_glog(path,dest):
    """
    we can get git log from dir by this fun !
    """
    os.chdir(path)
    bname= os.path.basename(path)    
    pdir = os.path.dirname(path)

    if False == os.path.exists(dest):
        os.makedirs(dest)
    
    cmd = "git log >" + os.path.join(dest,bname) + ".glog"
    if 0 == os.system(cmd):
        print(cmd)
        os.chdir(pdir)
        return 0
#del empty file that it have not git log.
    os.remove(os.path.join(dest,bname) + ".glog")

#recurs to  all dir
    for ln in os.listdir():
        tln = os.path.join(path,ln)
         
        if False == os.path.isdir(tln) or ln == ".repo":
            continue
   
        new_dst  = os.path.join(dest,ln)
        new_path = tln;

        gen_glog(new_path,new_dst)


if __name__ == "__main__":
    if curdir == outdir:
        print("outdir is same as input dir, not support")
        exit(0)

    print(gdir)
    gen_glog(curdir,gdir)








