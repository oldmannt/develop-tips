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
