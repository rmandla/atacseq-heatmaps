#/usr/bin/python

import pandas as pd
import subprocess, os, sys
import time

def beddir_to_matrix(bed_directory, consensus, output, bespec = 0):
    # Take in some directory with bed files with readconts, align to consensus and sum overlaps in same samples. Output results as a matrix
    # optionally can specify some filename header specificity to choose what bed files to read in
    files = []
    headers = []
    if bed_directory[-1] != '/':
        bed_directory += '/'
    for i in os.listdir(bed_directory):
        if type(bespec) == str:
            if bespec in i:
                files.append(bed_directory+i)
                headers.append(i.split('.bed')[0])
        else:
            if '.bed' in i and consensus != i:
                files.append(bed_directory+i)
                headers.append(i.split('.bed')[0])
    
    # make dictionary
    matrixrc = {}
    matrixrc['loci'] = []
    for i in headers:
        matrixrc[i] = []
    
    # read files
    consensus = pd.read_table(consensus,sep='\t',header=None)
    
    # fill dictionary
    total = len(consensus)
    for index,row in consensus.iterrows():
        t = time.process_time()
        chrom = row[0]
        beg = str(row[1])
        end = str(row[2])
        matrixrc['loci'].append(chrom + ":" + beg + "-" + end)
        with open('temp','w') as out:
            out.write(chrom+'\t'+beg+'\t'+end)
        for n in range(len(files)):
            s = files[n]
            key = list(matrixrc.keys())[n+1]
            subprocess.run("intersectBed -a " + s + " -b temp -wa > intertemp",shell=True,check=True)
            try:
                inter = pd.read_table("intertemp",header=None)
                if len(inter) == 1:
                    matrixrc[key].append(inter[3].to_list()[0])
                elif len(inter) > 1:
                    matrixrc[key].append(inter[3].sum())
            except:
                matrixrc[key].append(0)
        elapsed_time = time.process_time() - t
        remaining = (elapsed_time*total) - (elapsed_time*index)
        if remaining > 3600:
            eta = str(remaining/3600) + " hr"
        elif remaining > 60:
            eta = str(remaining/60) + " min"
        else:
            eta = str(remaining) + " sec"
        os.system('clear')
        print('ETA: ' + eta)
        percent = (index+1)/total * 100
        print(str(percent) + "% complete")
    os.remove("temp")
    os.remove("intertemp")
    output = pd.DataFrame.from_dict(matrixrc)
    output.to_csv(output,sep='\t',index=False)

beddir_to_matrix(sys.argv[1],sys.argv[2])
