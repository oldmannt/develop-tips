### list files
`git ls-files`

### ignore files which have been commit
	
	```
	git rm --cached -r files
	git add .gitignore
	git commit -m "xxx"
	```  
	
### update frome remote

	git fetch origin master:temp // get remote master branch as local temp
	git merge temp
	
fix conflict, check the conflicting files, and fix conflict in text edit or ide



### compare with remote

	```git
	git fetch origin
	git diff master origin/master
	```

### merge branch master and develop
	master is behind, develop forward

	```git
	git checkout master
	git merge develop
	```

### add tag

	```sh
	git tag -a v0.1 -m “it work”
	```

### git graphic log

git log --pretty=format:"%h %s" --graph

### git back to version, fix bug, merge to master

    git branch fixbug
    git reset --hard 5fd036b
    .... fix the bug
    git merge master
    Auto-merging ios/usnit_app.xcodeproj/project.pbxproj
    CONFLICT (content): Merge conflict in ios/usnit_app.xcodeproj/project.pbxproj
    edit project.pbxproj
    <<<<<<< HEAD:
    ...  I want to keep master so delete this code
    =======
    ...
    >>>>>>> master
    git commit -m "..."
  
###git submodule  
http://www.kafeitu.me/git/2012/03/27/git-submodule.html

	```sh
	git submodule add https://github.com/oldmannt/gearsbox.git gearsbox
	cd gearsbox
	git submodule #show submodules
	git submodule init #submodules registered, then could be download
	git submodule update
	Cloning into 'deps/djinni'...
	...
	Checking connectivity... done.
	Submodule path 'deps/djinni': checked out '191940c8a9fe5e459a7defa2c959b5e8423db91b'
	Cloning into 'deps/gyp'...
	...
	Checking connectivity... done.
	Submodule path 'deps/gyp': checked out '0bb67471bca068996e15b56738fa4824dfa19de0'
	#don't need to  cd deps/gyp &&git checkout -q 0bb67471bca068996e15b56738fa4824dfa19de0
	#has been done
	```
	
delete submodule  
1.Delete the relevant section from the `.gitmodules` file.  
2.Stage the `.gitmodules` changes `git add .gitmodules`  
3.Delete the relevant section from `.git/config.`  
4.Run `git rm --cached path_to_submodule (no trailing slash).`  
5.Run `rm -rf .git/modules/path_to_submodule`  
6.Commit `git commit -m "Removed submodule <name>"`  
7.Delete the now untracked submodule files `rm -rf path_to_submodule`  

### pushing to remotes
$git push [remote-name] [branch-name]
	
### git discard

#### This will unstage all files you might have staged with git add:  

	git reset
#### This will revert all local uncommitted changes (should be executed in repo root):  

	git checkout .
You can also revert uncommitted changes only to particular file or directory:

	git checkout [some_dir|file.txt]
Yet another way to revert all uncommitted changes (longer to type, but works from any subdirectory):  

	git reset --hard HEAD
#### This will remove all local untracked files, so only git tracked files remain:

	git clean -fdx
	
### Git Sparse Checkout  

    $mkdir project_folder
    $cd project_folder
    $git init
    $git remote add -f origin <url>
    $git config core.sparsecheckout true
list you files and directories in .git/info/sparse-checkout

    $echo “libs” >> .git/info/sparse-checkout
    $echo “apps/register.go” >> .git/info/sparse-checkout
    $echo “resource/css” >> .git/info/sparse-checkout
    $git pull origin master
    
### SSH KEY
``` shell
$ ssh-keyget -t rsa -b 4096 -C "your_email@x.com"
$ ssh-add -K ~/.ssh/id_rsa
$ pbcopy < ~/.ssh/id_rsa.pub
$ ssh -T git@github.com # test, check output
# then paste to github->accout->ssh key
```

### init and merge remote to local
``` shell
$ git init
$ git remote add origin https://github.com/oldmannt/learnNodeJS.git
$ git pull origin master
```

### modify
``` shell
$ git status # show the status
$ git add <filename>
$ git add * # add all the modification
$ git status # check what modified
# undo git add
$ git reset -- <file1> <file2> ...
$ git reset . # undo all
# commit to local repository
$ git commit -m "say something"
$ git log
```

### diff/merge tools
``` shell
$ git config --global --add diff.tool kdiff3
$ git config --global --add diff.tool.kdiff3.path /Applications/kdiff3.app/Contents/MacOS/kdiff3 
$ git config --global --add diff.tool.kdiff3.trustExitCode false
$ git difftool HEAD^

$ git config --global --add merge.tool kdiff3
$ git config --global --add merge.tool.kdiff3.path /Applications/kdiff3.app/Contents/MacOS/kdiff3 
$ git config --global --add merge.tool.kdiff3.trustExitCode false
```
It's not good. We can't see the list of files for diff result. It just show the file one by one after we close the previous one.
SourceTree is more nice.

```
$ git diff hash1 hash2 --stat  
$ git diff branch1 branch2 --stat  
$ git diff filename  
$ git diff –cached  
$ git diff –cached filename  
$ git diff hash1:filename hash2:filename
```
### merger to github
```
$ git remote -v # check the url and branch name
$ git remote origin master # roigin: remote branch, master: local branch
```
fatal: Authentication failed  
```
$ ssh-add -K ~/.ssh/github_id_rsa # the private key for github
$ $ git remote origin master # input username, password. weird what the ssh for
```
$
