### request permission
if targetSdkVersion if heigher than 23, you need to request permission. so the easy way is set targetSdkVersion lower than 23.
https://www.aswifter.com/2015/11/04/android-6-permission/
https://github.com/googlesamples/android-RuntimePermissions

### adb
https://developer.android.com/studio/command-line/adb.html#howadbworks

### android studio test suit
https://developer.android.com/studio/test/index.html

### Prepare for Release
1. turn off logging adn debugging
2. set version in gradle `versionCode 1  versionName "1.0"`
3. sign app

    ```gradle
    // Create a variable called keystorePropertiesFile, and initialize it to your
    def keystorePropertiesFile = rootProject.file("../../../android/keystore.properties")
    // Initialize a new Properties() object called keystoreProperties.
    def keystoreProperties = new Properties()
    // Load your keystore.properties file into the keystoreProperties object.
    keystoreProperties.load(new FileInputStream(keystorePropertiesFile))
    android {
        signingConfigs {
            release {
                keyAlias keystoreProperties['keyAlias']
                keyPassword keystoreProperties['keyPassword']
                storeFile file(keystoreProperties['storeFile'])
                storePassword keystoreProperties['storePassword']
            }
        }
        buildTypes {
            release {
                signingConfig signingConfigs.release
                minifyEnabled false
                proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
            }
        }
        ...
    }
    ```
4. buidl release

    ```sh
    cd android/usnit/ ->project directory
    chmod +x gradlew
    ./gradlew app:assembleRelease
    ```
    it will be signed and aligned
    
5. install to device for testing

    ```sh
    adb device
    adb -s device-id install xxx.apk 
    ```

### cmake for android studio
from "android.mk" to "gradle extension", now "cmake"..., it's long way full of holes, google must be hate c++ programer. fortunatly cmake work ok

1. gradle
app/CMakeLists.text 

  ```gradle
  defaultConfig{
    externalNativeBuild{
        cmake {
            //targets "target1"
            //arguments "-DANDROID_TOOLCHAIN=clang"
            cFlags "-std=c11","-DZF_LOG_USE_ANDROID_LOG"
            cppFlags "-std=c++11","-fexceptions","-frtti","-D_GLIBCXX_HAS_GTHREADS"
            abiFilters "armeabi-v7a", "x86_64"
        }
    }
  }
  externalNativeBuild{
        cmake{
            path "CMakeLists.txt"
        }
    }
  ```
2. 
  
  ```cmake
  cmake_minimum_required(VERSION 3.4.1)
  
  set(CMAKE_VERBOSE_MAKEFILE on)
  
  # include headers locale path is "project/app"
  include_directories(../../../gearsbox/deps/djinni/support-lib)
  include_directories(../../../gearsbox/deps/djinni/support-lib/jni)

  # source files list
  # recurse search
  file(GLOB_RECURSE DJINNI ../../../gearsbox/deps/djinni/support-lib/jni/*.c* *.h*)
  file(GLOB_RECURSE GEARS_GEN ../../../gearsbox/generated-src/*.c* *.h*)
  # add source files one by one
  file(GLOB_RECURSE LIBUV ../../../gearsbox/deps/libuv/src/fs-poll.c
  ../../../gearsbox/deps/libuv/src/inet.c
  ../../../gearsbox/deps/libuv/src/threadpool.c)
  
  # build shared library
  add_library(usnit_jni SHARED ${DJINNI} ${GEARS_GEN} ${LIBUV})
  
  # build native_app_glue as a static lib
  include_directories(${ANDROID_NDK}/sources/android/native_app_glue)
  add_library(app-glue STATIC
            ${ANDROID_NDK}/sources/android/native_app_glue/android_native_app_glue.c)
  
  # add lib dependencies
  target_link_libraries(usnit_jni android log dl app-glue)
  ```
  
### if google service invalib, let ad banner gone

  ```java
  int gps = GoogleApiAvailability.getInstance().isGooglePlayServicesAvailable(context);
  if (gps != ConnectionResult.SERVICE_DISABLED &&
          gps != ConnectionResult.SERVICE_INVALID &&
          gps != ConnectionResult.SERVICE_MISSING){
      MobileAds.initialize(context, appid);
      // Gets the ad view defined in layout/ad_fragment.xml with ad unit ID set in
      // values/strings.xml.
      mAdView = (AdView) adview;
  }
  else {
      LogGen.instance().logerrf("google service invalid:"+ GoogleApiAvailability.getInstance().getErrorString(gps));
      adview.setVisibility(View.GONE);
  }
  ```

### permission 

  <uses-permission android:name="android.permission.INTERNET" />
  
  
