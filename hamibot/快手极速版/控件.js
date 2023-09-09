console.show()
console.log('hello');
sleep(1000);
var width=device.width
var height=device.height
setScreenMetrics(width, height);
toast('正在加载配置文件')
sleep(3000)
if(text('领权益').clickable(true).exists()){
    console.log('权益存在')
}
// s();
// // f();
// // me();
// function s(){
//     var k=text('首页').exists();
//     if(k){
//         console.log('首页存在');

//     }
//     click("首页");
//     sleep(3000);
//     swipe(1000, 2000, 1000, 300, 3000)
// }



// function f(){
//     click('放映厅');
//     sleep(3000);
// }
// function me(){
//     click('我');
//     sleep(3000);
// }




