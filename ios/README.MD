### uiviewcontroller lifecycel
![image](https://github.com/oldmannt/develop-tips/raw/master/ios/uiviewcontroller-lifecycle.png)  
`loadView` — Creates the view that the controller manages.  
It’s only called when the view controller is created and only when done programatically. You can override this method in order to create your views manually.

`viewWillLayoutSubviews`  — Called to notify the view controller that its view is about to layout its subviews.  
This method is called every time the frame changes like for example when rotate or it’s marked as needing layout. It’s the first step where the view bounds are final. If you are not using autoresizing masks or constraints and the view size changes you probably want to update the subviews here.

`viewDidLayoutSubviews` Called to notify the view controller that its view has just laid out its subviews.  
Make additional changes here after the view lays out its subviews.


### share video to another app
	```swift
	let cell_data:LPAProjectCellGen? =  LPAProjectListGen.instance()?.getProjectData(-1)	
	if nil != cell_data{

		let video_url:URL = URL(fileURLWithPath: cell_data!.getPath())
		let activity_vc = UIActivityViewController(activityItems: [video_url], applicationActivities: nil	)
		super.m_popbase?.present(activity_vc, animated: true, completion: nil)
	}
	```

### UIViewController-rotate-flow
https://developer.apple.com/library/prerelease/content/featuredarticles/ViewControllerPGforiPhoneOS/TheAdaptiveModel.html#//apple_ref/doc/uid/TP40007457-CH19-SW1
![image](https://github.com/oldmannt/develop-tips/raw/master/ios/uiviewcontroller-rotate-flow.png) 

### UITableView add/delete cell by projrammatically

	```swift
	// build indexpath
	let indexPath: IndexPath = IndexPath(row: i, section: 0)
	
	func deleteItem(index:IndexPath) {
		m_table_view.beginUpdates()
		if m_table_view.numberOfRows(inSection: 0) > index.row {
			m_table_view.deleteRows(at: [index], with: .right)
		}
		m_table_view.endUpdates()
	}

	func addItem(index:IndexPath) {
		m_table_view.beginUpdates()
		m_table_view.insertRows(at: [index], with: .right)
		m_table_view.endUpdates()
	}
	```

### open keyword in swift3
	A open class is accessible and subclassable outside of the defining module. A open class member is accessible and overridable outside of the defining module.  
	A public class is accessible but not subclassable outside of the defining module. A public class member is accessible but not overridable outside of the defining module.  
http://stackoverflow.com/questions/38947101/what-is-the-open-keyword-in-swift

### long press for tableview

	```swift
	@IBOutlet weak var m_table_view: UITableView!
    
	var m_project_setting_view: ProjectSettingView?
	override func viewDidLoad() {
		super.viewDidLoad()
		m_project_setting_view = ProjectSettingView(nibName: "project_setting_view", bundle: nil)
		m_project_setting_view?.setPopbase(self)
		let longPressRecognizer = UILongPressGestureRecognizer(target: self, action: #selector(ProjectsViewController.longPress))
		self.view.addGestureRecognizer(longPressRecognizer)
	}
	
    func longPress(longPressGestureRecognizer: UILongPressGestureRecognizer) {
        if longPressGestureRecognizer.state == UIGestureRecognizerState.Ended {
            
            let touchPoint = longPressGestureRecognizer.locationInView(self.m_table_view)
            if let indexPath = m_table_view.indexPathForRowAtPoint(touchPoint) {
                // your code here, get the row for the indexPath or do whatever you want
                let cell = m_table_view.cellForRowAtIndexPath(indexPath)
                let pos = cell?.convertPoint(CGPoint(x:0,y:0), toView: self.view)
                self.presentpopupViewController(m_project_setting_view!, pos: pos!, size: (cell?.contentView.frame.size)!,animationType: .RightLeft, completion: nil)
            }
        }
    }
	```

### image fit mode
![image](https://github.com/oldmannt/develop-tips/raw/master/ios/image_fit_mode.png)  

### button with tittle under image   
	
	```swift
	class UIButtonBottomTittle: UIButton {
	    override func layoutSubviews() {
		super.layoutSubviews()

		let btn_h = self.frame.size.height
		let img_h = self.imageView?.frame.size.height
		let lab_h = self.titleLabel?.frame.size.height

		self.imageView?.center.x = self.center.x
		self.imageView?.frame.origin.y = btn_h - img_h! - lab_h!
		self.titleLabel?.center.x = self.center.x
		self.titleLabel?.frame.origin.y = btn_h - lab_h!
		self.titleLabel?.sizeToFit()
	    }
	} 
	```

### `CVPixelBufferLockBaseAddress` failed return `kCVReturnInvalidArgument`(-6661)
this is serious problem...  
invoke `m_stillImageOutput.captureStillImageAsynchronouslyFromConnection`, get the sampleBuffer in callback  
	
	```swift
	CVPixelBufferRef imageBuffer = CMSampleBufferGetImageBuffer(sampleBuffer);
        CVReturn rt = CVPixelBufferLockBaseAddress(imageBuffer, kCVPixelBufferLock_ReadOnly);
        ```
`CVPixelBufferLockBaseAddress` failed return kCVReturnInvalidArgument(-6661), we need to set `PixelFormatType` before invoke `captureStillImageAsynchronouslyFromConnection`

	```swift
	let dctPixelFormatType : Dictionary<NSString, NSNumber> = [kCVPixelBufferPixelFormatTypeKey : NSNumber(unsignedInt: kCVPixelFormatType_420YpCbCr8BiPlanarVideoRange)]
        
        m_stillImageOutput.outputSettings = dctPixelFormatType

        if m_captureSession.canAddOutput(m_stillImageOutput) {
            m_captureSession.addOutput(m_stillImageOutput)
        }
	```
http://stackoverflow.com/questions/9957427/cant-get-cvimagebufferref-in-capturestillimageasynchronouslyfromconnection  
### in AutoLayout, we need to move view by constraint
1. outlets constraint to viewcontroller  
2. update constraint in run time  
views will be reset by constraints after lablel's text change or other conditions
### animate
1. fade out in 0.2 second
	
	```swift
	UIView.animateWithDuration(0.2, animations: {
	    self.blurBg.alpha = 1
	}, completion: {
	    (value: Bool) in
	    self.blurBg.hidden = true
	})
	```
2. scale to 0.5 in 0.5 second

	```swift
	UIView.animateWithDuration(0.5, animations: {
                self.m_exposure_sel.transform = CGAffineTransformScale(self.m_exposure_sel.transform, 0.5, 0.5)
            }, completion: {
                (value: Bool) in
                print("tapView done")
        })
	```

### `pan gesture recognizer` to drag view
1. add an `Pan Gesture Recognizer` in storyboard, and connect to view by control and drag
2. add action in viewcontroller by control and drag `Pan Gesture Recognizer`

	```swift
	@IBAction func dragExposureSel(sender: UIPanGestureRecognizer) {
		let exposure_sel = sender.view
		if nil == exposure_sel {
			return
		}
		if sender.state == UIGestureRecognizerState.Began ||
		   sender.state == UIGestureRecognizerState.Changed {
			let translation = sender.translationInView(exposure_sel?.superview)
			exposure_sel?.center = CGPoint(x: (exposure_sel?.center.x)!+translation.x,
										   y: (exposure_sel?.center.y)!+translation.y)
			sender.setTranslation(CGPointZero, inView: exposure_sel?.superview)
		}
	}
	```

### format string

	```swift
	String(format: "1/%.00f", 9.11) // 9
	String(format: "1/%.01f", 9.11) // 9.1
	```
	
### CMTime
	value/timescale = seconds, timescale like fps

### detect rotation
add `UIDeviceOrientationDidChangeNotification` observer in viewWillAppear, remove observer in viewDidDiss
	
	```swift
	override func viewWillAppear(animated: Bool) {
        NSNotificationCenter.defaultCenter().addObserver(self, selector: #selector(ViewController.screenRotate), name: UIDeviceOrientationDidChangeNotification, object: nil)
    }
    
    override func viewDidDisappear(animated: Bool) {
        super.viewDidAppear(animated)
        NSNotificationCenter.defaultCenter().removeObserver(self)
    }
    
    func screenRotate() {
        print("screen rotate: \(UIApplication.sharedApplication().statusBarOrientation)")
        //let ori:UIDeviceOrientation = UIDevice.currentDevice().orientation
        camera_controller.rotateScreen()
    }
	```


### crash:NSInvalidArgumentException' unrecognized selector sent to instance
If it happened in button's action, may be the button's action connect to two outlets, one of the outlet's code was delete. 
### error:"Loaded nib but the view outlet was not set"
http://stackoverflow.com/questions/4763519/loaded-nib-but-the-view-outlet-was-not-set-new-to-interfacebuilder  
![image](https://github.com/oldmannt/develop-tips/raw/master/ios/set_view_outlet1.jpg)    
![image](https://github.com/oldmannt/develop-tips/raw/master/ios/set_view_outlet2.jpg)  
### make UILabel autosize by text
1. storyboard
	Editor > Size to Fit Content (keyboard shortcut: Cmd =)
2. programmatically

	```swift
	testLabel.numberOfLines = 0
	testLabel.sizeToFit()
	```

### ERROR ITMS-90096: "Your binary is not optimized for iPhone 5 
1. create a png file name "Default-568.png", the size must be 320 by 568, drag it to the root of app project
2. add below to info.xml
	
	```xml
	<key>UILaunchImages</key>
	<array>
	    <dict>
	        <key>UILaunchImageName</key>
	        <string>Default-568</string>
	        <key>UILaunchImageSize</key>
	        <string>{320, 568}</string>
	    </dict>
	</array>
	```
done

### cmaera fullscreen capture view missing halfly, when landscapce
reset frame of previewLayer

	```swift
	m_previewLayer?.frame = UIScreen.mainScreen().bounds
	```
### automaticly open keyboard for textfield
	text_field.becomeFirstResponder() in didload or didappear

### how to tell path is file or folder, and iterator folder

	```swift
    let filemanager:NSFileManager = NSFileManager()
    var is_dir:ObjCBool = false
    let files:NSDirectoryEnumerator? = filemanager.enumeratorAtPath(path)
    while let file = files?.nextObject() as? String {
        
        filemanager.fileExistsAtPath(path+"/\(file)", isDirectory: &is_dir)
        print(is_dir ? "is directory" : "is a file")
        if file.hasSuffix("json"){
            print(file)
        }
    }
    ```
    
    another way
    
    ```swift
    var subs:[String] = []
    do {
        subs = try filemanager.subpathsOfDirectoryAtPath(path)
    }catch let error as NSError{
        print("SFUsnitLogic.init write failed \(error.userInfo) ")
    }

    let totalFiles = subs.count
    print(totalFiles)
    for sub in subs {
        
        if sub.rangeOfString(".DS_Store") != nil {
            //a DS_Store file
        } else if sub.rangeOfString(".xcassets") != nil {
            //a xcassets file
        } else if (sub as NSString).substringWithRange(NSRange(location: 0, length: 4)) == ".git" {
            //a git file
        } else if sub.hasSuffix("json") {
            print("json")
        }
        let fullPath = path+("/\(sub)")
        print(fullPath)
    }
	```

### Undefined symbols for architecture x86_64
if the link errors are all about std::string, it turns out when there isn't cpp file in project, it assumes isn't required. So just add an empty cpp file "justforlink.cpp"

### compile ffmepg
	```sh
	# install yasm 1.2
	curl http://www.tortall.net/projects/yasm/releases/yasm-1.2.0.tar.gz >yasm.tar.gz
	tar xzvf yasm.tar.gz
	cd yasm-1.2.0
	./configure
	make
	sudo make install
	# or ./configure && make -j 4 && sudo make install
	```
	
download FFmpeg-iOS-build-script, edit `build-ffmpeg.sh`  
change `#X264=`pwd`/fat-x264` to `X264=`pwd`/fat-x264`

	```sh
	# compile script
	cd /workingdirecotry
	git clone https://github.com/kewlbear/FFmpeg-iOS-build-script.git
	cd FFmpeg-iOS-build-script
	sudo ./build-ffmpeg.sh
	```

### opencv Undefined symbols for architecture arm64:
undefined symbols for architecture arm64:
“_png_init_filter_function_neon”, referenced from:
	_png_read_filter_row in opencv2(pngrutil.o)
ld: symbol(s) not found for architecture arm64

http://answers.opencv.org/question/87370/error-compiling-ios-app-with-opencv-framework/
"this case it seems your hardware is not supporting NEON optimizations. Could you explicitly disable them in the cmake configuration?"
I modify 
	
	```python
    if arch.startswith("armv"):
    	cmakecmd.append("-DENABLE_NEON=ON")
    ```
to
	```python
    if arch.startswith("arm"):
    	cmakecmd.append("-DENABLE_NEON=ON")
	```
then rebuild opencv2, png link error dismiss.
  

### opencv building

http://docs.opencv.org/3.1.0/d5/da3/tutorial_ios_install.html#gsc.tab=0
Make symbolic link for Xcode to let OpenCV build scripts find the compiler, header files etc.

	```sh
    cd /
    sudo ln -s /Applications/Xcode.app/Contents/Developer Developer
    ```
    
Build OpenCV framework:

	```sh
    cd ~/<my_working_directory>
    python opencv/platforms/ios/build_framework.py ios
    ```

trubole:
1. permission, cmake missing
2. libtool:   error: unrecognised option: '-static'
modify `execute(["/usr/bin/libtool", "-static", "-o", res] + libs + libs3)`
to	   `execute(["libtool", "-static", "-o", res] + libs + libs3)`
I don't know why there two `libtool` in my mac.

libtool
I get an error when I was building opencv.
`libtool:   error: unrecognised option: '-static'`



###  multilines UILabel
set numberOfLines to 0 (and the label to word wrap), the label will automatically wrap and use as many of lines as needed.

### after add subviews in scrollview can't scroll to the end  
adjest the contentSize of scrollview in `viewDidLayoutSubviews()` of viewcontroller, it be invoked after the constraints apply
	```swift
	override func viewDidLayoutSubviews() {
	        super.viewDidLayoutSubviews()
	        
	        var maxHeight : CGFloat = 0
	        for view in viewUnit.subviews {
	            let newHeight = view.frame.origin.y + view.frame.height
	            if newHeight > maxHeight {
	                maxHeight = newHeight
	            }
	        }
	        // set content size
	        
	        viewSC.contentSize = CGSize(width: viewSC.contentSize.width, height: maxHeight)
	 }
	 ```
### show documents directory in Mac's itunes when device connected
in info.plist add item `Applicaton supports iTunes file sharing` and set `YES`

### The Upload to App Store and Validate buttons are grayed out in the Archives Organizer
	set `Skip Install` to true in static library project
	https://developer.apple.com/library/ios/technotes/tn2215/_index.html
	
### copy files form bundle to document
	
		let res_path = NSBundle.mainBundle().pathForResource("www", ofType: "bin")
        var doc_path:String = NSSearchPathForDirectoriesInDomains(.DocumentDirectory, .UserDomainMask, true)[0] as String
        doc_path.appendContentsOf("/www.bin")

        var fileMgr = NSFileManager.defaultManager()
        if fileMgr.copyItemAtPath(res_path, toPath: doc_path) != true{
            print("copy done")
        }
        else{
            print("copy failed")
        }


### constraints conflicting h=--& v=--& xxxx:.midX ==>
Visual Format Language  
h->horizontal v->vertical  
h=--& fixed x, fixed w, flexible,right margin  
v=--& fixed y, fixed h, flexible,bottom margin  
add constraints pragmatically, should set `translatesAutoresizingMaskIntoConstraints` false, by default, that is ture, so the autoresizing mask on uiviews are translated to additional constraints, which will conflicting with constraints that you add.

	myTextField.translatesAutoresizingMaskIntoConstraints = false;
	
https://developer.apple.com/library/ios/documentation/UserExperience/Conceptual/AutolayoutPG/VisualFormatLanguage.html
https://developer.apple.com/library/ios/documentation/UserExperience/Conceptual/AutolayoutPG/DebuggingTricksandTips.html

### add scrollable scrollview by storyboard
1. add a scrollview
2. add a view into scrollview, all the content should be added into this view
3. add constraints make view's board equal to scrollview's board
4. add constraints make scrollview's top and bottom equal to topMargin
5. add constraints make scrollview's width and centerX equal to parent view
6. add constraints make view's width and height equal to scrollview's parent, set the height constraint's priority to 250
![image](https://github.com/oldmannt/develop-tips/raw/master/ios/scrollview-storyboard.png)  

### add a View Controller to Tab Bar Controller
Drag a `UITableViewController` instance from the **Object Library** to the workspace and set its class to `YourViewController` in the **Identity Inspector**. Select the view controller's table view and set **Prototype Cells** to 0 in the **Attributes Inspector**.  
To add the authors view controller to the tab bar controller's array of view controllers, drag from the tab bar controller to the authors view controller, holding down the **Control** key. Select **Relationship Segue > view controllers** from the menu that appears.  
http://code.tutsplus.com/tutorials/ios-from-scratch-with-swift-exploring-tab-bar-controller--cms-25470  
![image](https://github.com/oldmannt/develop-tips/raw/master/ios/figure-adding-table-view-controller.jpg)  


### passing data to another view controller

	override func prepareForSegue(segue: UIStoryboardSegue!, sender: AnyObject!) {
	    if (segue.identifier == "Load View") {
	        // pass data to next view
	    }
	}

### get point from UITagGestureRecognizer

	let point:CGPoint = sender.locationInView(sender.view)

### #selector
Using #selector will check your code at compile time to make sure the method you want to call actually exists. Even better, if the method doesn’t exist, you’ll get a compile error: Xcode will refuse to build your app, thus banishing to oblivion another possible source of bugs.  
https://swift.org/blog/swift-2-2-new-features/

	override func viewDidLoad() {
	    super.viewDidLoad()
	
	    navigationItem.rightBarButtonItem =
	        UIBarButtonItem(barButtonSystemItem: .Add, target: self,
	                        action: #selector(addNewFireflyRefernce))
	}
	
	func addNewFireflyReference() {
	    gratuitousReferences.append("Curse your sudden but inevitable betrayal!")
	}

### detect the type of a variant

	let view:UIView = digitsOnlyTextField;
    if view is UIControl{
		print(view.dynamicType) // UITextField
    }

### add constraint for views
use admob for exsmple

	view.addConstraint(NSLayoutConstraint(item: bannerView, attribute: .Bottom,
            relatedBy: .Equal, toItem: rootController.view , attribute: .Bottom, multiplier: 1, constant: -offsety))

###set background color of uiview

	m_view.backgroundColor = UIColor(colorLiteralRed: r, green: g, blue: b, alpha: a)

###remove a subview
get subview variant, invoke removeFromSuperview

	getUIView().removeFromSuperview()

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
implement by code in AdmobBanner.swift

###update Admob
modfiy Podfile, from 7.8.0 -> 7.8.1

	source 'https://github.com/CocoaPods/Specs.git'
	
	platform :ios, '7.0'
	
	target "usnit_app" do
	-pod 'Google-Mobile-Ads-SDK', '~> 7.8.0'
	+pod 'Google-Mobile-Ads-SDK', '~> 7.8.1'
	end
	
in project directory run  

	pod update


#### distribution
upload app keyword to keep me rember  
0. update WWDR  
WWDR intermediate certificate  
1. Create App ID
developer.apple.com->Account->Certificates->Idenitifiers->"+" to create an App ID  
2. Create Production Certificates(If created, pass)  
&ensp;&ensp;&ensp;&ensp;developer.apple.com->Account->Certificates->Production->"+"->"App Store and Ad Hoc"  
&ensp;&ensp;&ensp;&ensp;Create a CSR file. just do as the page said  
&ensp;&ensp;&ensp;&ensp;Back to the page -> continue-> choose the file you have just created  
&ensp;&ensp;&ensp;&ensp;->download certificate file "*.csr"-> Double click to import  
3. Create Provisioning Profiles  
&ensp;&ensp;&ensp;&ensp;developer.apple.com->Account->Certificates->  
&ensp;&ensp;&ensp;&ensp;Provisioning Profiles->All->"+"->App Store->continue...->Generate->Download->"YOUR_PROFILE"  
4. iTunes Connect->new APP  
5. XCode  
&ensp;&ensp;&ensp;&ensp;BuildSetting->Code Signing->  
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;Code Signing Identity->IPhone Distribution  
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;Provisioning Profile->"YOUR_PROFILE"  
&ensp;&ensp;Genneral->Identity  
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;Version,Build,Bundle Identifier  
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;Team, should not have a warnning  
&ensp;&ensp;&ensp;&ensp;Scheme Edit...->Run->Release, uncheck "Debug excutable"  
&ensp;&ensp;&ensp;&ensp;Product->Archive  

###WWDR intermediate certificate expired cause upload app error   
the error message is "missing ios distribution signing identity for "  
https://developer.apple.com/support/certificates/expiration/  
From Apple -  
Thanks for bringing this to the attention of the community and apologies for the issues you’ve been having. This issue stems from having a copy of the expired WWDR Intermediate certificate in both your System and Login keychains. To resolve the issue, you should first download and install the new WWDR intermediate certificate (by double-clicking on the file). Next, in the Keychain Access application, select the System keychain. Make sure to select “Show Expired Certificates” in the View menu and then delete the expired version of the Apple Worldwide Developer Relations Certificate Authority Intermediate certificate (expired on February 14, 2016). Your certificates should now appear as valid in Keychain Access and be available to Xcode for submissions to the App Store. 

#### call C from swift

1.include C header file in XX-Briding-Header.h `#include "usnit.h"'  
2.browce `usnit.h' in xcode, select 'Counterparts'-> 'usnit.h(interface)', xcode will show the swift interface of c fuction

    #define LANG_CH     1
    #define LANG_ENG    2
    typedef int (*my_cb_t)(int type, const void* data);
    int     UsnitInit(const char* conf_str, int lang, my_cb_t cb_func);

C fucntion above, swift interface below, magic isn't it

    public var LANG_CH: Int32 { get }
    public var LANG_ENG: Int32 { get }
    public typealias my_cb_t = @convention(c) (Int32, UnsafePointer<Void>) -> Int32
    public func UsnitInit(conf_str: UnsafePointer<Int8>, _ lang: Int32, _ cb_func: my_cb_t!) -> Int32

#### call swift from C
make swift function assign to C functon pointer, then you can call swift from C

    func UsnitCallback(type: Int32, _ data: UnsafePointer<Void>)->Int32 { }  
    //the swift function type above is equal to the C function below, 
    typedef int (*my_cb_t)(int type, const void* data);  
    my_cb_t = UsnitCallback // this assignment is ok  
