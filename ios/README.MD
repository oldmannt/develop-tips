#### call swift from C
make swift function assign to C functon pointer, then you can call swift from C

    func UsnitCallback(type: Int32, _ data: UnsafePointer<Void>)->Int32 { }  
    //the swift function type above is equal to the C function below, 
    typedef int (*my_cb_t)(int type, const void* data);  
    my_cb_t = UsnitCallback // this assignment is ok  
