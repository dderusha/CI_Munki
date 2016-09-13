#!/usr/bin/python
import CoreFoundation
# import requests
import subprocess
import urllib
from SystemConfiguration import SCDynamicStoreCopyConsoleUser
import sys

LOGGED_IN_USER = (SCDynamicStoreCopyConsoleUser(None, None, None) or [None])[0]; LOGGED_IN_USER = [LOGGED_IN_USER, ""][LOGGED_IN_USER in [u"loginwindow", None, u""]]; sys.stdout.write(LOGGED_IN_USER + "\n")
munkiserver = raw_input("Enter munki server http://10.0.6.127/munki_repo: ")
manifest = raw_input("Enter manifest: ")
if munkiserver is str :
    print str(munkiserver)

package = '/Users/' + LOGGED_IN_USER + '/munkitools-2.8.0.2810.pkg'

# res = requests.get('https://github.com/munki/munki/releases/download/v2.8.0/munkitools-2.8.0.2810.pkg')
# url_handle = urllib.urlopen('https://github.com/munki/munki/releases/download/v2.8.0/munkitools-2.8.0.2810.pkg')
res = urllib.urlretrieve('https://github.com/munki/munki/releases/download/v2.8.0/munkitools-2.8.0.2810.pkg', package)


# cmd = ['sudo', '/usr/sbin/installer', '-pkg', package, '-tgt', '/']
# or
cmd = ['sudo', '/usr/sbin/installer', '-pkg', package, '-tgt', '/']

install_process = subprocess.Popen(cmd, shell=False, bufsize=1,
                                   stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)

print str(install_process.communicate()[0])

keys = {"SoftwareRepoURL": munkiserver, "ClientIdentifier": manifest, }
ManagedInstalls = '/Library/Preferences/ManagedInstalls.plist'

CoreFoundation.CFPreferencesSetMultiple(keys, [], "ManagedInstalls",  CoreFoundation.kCFPreferencesAnyUser, CoreFoundation.kCFPreferencesCurrentHost)

#CoreFoundation.CFPreferencesSetMultiple(keys, "/Library/Preferences/ManagedInstalls.plist")
#CoreFoundation.CFPreferencesAppSynchronize("/Library/Preferences/ManagedInstalls.plist")
