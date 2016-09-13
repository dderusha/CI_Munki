# CI_munki

## Overview

CI_munki is tool to help with the installation of munkitools-2.8.0.2810 on OS X. CI_munki asks for your munki repo and manifest so when your computer reboots its ready to use Managed Software Center.app.

##How to Use

- Download the script to your workstation.  
- Open /Applications/Utilities/Terminal.app
- at the Terminal prompt type “python” minus the “”
- drag CI_munki.py to the same terminal window, and press return

CI_munki will ask you to enter in your munki server such as http://10.1.1.2/munki_repo.
Next you will be asked for the desired manifest you would like applied to the workstation.
Lastly, when CI_munki exits you should restart your computer for the changes to take effect.

## Acknowledgments

Thank you to Damon O’Hare for .pkg python install assistance. Part of muni’s original code. Always thankful to MacMule for his last logged in user writeup. Lastly @elios (macadmins slack #python channel) for help with CFPreferencesSetMultiple.