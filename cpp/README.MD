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


