console.show(); //启动控制台
var h=app.getPackageName("起点读书");   //通过软件名获取应用包名
console.log(h);
app.uninstall(h);   //删除应用
while (!click('确定')); 		//等待按钮被点击，然后终止程序