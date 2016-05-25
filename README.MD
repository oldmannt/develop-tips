### json format

	"key":"value"
	"key":123
	"key":true/false
	"key":{"key1":"value1",...}
	"key":[
		{"key1":"value1",...}
		{"key1":"value2",...},
		....
		{"key1":"value1",...}
	]

### ARC forbids explicit message send of 'autorelease'
if Objective-C Automatic Reference Counting is "Yes", then "autorelease" is forbided, will cause the error message below, just delete "autorelease"

	ARC forbids explicit message send of 'autorelease'
	'autorelease' is unavailable: not available in automatic reference counting mode

### show encoding in sublien text 2  
view->Show Console enter commond

	view.encoding()  // or below
	sublime.message_dialog(view.encoding())

### EXC_BAD_ACCESS(code=EXC_I386_GPFLT)
I got a weired strange problem, in zf_log.c

	CFLog(apple_lvl(msg->lvl), CFSTR("%s"), msg->msg_b); // crash throw EXC_BAD_ACCESS(code=EXC_I386_GPFLT)
	
	// add a const char*, then ok, don't crash. but today I change back to above, OK again, I don't know why
	// if get same cash next time, add "const char*"
	cosnt char* pp = msg->msg_b;
	CFLog(apple_lvl(msg->lvl), CFSTR("%s"), msg->msg_b); 
	
	typedef struct zf_log_message
	{
		int lvl; /* Log level of the message */
		const char *tag; /* Associated tag (without tag prefix) */
		char *buf; /* Buffer start */
		char *e; /* Buffer end (last position where EOL with 0 could be written) */
		char *p; /* Buffer content end (append position) */
		char *tag_b; /* Prefixed tag start */
		char *tag_e; /* Prefixed tag end (if != tag_b, points to msg separator) */
		char *msg_b; /* Message start (expanded format string) */
	}

	
	
	
###git submodule  
http://www.kafeitu.me/git/2012/03/27/git-submodule.html

	git add https://github.com/oldmannt/gearsbox_client.git gearsbox
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


###curl compile error on android "CURL_SIZEOF_LONG definition is missing!"  
check app/gradle.build, "productFlavors" shoud not be "flavor1", specify a cpu type, than curl can define CURL_SIZEOF_LONG

	productFlavors {
		create("x86-64") {	// for debug
                	ndk.abiFilters.add("x86_64")
            	}
		create("arm7") {	// should not be "flavor1"
			ndk.abiFilters.add("armeabi-v7a")
		}
	}

### Gradle exclude cpp files  

	exclude './../../deps/libuv/src/win/*.c'  
	exclude './../../deps/libuv/src/unix/aix.c'  
above don't work, you need beow  
	exclude '**/win/*.c'  

###c platform defnie   
defined (__FLASHPLAYER__) || defined(_FLASH)  
defined (__APPLE_CC__)  
defined (__ANDROID__)  

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

detail in  
https://link.zhihu.com/?target=http%3A//schacon.github.io/git/git-read-tree.html%23_sparse_checkout

###Import swift project to another swift project
"import $(SWIFT_MODULE_NAME)" in the swift file

###Djinni
http://mobilecpptutorials.com/your-first-cross-platform-djinni-app-part-1-cplusplus/
1. down djinni and gyp

	$ git submodule add https://github.com/dropbox/djinni.git deps/djinni
	$ git submodule add https://chromium.googlesource.com/external/gyp.git deps/gyp
gyp need to set to an older version

	$ cd deps/gyp
	$ git checkout -q 0bb67471bca068996e15b56738fa4824dfa19de0
2. genrate the interactive code
edit the djinni for c++ interface helloworld.djinni  
edit the sh script, run_djinni.sh  

	$  sh ./ run_djinni.sh
3. genrate the ios project
edit libhelloworld.gyp  
edit Mkefile  
	
	$ make ios
4. modify the ios project
delete jni src and jni config  
add libraries libhelloworld_objc.a and libdjinni_objc.a  
add User header Search Paths"   

	"$(SRCROOT)/../../deps/djinni/support-lib/objc"   
	"$(SRCROOT)/../../generated-src/objc"  
in swift project need to add a empty cpp file to enable c++ librarie support  
in objectc need to modify main.m to main.mm  

android has more holes than ios  
error: 'mutex' in namespace 'std' does not name a type  
cppFlags.add(“-D_GLIBCXX_HAS_GTHREADS”)  

more infomation  
http://tools.android.com/tech-docs/new-build-system/gradle-experimental?pli=1#TOC-Gradle-Requirements


https://codelabs.developers.google.com/codelabs/android-studio-jni/index.html?index=..%2F..%2Findex#0

###crash when hide keyboard
the "Editing Did End" event added in storyboard,  but I forget it, when the event send out, but there is no function to handle, or the function is nil, so it crash. It is easy but hard to find


###A valid provisioning profile for this executable was not found
change code signing to Developer

