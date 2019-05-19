# DLL Hijacking Helper
# Myo Soe, http://yehg.net/
# 2013-12-08

# platform: Python 2.x @ Windows 

import csv
import shutil
import hashlib
import os
import sys
import re


def md5sum(filename):
    md5 = hashlib.md5()
    if os.path.exists(filename) == True:
        with open(filename,'rb') as f: 
            for chunk in iter(lambda: f.read(128*md5.block_size), b''): 
                 md5.update(chunk)
        return md5.hexdigest()
    else:
        print filename + " does not exist. \nYou should run dll-hijack-helper from its directory not your tested application directory."
        sys.exit()
        



# default ProcMon Output
file = 'Logfile.CSV'

if os.path.exists(file) == False:
    print "\nLogfile.CSV was not found. Read README.txt.\n"
    sys.exit()
    

# command to kill tested application process
kill_cmd = 'taskkill /f /im target.exe && taskkill /f /im calc.exe'

hijacker_dll =  'hijacker.dll'
hijacker_dll_md5 = md5sum('hijacker.dll')

hijacker_exe = 'hijacker.exe'
hijacker_exe_md5 = md5sum('hijacker.exe')

print "\nRunning DLL Hijack Helper - by Myo Soe , http://yehg.net"
print "\n\nhijacker_dll_m5: " + hijacker_dll_md5 
print "hijacker_exe_m5: " + hijacker_exe_md5 + "\n\n----------------------------------\n"

vuln_dlls  = []
scanned_dlls = []
header = 0 
with open(file,'rb') as csvfile:
    line_reader = csv.reader(csvfile,delimiter=",",quotechar='"')
    for row in line_reader:
        if header != 0:
            target_file =  str(row[4])

            if re.search('exe$',target_file,re.M|re.I) and not target_file in scanned_dlls:
                if not os.path.exists(target_file):
                    shutil.copyfile(hijacker_exe,target_file)
                    print "\nCreated EXE -> " + target_file + "\n"
                    is_vuln = raw_input("\n[!] Manually launch the application to test it.\n[!] Enter 'y' key if it works, other key to continue\n_")
                    if re.search('y',is_vuln,re.M|re.I):
                        vuln_dlls.append(target_file)
                    print "\nKilling the process ...\n"
                    os.system(kill_cmd)                    
                    os.remove(target_file)
                    scanned_dlls.append(target_file)
                else:
                    target_file_md5 =  md5sum(target_file)
                    if (target_file_md5!=hijacker_exe_md5):
                        os.remove(target_file)
                        shutil.copyfile(hijacker_exe,target_file)
                        print "\nCreated EXE -> " + target_file + "\n"
                        is_vuln = raw_input("\n[!] Manually launch the application to test it.\n[!] Enter 'y' key if it works, other key to continue.\n_")
                        if re.search('y',is_vuln,re.M|re.I):
                            vuln_dlls.append(target_file)                        
                        print "\nKilling the process ...\n"
                        os.system(kill_cmd)
                        os.remove(target_file) 
                        scanned_dlls.append(target_file)
                    else:
                        print "Hijacker EXE already exists. \nSkipped creating -> " + target_file + "\n"
                    
                
                
            elif re.search('dll$',target_file,re.M|re.I) and not target_file in scanned_dlls:
                if not os.path.exists(target_file):
                    shutil.copyfile(hijacker_dll,target_file)
                    print "\nCreated DLL -> " + target_file + "\n"
                    is_vuln = raw_input("\n[!] Manually launch the application to test it.\n[!] Enter 'y' key if it works, other key to continue.\n_")
                    if re.search('y',is_vuln,re.M|re.I):
                        vuln_dlls.append(target_file)
                    print "\nKilling the process ...\n"
                    os.system(kill_cmd)
                    os.remove(target_file)  
                    scanned_dlls.append(target_file)
                else:
                    target_file_md5 =  md5sum(target_file)
                    if (target_file_md5!=hijacker_dll_md5):
                        os.remove(target_file)
                        shutil.copyfile(hijacker_dll,target_file)
                        print "\nCreated DLL -> " + target_file + "\n"
                        is_vuln = raw_input("\n[!] Manually launch the application to test it. \n[!] Enter 'y' key if it works, other key to continue.")
                        if re.search('y',is_vuln,re.M|re.I):
                            vuln_dlls.append(target_file)
                        print "\nKilling the process ...\n"
                        os.system(kill_cmd)
                        os.remove(target_file)
                        scanned_dlls.append(target_file) 
                    else:
                        print "Hijacker DLL already exists. \nSkipped creating -> " + target_file + "\n"
                    
                
        else:
            header = 1
            
        
        
        
    

if len(vuln_dlls)>0:
    print "\n------------------------------\nVulnerable DLL/EXEs: \n\n - " + "\n - ".join(vuln_dlls)


