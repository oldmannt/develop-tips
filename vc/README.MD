### VS: shortcut for open files
ctrl + ;

### macOS show hiden file in finder
copy and pase the below line to terminal and run
"defaults write com.apple.finder AppleShowAllFiles YES"

### macOS .bash_profile 
.bash_profile is under /Users/"your name"/.bash_profile, it need to be created
touch ~/.bash_profile
open ~/.bash_profile

### Perforce "Parallel file transfer must be enabled using net.parallel.max"
 disable parallel sync in P4V -> Preferences -> Server Data

#### P4V A given file is missing from my Workspace, but present at the Perforce Depot.  
    use the "Get Revision..." item and in the subsequent dialog, you can check the "force operation" checkbox
    
#### show all connection of PID
    netstat -a -n -o|findstr "PID"  
    
#### P4 "all revision(s) already integrated" 
    "advanced options" -f
    
#### P4 "Back Out" and "Rollback"
    "Back out" only remove target change list, keep the newer change list  
    "Rollback" remove all the change list after target  
    but "Rollback" don't work to me, I just "Back Out" one by one
