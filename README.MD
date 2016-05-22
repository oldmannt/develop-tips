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


###WWDR intermediate certificate expired cause upload app error
the error message is "missing ios distribution signing identity for "
https://developer.apple.com/support/certificates/expiration/
From Apple -
Thanks for bringing this to the attention of the community and apologies for the issues you’ve been having. This issue stems from having a copy of the expired WWDR Intermediate certificate in both your System and Login keychains. To resolve the issue, you should first download and install the new WWDR intermediate certificate (by double-clicking on the file). Next, in the Keychain Access application, select the System keychain. Make sure to select “Show Expired Certificates” in the View menu and then delete the expired version of the Apple Worldwide Developer Relations Certificate Authority Intermediate certificate (expired on February 14, 2016). Your certificates should now appear as valid in Keychain Access and be available to Xcode for submissions to the App Store.

upload app keyword to keep me rember  
0. update WWDR
WWDR intermediate certificate
1. generate certificate
https://developer.apple.com/account/ios/certificate/distribution
2. add app id
https://developer.apple.com/account/ios/identifier/bundle
3. uploade app
configure in xcode, app bundle identifier, version, .....Busild Settings->Code Signing->Code Signing Identity ... Provisioning Profile
Producte->Archive

###add Admob
https://developers.google.com/admob/ios/quick-start#prerequisites
1. install cocoapods

	$ sudo gem install cocoapods
2. edit podfile
source 'https://github.com/CocoaPods/Specs.git'

	platform :ios, '7.0'

	target "USNIT" do
		pod 'Google-Mobile-Ads-SDK', '~> 7.8'
	end
3. $ pod update
4.  adding the two frameworks - CoreBluetooth and SafariServices 
5.  https://developers.google.com/admob/ios/quick-start  
i implement by code in AdmobBanner.swift

###A valid provisioning profile for this executable was not found
change code signing to Developer

