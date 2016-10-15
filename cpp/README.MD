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

### std::bind

函数使用形式
bind(f [,t][,…])                                                 // 自动推断
bind<返回值类型>(f [,t][,…])                                       // 非自动推断
bind<返回值类型, 函数类型, 绑定器传入参数类型>(f ,[…])                 // 非自动推断
bind<返回值类型, 函数参数类型, 绑定器传入参数类型>(f [,…])              // 非自动推断
bind<返回值类型, 类, 绑定器传入参数类型（即对应的类实例）>(T::*f ,t [,…])// 非自动推断
bind<返回值类型, 类, 函数参数类型, 绑定器传入参数类型（即对应的类实例+函数传入的参数）, >(T::*f ,t [,…])  // 非自动推断
