### xcode time.h conflict
<google/protobuf/stubs/time.h> is conflict with <time.h>
set `Build Settings->Search Paths->Always Search User Paths` to false

### protocbuf
I want to used python write the data, then read by c++ in ios and android, and flash maybe  
1.download Protocol Buffers v3.0.0-beta-3 cpp and python, after downloaded just merge  
2.build protocbuf  
https://developers.google.com/protocol-buffers/docs/cpptutorial#defining-your-protocol-format  

	$ ./autogen.sh
	$ ./configure
	$ make
	$ make check
	$ sudo make install
	$ sudo ldconfig # refresh shared library cache. mac don't need this
	$ protoc --version 
static,shared and exec all in src/.lib, copy the files, then make clean to clean the huge compiled files  
I need `libprotobuf.a`, be linked in c++, to read the data files  
3.install protocbuf for python  
https://github.com/google/protobuf/tree/master/python  

	$ python setup.py build  
	$ python setup.py test  
	$ sudo python setup.py install   
4.generate .h .cc, .py file for writing and reading  

	base_dir=$(cd "`dirname "0"`" && pwd)
	proto_input="$base_dir/proto"
	cpp_out="$base_dir/cpp"
	python_out="$base_dir/python/"
	rm -rf $cpp_out
	rm -rf $python_out
	mkdir $cpp_out
	mkdir $python_out
	touch $python_out/__init__.py
	protoc -I=$proto_input \
	   --cpp_out=$cpp_out  \
	   --python_out=$python_out \
	   $proto_input/person.proto
5-make a ios static libarey project  
find src/Makefile.am, check the source files of `libprotobuf.a` that's what I need to build libarey for ios and android, try to write a gyp file

### import py file in subdirectory
need to add `__init__.py` in the subdirectory
import uplevel directory

	-- src
	    |-- mod1.py
	    |-- lib
	    |    |-- mod2.py
	    |	 |-- __init__.py
	    |-- sub
	    |    |-- test2.py

	import sys
	sys.path.append("..")
	import mod1
	import lib.mod2
### sublime text3 for python
1. enable `subl` command  

		$ sudo ln -s /Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl /yourpath/subl
		$ echo "export PATH=~/bin:$PATH" >> ~/.profile
2. install package control  
View->Show Console

		import urllib.request,os,hashlib; h = '2915d1851351e5ee549c20394736b442' + '8bc59f460fa1548d1514676163dafc88'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)  
then `cmd+shift+P` enter `install Package`, now you can install packages
3. install SideBarEnhancements  
4. Anaconda  
5. GitGutter
6. SublimeREPL  
get input


### Protocol Buffers
download protobuf3.0beta3

	$ ./autogen.sh
	$ ./configure
	$ make
	$ make check
	$ sudo ldconfig # refresh shared library cache. mac don't need this
	$ protoc --version 

https://developers.google.com/protocol-buffers/docs/cpptutorial#defining-your-protocol-format  

### shared_from_this causing bad_weak_ptr crash
using shared_from_this() on an object which has no shared_ptr pointing to it. This violates a precondition of shared_from_this(), namely that at least one shared_ptr must already have been created (and still exist) pointing to this.

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

