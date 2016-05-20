android tip
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
