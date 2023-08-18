console.show()
console.log('启动开始极速版');
app.launchApp('快手极速版');
sleep(5000);

// while(!click('去赚钱'));
setScreenMetrics(1600, 2500);
// click(1138, 2474);

// for(var i=0;i<20;i++){
//     console.log('观看第'+i+'视频');
//     swipe(1200, 2300, 1200, 200, 500);
//     sleep(8000);
// }
// 去赚钱 
function money(){
    sleep(2000);
    console.log('点击去赚钱');
    var money=text("去赚钱").fineOne();
    money.click();
    sleep(2000);
    ad();

}
function ad(){
    sleep(2000);
    var clickad =className("android.widget.TextView").text("看视频得5000金币").fineOne().scrollForward();
    clickad.click();
}
money();

                     
console.hide();