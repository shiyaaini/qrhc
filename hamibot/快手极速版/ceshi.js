// 显示控制台
console.show();
// 启用按键监听
events.observeKey();

// 初始化计数器
var counter = 0;

// 监听音量上键按下

events.onKeyDown("volume_up", function(event) {
    console.log('音量上键被按下了，脚本将停止。');
    toast('音量上键被按下了，脚本将停止。');
    sleep(1000);
    console.hide();
    exit();
    });



// console.log('计数器已达到 1000，脚本将退出。');