### avoid call onCreate when rotate

    <activity
      android:name=".MainActivity"
      android:configChanges="orientation|keyboardHidden|screenSize">
    </activity>
  
add onConfigurationChanged

    ``` java
     @Override
    public void onConfigurationChanged(Configuration newConfig) {
        super.onConfigurationChanged(newConfig);

        // Checks the orientation of the screen
        if (newConfig.orientation == Configuration.ORIENTATION_LANDSCAPE) {
            Toast.makeText(this, "landscape", Toast.LENGTH_SHORT).show();
        } else if (newConfig.orientation == Configuration.ORIENTATION_PORTRAIT){
            Toast.makeText(this, "portrait", Toast.LENGTH_SHORT).show();
        }
    }
    ```

### alignParentLeft vs alignParentStart
It depends on the layout direction. The layout direction can be either left-to-right (start = left, end = right), or right-to-left (vice versa).  

By default, the layout direction is based on the locale (left-to-right for languages like English, right-to-left for languages like Arabic), but you can override it with the layoutDirection XML attribute or setLayoutDirection function.   e.g.:  

android:layoutDirection="ltr"     
^ will make alignParentStart equivalent to alignParentLeft on all devices.  
  
android:layoutDirection="rtl"     
  
### top space, leading space, trailing space

    // to parent's top, leading
    <TextView
        android:text="1234567890"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:id="@+id/textView1"
        android:layout_marginStart="14dp"
        android:layout_marginTop="14dp"
        android:layout_alignParentTop="true"
        android:layout_alignParentStart="true" />
        
    //  trailing, equal top
    <TextView
        android:text="TextView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignTop="@+id/textView1"
        android:layout_toEndOf="@+id/textView1"
        android:layout_marginStart="13dp" // tailing space
        android:id="@+id/textView3" />
        
    // bottom space, equal leading 
    <TextView
        android:text="1234567890"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:id="@+id/textView5"
        android:layout_below="@+id/textView1"
        android:layout_alignStart="@+id/textView1"
        android:layout_marginTop="14dp"/>
        
            
    <TextView
        android:text="TextView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignTop="@+id/textView1"
        android:id="@+id/textView3"
        android:layout_toEndOf="@+id/textView1" // leading to trailing
        android:layout_toStartOf="@+id/centersapce"/> // trailing to leading
### 

### define a percentage for a width
90% of parent and center horizontal

    <LinearLayout
        android:orientation="horizontal"
        android:layout_width="fill_parent"
        android:layout_height="1px"
        android:layout_weight="1">

        <Space
            android:layout_width="0px"
            android:layout_height="0px"
            android:layout_weight="0.05"/>

        <View
            android:layout_width="0px"
            android:layout_height="1px"
            android:layout_weight="0.9"
            android:id="@+id/view" />

        <Space
            android:layout_width="0px"
            android:layout_height="0px"
            android:layout_weight="0.05"/>
    </LinearLayout>

### relativelayout margin right/left from center
add an invisable space, then set endof/alighstartof
    <Space
        android:layout_height="0dp"
        android:layout_centerHorizontal="true"
        android:id="@+id/centersapce"
        android:layout_width="0dp" />
        
    <TextView
        android:text="1234567890"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:id="@+id/textView2"
        android:layout_toEndOf="@+id/centersapce" />

###
https://gist.github.com/ph0b/0575b30b67e04f2ec10f

### Activity Lifecycle
http://blog.csdn.net/android_tutor/article/details/5772285  
https://developer.android.com/reference/android/app/Activity.html  
![image](https://github.com/oldmannt/develop-tips/raw/master/android/activity_lifecycle.png) 

##android tip  
### get source 'file' 'line' 'function' in jave

    String fullClassName = Thread.currentThread().getStackTrace()[2].getClassName();
    String className = fullClassName.substring(fullClassName.lastIndexOf(".") + 1);
    String methodName = Thread.currentThread().getStackTrace()[2].getMethodName();

#### Generating the release unsigned build .apk
android studio 2.2

      1. Build->Select Build Variant
      2. Select xxxRelease
      
### link java folder in gradle

      sourceSets {
            main.java.srcDirs += '../../../generated-src/java'
      }

### main thread loop  
there must be a better one

      s_handler = new Handler(){
        private long last = System.currentTimeMillis();
        public void handleMessage( Message msg ) {
            switch (msg.what){
                case 999:{
                    long current = System.currentTimeMillis();
                    AsyncLoopGen.instance().process(current-last);
                    last = current;
                }
                default:
                    break;
            }// end switch
        }
    };

    m_timer = new Timer();
    m_timer.schedule(new TimerTask() {
        public void run() {
            s_handler.sendEmptyMessage(999);
        }
    }, 0, 1000);
