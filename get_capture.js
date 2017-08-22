function waitFor(testFx, onReady, timeOutMillis) {
    var _x = 86;
    var maxtimeOutMillis = timeOutMillis ? timeOutMillis : 2000, //< Default Max Timout is 3s
    
        start = new Date().getTime(),
        condition = false,
        interval = setInterval(function() {
            if ( (new Date().getTime() - start < maxtimeOutMillis) && !condition ) {
                // If not time-out yet and condition not yet fulfilled
                condition = (typeof(testFx) === "string" ? eval(testFx) : testFx()); //< defensive code
            } else {
                if(!condition) {
                    // If condition still not fulfilled (timeout but condition is 'false')
                    console.log("init ok");
                    
                    page.evaluate(function() {
                        document.getElementById('popup-submit').click();
                        
                    });
                    
                    clearInterval(interval);
                    start2 = new Date().getTime(),
                    condition = false,
                    interval2 = setInterval(function() {
                    if ( (new Date().getTime() - start2 < maxtimeOutMillis)  ) {
                        console.log('.');
                        
                    }else{
                        clearInterval(interval2);
                        page.render('aa.png');
                        
                        page.evaluate(function() {
                            var mouseMoveArr = [[122,30],[122,30],[122,30],[122,30],[122,30],[122,30],[122,30],[122,30],[122,30],[122,30]];  
                            var createEvent = function(eventName, ofsx, ofsy) {var ev = document.createEvent('MouseEvents');
                            ev.initMouseEvent(eventName, true, false, null, 0, 0, 0, ofsx, ofsy, false, false, false, false, 0, null); return ev;};
                            //createEvent("click",200,500); 
                            var _auto_down = createEvent("mousedown",86,876);  
                            var _obj = document.querySelectorAll(".gt_slider_knob");
                            _obj = _obj[1];
                            _obj.dispatchEvent(_auto_down);  
                            
                              
                        });
                        //等出现拼图
                        waitStart = new Date().getTime();
                        intervalWait = setInterval(function(){  
                        if(new Date().getTime() - waitStart > 1000){
                            clearInterval(intervalWait);
                            
                            page.render('bb.png');
                            
                            //获取位移量
                            var input = ''; var sys = require('system');
                            console.log('input:');
                            input = sys.stdin.readLine();
                            console.log(input);
                            var moveInt = parseInt(input);
                            
                            var startX = 86;
                            console.log('distance:',moveInt);
                            var distance = moveInt - 80;
                            function getX(index){
                               var temp = 0;
                               if (index < 7){
                                   temp = 80 + 1.169 * index * distance/10 - (index/10) * (index/10) * 17;
                                   
                               }else{
                                   temp = 80 + distance * index / 10 + (1.169 * index * distance/10 - (index/10) * (index/10) * 17 - distance * index / 10) * (index / 10);
                               }
                               return temp; 
                            };
                            console.log(getX(0),getX(1),getX(2),getX(3),getX(4),getX(5),getX(6),getX(7),getX(8),getX(9));
                            
                            page.evaluate(function(input) {
                                var startX = 86;
                                var distance = input - 80;
                                function getX(index){
                                   var temp = 0;
                                   if (index < 7){
                                       temp = 1.169 * index * distance / 10 - (index/10) * (index/10) * 17;
                                       
                                   }else{
                                       temp = distance * index / 10 + (1.169 * index * distance - (index/10) * (index/10) * 17 - distance * index / 10) * (index / 10);
                                   }
                                   return temp; 
                                };
                                
                                
                                var mouseMoveArr = [[getX(0),876],[getX(1),876],[getX(2),876],[getX(3),876],[getX(4),876],[getX(5),876],[getX(6),876],[getX(7),876],[getX(8),876],[input,876]];  
                                var createEvent = function(eventName, ofsx, ofsy) {var ev = document.createEvent('MouseEvents');
                                ev.initMouseEvent(eventName, true, false, null, 0, 0, 0, ofsx, ofsy, false, false, false, false, 0, null); return ev;};
                                //createEvent("click",200,500); 
                                var _auto_down = createEvent("mousedown",86,876);  
                                
                                //var _obj = document.getElementById("popup-submit");  
                                var _obj = document.querySelectorAll(".gt_slider_knob");
                                _obj = _obj[1];
                                //_obj.dispatchEvent(_auto_down);  
                                
                                MoveStart = new Date().getTime();
                                var moveIndex = 0;
                                IntervalMove = setInterval(function(){  
                                //var moveIndex = Math.round(Math.random() * (mouseMoveArr.length - 1));  
                                
                                _obj.dispatchEvent(createEvent("mousemove",mouseMoveArr[moveIndex][0],mouseMoveArr[moveIndex][1]));  
                                moveIndex = moveIndex + 1;
                                if (moveIndex >= mouseMoveArr.length - 1){
                                    moveIndex = mouseMoveArr.length - 1;
                                }
                                    
                                
                                if(new Date().getTime() - MoveStart > 1256){
                                    clearInterval(IntervalMove);
                                    _obj.dispatchEvent(createEvent("mouseup",mouseMoveArr[9][0],mouseMoveArr[9][1]));  
                                }
                                },100);  
                            
                            
                        },moveInt+78);
                        
                      
                        start3 = new Date().getTime(),
                        interval3 = setInterval(function() {
                        if ( (new Date().getTime() - start3 < 3000) ) {
                            console.log('%d',_x);
                            _x = _x + 1;
                            if(_x == 87){
                                page.render('00.png');
                            }
                            if(_x == 88){
                                page.render('01.png');
                            }
                            if(_x == 90){
                                page.render('02.png');
                            }
                            if(_x == 92){
                                page.render('03.png');
                            }
                            
                            //page.sendEvent("mousemove",_x,876);
                        }else{
                            clearInterval(interval3);
                            page.render('dd.png');
                            phantom.exit();
                        }
                        
                        },250);
                            
                        }else{
                            console.log('d')
                        }
                        
                        },100);  
                        //_obj.dispatchEvent(createEvent("mousemove",150,876));
                        
                        
                        
                    }
                    },250);
                    
                } else {
                    // Condition fulfilled (timeout and/or condition is 'true')
                    console.log("'waitFor()' finished in " + (new Date().getTime() - start) + "ms.");
                    typeof(onReady) === "string" ? eval(onReady) : onReady(); //< Do what it's supposed to do once the condition is fulfilled
                    clearInterval(interval); //< Stop this interval
                }
            }
        }, 250); //< repeat check every 250ms
};


var page = require('webpage').create();
page.settings.userAgent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36';
page.open('http://127.0.0.1:5000/', function(status) {
  console.log("Status: " + status);
  if(status == "success") {
    waitFor(function check() { return page.evaluate(function () { return (document.querySelectorAll('.gt_cut_bg_slice').length >= 50) && (document.querySelectorAll('.gt_cut_fullbg_slice').length <= 50);//确保页面已经渲染完成，出现了背景图
    });
        }, function() {
           console.log("The x should be visible now.");
           page.evaluate(function() {document.getElementById('popup-submit').click();});
           
           waitFor(1,1==1);
           console.log("clicked");
           page.render('example2.png');
           phantom.exit();
        });
    
  }
});




