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
