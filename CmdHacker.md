# del /q /f /s pathToFolder
    /q (quiet mode) 
    /f (force)
    /s (including all subdirectories) 

# nslookup
    Displays information that you can use to diagnose Domain Name System (DNS) infrastructure.

# ipconfig/all
    Shows your pc ip and all net details

# ping website url
    Show the ip address of any website

# attrib +h +s +r nameOfFolder
    hide any folder
    attrib is used to display or change file attributes
    +h This flag is used to add the "Hidden" attribute to the specified file or folder
    +s This flag is used to add the "System" attribute to the specified file or folder.
    +r This flag is used to add the "Read-only" attribute to the specified file or folder.

# attrib -h -s -r nameOfFolder
    unhide any folder
    attrib is used to display or change file attributes
    -h This flag is used to remove the hidden attribute from the file
    -s This flag is used to remove the "System" attribute from the specified file
    -r This flag is used to remove the "Read-only" attribute from the specified file 

# wmic product get name
    This command is a Windows Management Instrumentation Command-line (WMIC) command used
    to retrieve the names of installed software products on a Windows system.


# driverquery
    This command is a Windows Command Prompt command that allows you to display a list of all
    installed device drivers and their properties on a Windows system

    add /FO LIST to display the output as a list
    add /SI (signature) to displays digital signature information for drivers.
    add /V (verbose) to displays additional information about each driver.

# systeminfo
    Display information about your system 

# | clip
    copy output

# arp -a
    The ARP -A command is used in the Windows Command Prompt to display the current Address Resolution
    Protocol (ARP) cache on your computer. The ARP cache contains a mapping of IP addresses to physical
    MAC (Media Access Control) addresses on your local network.


# netstat -an
    The netstat -an command is a network utility tool available in various operating systems, including Windows
    and Unix-like systems. It provides information about network connections, routing tables, interface statistics,
    masquerade connections, and more. The -an flags are specific options used with the netstat command to display
    detailed information about network connections in a numerical format.

# ver
    windows version

# title 
    change title of cmd window

# tracert
    This command, short for "traceroute," is a network diagnostic tool used to trace the route that packets take from your
    computer to a destination IP address or domain. 


# wmic bios get serialnumber
    get computer's serialnumber

# wmic memorychip get speed
    retrieve information about the speed of the memory chips (RAM) installed on your computer.

# start softwareName
    open / run a software;.

# fc file1 filw2
    This command comapres the content of the files

# sfc /scannow
    The sfc /scannow command is a system utility in Windows used to scan and repair
    corrupted or missing system files. SFC stands for System File Checker, and the
    /scannow parameter instructs the utility to scan the integrity of all protected
    system files and attempt to repair any issues it finds.

# prompt 
    Changes the text that indicates the current working directory

# prompt /?
    Shows the options to use with prompt

# cd
    Changes directory, but only cd will show the current directory
