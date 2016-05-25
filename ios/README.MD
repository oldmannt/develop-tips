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
