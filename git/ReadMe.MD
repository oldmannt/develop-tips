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

	git submodule https://github.com/oldmannt/gearsbox_client.git gearsbox
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
delete submodule  
1.Delete the relevant section from the `.gitmodules` file.  
2.Stage the `.gitmodules` changes `git add .gitmodules`  
3.Delete the relevant section from `.git/config.`  
4.Run `git rm --cached path_to_submodule (no trailing slash).`  
5.Run `rm -rf .git/modules/path_to_submodule`  
6.Commit `git commit -m "Removed submodule <name>"`  
7.Delete the now untracked submodule files `rm -rf path_to_submodule`  
	
	
###git discard

####This will unstage all files you might have staged with git add:  

	git reset
####This will revert all local uncommitted changes (should be executed in repo root):  

	git checkout .
You can also revert uncommitted changes only to particular file or directory:

	git checkout [some_dir|file.txt]
Yet another way to revert all uncommitted changes (longer to type, but works from any subdirectory):  

	git reset --hard HEAD
####This will remove all local untracked files, so only git tracked files remain:

	git clean -fdx
	
###Git Sparse Checkout  

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
    
