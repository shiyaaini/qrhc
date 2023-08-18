console.show();
var w = floaty.rawWindow(<frame gravity='center' bg='#44ffcc00' />);

w.setSize(1000, 1000);
w.setPosition(500,1000);
sleep(2000);
console.log(w.getWidth());
setTimeout(() => {
  w.close();
}, 5000);
sleep(100000);
