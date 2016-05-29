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
