### lock_guard
another way, it doesn't looks better than unique_look
   ```C++
   if (_mutex.try_lock()) { 
       std::lock_guard<std::mutex> guard(_mutex, std::adopt_lock);
       if (m_queue_mt_excuser.size()!=0){
           // critical setion
       }
   } // mutex will be unlocked here
   ```

### unique_lock
unique_lock is movable but not copyable.
1. unique_lock() noexcept;   //empty unique_lock
2. explicit unique_lock (mutex_type& m); //own mutex，invoke mutex.lock()      
3. unique_lock (mutex_type& m, try_to_lock_t tag); //invoke mutex.try_lock()
4. unique_lock (mutex_type& m, defer_lock_t tag) noexcept;// don't lock, just manager, will unlock when it die
5. unique_lock (mutex_type& m, adopt_lock_t tag);//m was locked when I born, I'll unlock m when I die
6. template <class Rep, class Period>  
   unique_lock (mutex_type& m, const chrono::duration<Rep,Period>& rel_time);// mutex.try_lock_for(rel_time)  
7. template <class Clock, class Duration>  
   unique_lock (mutex_type& m, const chrono::time_point<Clock,Duration>& abs_time);//mutex.try_lock_until(abs_time)
8.unique_lock (const unique_lock&) = delete; // disable copy constructor  
9.unique_lock (unique_lock&& x); // move

    ```C++
    std::unique_lock<std::mutex> try_lock(m_mt_task, std::try_to_lock);
    if (try_lock.owns_lock() && m_queue_mt_excuser.size()!=0){
        // critical section
    }
    ```

### lambda
![image](https://github.com/oldmannt/develop-tips/raw/master/cpp/lamda01.jpeg)  
https://msdn.microsoft.com/zh-cn/library/dd293608.aspx  
1. capture clause (Also known as the lambda-introducer in the C++ specification.)  
2. parameter list Optional.  (Also known as the lambda declarator)  
3. mutable specification Optional.  
4. exception-specification Optional.  
5. trailing-return-type Optional.  
6. lambda body)  
### time
    
    ```c++
    //getTickCount by millisecond, in mac64, long long is 8 bits
    long long nowMilli(){
        using namespace std::chrono;
        return duration_cast<milliseconds>(steady_clock::now().time_since_epoch()).count();
    }
    ```
    

### std::move
http://www.cplusplus.com/reference/utility/move/  

    ```c++
    std::string bar = "bar-string";
    std::string xx = std::move(bar); // x == "bar-string", bar unspecified 
    ```
    move `bar` to xx, then destory bar, work on stl type
### std::ref  
std::ref<T> pass reference  

### shared_ptr manager resource


    std::shared_ptr<FILE> auto_close(fopen("test.txt","r"),&fclose);

### sleep 

    std::this_thread::sleep_for(std::chrono::seconds(1));
    std::this_thread::sleep_for(std::chrono::milliseconds(1));

### about implement std::bind
http://en.cppreference.com/w/cpp/utility/functional/bind
http://blog.think-async.com/2010/04/bind-illustrated.html  
![image](https://github.com/oldmannt/develop-tips/raw/master/cpp/bind01-plain-function-one-var-zero-args.png) 
![image](https://github.com/oldmannt/develop-tips/raw/master/cpp/bind02-member-function-one-var-zero-args.png) 
![image](https://github.com/oldmannt/develop-tips/raw/master/cpp/bind03-member-function-zero-vars-one-arg.png) 
![image](https://github.com/oldmannt/develop-tips/raw/master/cpp/bind04-member-function-one-var-one-arg.png) 
![image](https://github.com/oldmannt/develop-tips/raw/master/cpp/bind05-plain-function-one-var-two-args.png) 
![image](https://github.com/oldmannt/develop-tips/raw/master/cpp/bind06-plain-function-one-var-two-args-second-ignored.png) 
![image](https://github.com/oldmannt/develop-tips/raw/master/cpp/bind07-plain-function-one-var-two-args-first-ignored.png) 
![image](https://github.com/oldmannt/develop-tips/raw/master/cpp/bind08-plain-function-one-var-two-args-reordered.png) 

### std::function sample
http://en.cppreference.com/w/cpp/utility/functional/function
http://www.jellythink.com/archives/771
    ```c++
    #include <functional>
    #include <iostream>

    struct Foo {
        Foo(int num) : num_(num) {}
        void print_add(int i) const { std::cout << num_+i << '\n'; }
        int num_;
    };

    void print_num(int i)
    {
        std::cout << i << '\n';
    }

    struct PrintNum {
        void operator()(int i) const
        {
            std::cout << i << '\n';
        }
    };

    int main()
    {
        // store a free function
        std::function<void(int)> f_display = print_num;
        f_display(-9);

        // store a lambda
        std::function<void()> f_display_42 = []() { print_num(42); };
        f_display_42();

        // store the result of a call to std::bind
        std::function<void()> f_display_31337 = std::bind(print_num, 31337);
        f_display_31337();

        // store a call to a member function
        std::function<void(const Foo&, int)> f_add_display = &Foo::print_add;
        const Foo foo(314159);
        f_add_display(foo, 1);

        // store a call to a data member accessor
        std::function<int(Foo const&)> f_num = &Foo::num_;
        std::cout << "num_: " << f_num(foo) << '\n';

        // store a call to a member function and object
        using std::placeholders::_1;
        std::function<void(int)> f_add_display2 = std::bind( &Foo::print_add, foo, _1 );
        f_add_display2(2);

        // store a call to a member function and object ptr
        std::function<void(int)> f_add_display3 = std::bind( &Foo::print_add, &foo, _1 );
        f_add_display3(3);

        // store a call to a function object
        std::function<void(int)> f_display_obj = PrintNum();
        f_display_obj(18);
    }
    ```

### nice std::function 
pass a lambda block `[variable](){}` or `std::bind(&class::fun, this)` to std::function<void()>  
  ```c++
  // a helper class to turn the `TaskInfoGen` api into a std::function based one
    class FnTask final : public TaskExcuserGen {
    public:
        FnTask(std::function<void()> run_me): m_fn {std::move(run_me)} {
        }
        virtual void excuse(const std::shared_ptr<TaskInfoGen> & info) override{
            m_fn();
        }
    private:
        std::function<void()> m_fn;
    };
    
    static std::shared_ptr<TimerGen> create(int64_t interval, int32_t repeat_times, 
      const std::shared_ptr<TaskExcuserGen> & hander);
      
    bool LapseSettingDlgImp::onFpsChange(int32_t fps) {
      m_fps_change_timer = nullptr;

      int32_t min_fps = DataGen::instance()->getMinFps();
      int32_t max_fps = DataGen::instance()->getMaxFps();
      if (fps < min_fps || fps > max_fps){
          const std::weak_ptr<LapseSettingDlgImp> weak_self = shared_from_this();
          const std::weak_ptr<LapseSettingDlgDelegate> week_delegate = this->m_delegate;
          int32_t delay = m_saving ? -1 : 500;
          m_fps_change_timer = TimerGen::create(delay, 0, std::make_shared<FnTask>(
         [weak_self, week_delegate, min_fps, max_fps](){

             const std::shared_ptr<LapseSettingDlgDelegate> delegate = week_delegate.lock();
             CHECK_RT(delegate!=nullptr, "delegate null");
             int32_t new_fps = delegate->getFps();
             // ....
         }));
          m_fps_change_timer->start();
          return false;
      }

      return true;
    }

  ```


