DLL Hijack Helper - How-to
++++++++++++++++++++++++++++++

1. Run ProcMon
2. Set filter rule with result "NAME NOT FOUND"
3. Run your target application
4. Save ProcMon output as Logfile.CSV
5. Exit ProcMon
6. Edit dll-hijack-helper.py
7. Search and Replace "target.exe" with your test application name.
5. Run dll-hijack-helper.py

Typical output looks like this:
------------------------------------------


Running DLL Hijack Helper - by Myo Soe , http://yehg.net


hijacker_dll_m5: e6744ebb969ce6373d3702d1e7f70487
hijacker_exe_m5: a56a094461f79a3be7c672d10fc413c3

----------------------------------


Created DLL -> D:\tmp\TestApp 32bit\msi.dll


[!] Launch the application to test it.
[!] Enter 'y' key if it works, other key to continue.
_y

Created DLL -> D:\tmp\TestApp 32bit\sfc_os.dll


[!] Launch the application to test it.
[!] Enter 'y' key if it works, other key to continue.
_y

Created DLL -> D:\tmp\TestApp 32bit\WINTRUST.dll


[!] Launch the application to test it.
[!] Enter 'y' key if it works, other key to continue.
_y

Created DLL -> D:\tmp\TestApp 32bit\CRYPT32.dll


[!] Launch the application to test it.
[!] Enter 'y' key if it works, other key to continue.
_y

Created DLL -> D:\tmp\TestApp 32bit\MSASN1.dll


[!] Launch the application to test it.
[!] Enter 'y' key if it works, other key to continue.
_n

Created DLL -> D:\tmp\TestApp 32bit\MsiMsg.dll


[!] Launch the application to test it.
[!] Enter 'y' key if it works, other key to continue.
_n

Created DLL -> D:\tmp\TestApp 32bit\rsaenh.dll


[!] Launch the application to test it.
[!] Enter 'y' key if it works, other key to continue.
_n

Created DLL -> D:\tmp\TestApp 32bit\MSISIP.DLL


[!] Launch the application to test it.
[!] Enter 'y' key if it works, other key to continue.
_n

Created DLL -> D:\tmp\TestApp 32bit\xpsp2res.dll


[!] Launch the application to test it.
[!] Enter 'y' key if it works, other key to continue.
_n

Created DLL -> D:\tmp\TestApp 32bit\netapi32.dll


[!] Launch the application to test it.
[!] Enter 'y' key if it works, other key to continue.
_n

Created DLL -> D:\tmp\TestApp 32bit\cryptnet.dll


[!] Launch the application to test it.
[!] Enter 'y' key if it works, other key to continue.
_n

Created DLL -> D:\tmp\TestApp 32bit\PSAPI.DLL


[!] Launch the application to test it.
[!] Enter 'y' key if it works, other key to continue.
_n

Created DLL -> D:\tmp\TestApp 32bit\SensApi.dll


[!] Launch the application to test it.
[!] Enter 'y' key if it works, other key to continue.
_n

Created DLL -> D:\tmp\TestApp 32bit\WINHTTP.dll


[!] Launch the application to test it.
[!] Enter 'y' key if it works, other key to continue.
_n

Created DLL -> D:\tmp\TestApp 32bit\CLBCATQ.DLL


[!] Launch the application to test it.
[!] Enter 'y' key if it works, other key to continue.
_n

Created DLL -> D:\tmp\TestApp 32bit\COMRes.dll


[!] Launch the application to test it.
[!] Enter 'y' key if it works, other key to continue.
_n

Created DLL -> D:\tmp\TestApp 32bit\UxTheme.dll


[!] Launch the application to test it.
[!] Enter 'y' key if it works, other key to continue.
_n

Created DLL -> D:\tmp\TestApp 32bit\SHFolder.dll


[!] Launch the application to test it.
[!] Enter 'y' key if it works, other key to continue.
_n

Created EXE -> D:\tmp\TestApp 32bit\MSIEXEC.EXE


[!] Launch the application to test it.
[!] Enter 'y' key if it works, other key to continue
_y

------------------------------
Vulnerable DLL/EXEs:

 - D:\tmp\TestApp 32bit\msi.dll
 - D:\tmp\TestApp 32bit\sfc_os.dll
 - D:\tmp\TestApp 32bit\WINTRUST.dll
 - D:\tmp\TestApp 32bit\CRYPT32.dll
 - D:\tmp\TestApp 32bit\MSIEXEC.EXE
