function doPost(e){
  var estringa = JSON.parse(e.postData.contents);
  var payload = identificar(estringa);
  var data = {
    "method": "post",
    "payload": payload
  }
  /* 這段會用可以解開註解
  var d = new Date();
  var SpreadSheet = SpreadsheetApp.openById("1n6iAtxDLhT_ILzpez6vQ4U0l8w9IRXrUAYS6ZPOgaMM");
  var Sheet = SpreadSheet.getSheetByName("紀錄收到的訊息");
  var LastRow = Sheet.getLastRow();
  Sheet.getRange(LastRow+1, 1).setValue(d);
  Sheet.getRange(LastRow+1, 2).setValue(estringa);
  //*/
  UrlFetchApp.fetch("https://api.telegram.org/bot6469891265:AAFKC2SjxPATJJAR1lswA9dFy34jgsNMrBI/", data);
}

function identificar(e){

    //var x=UrlFetchApp.fetch("http://fuyz92.natappfree.cc?proplem="+e.message.text);
    var url = 'http://124.70.102.7:3000'; // 目标API的URL
    var payload = e; // POST请求的参数，以JavaScript对象形式

    var options = {
      method: 'post', // 使用POST请求
      contentType: 'application/x-www-form-urlencoded', // 指定请求体的内容类型为JSON
      payload: JSON.stringify(payload) // 将参数对象转换为JSON字符串
    };

    var response = UrlFetchApp.fetch(url, options);
    var data = response.getContentText();
    Logger.log(data);
    mensaje = {
    "method": "sendMessage",
    "chat_id": String(e.message.chat.id),
    "text": data,
    }



  return mensaje
}