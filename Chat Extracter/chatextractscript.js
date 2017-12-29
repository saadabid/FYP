var fs = require('fs');

// Create a new instance of a Workbook class
// var workbook = new excel.Workbook();

// // Add Worksheets to the workbook
// var worksheet = workbook.addWorksheet('Sheet 1');
// worksheet.cell(1,1).string("userqueries");
// worksheet.cell(1,2).string("Awnser");

fs.readFile('read3.txt','utf8',function(err,data){
  //console.log(data);
  var jsondata = JSON.parse(data);
  var len1 = jsondata.conversations.data.length;
  var len2 = jsondata.conversations.data[0].messages.data.length;
  var k=1;
  console.log(len1);

  //console.log(jsondata.conversations.data[0].messages.data[0].message);
  for(var i = 0 ; i < len1 ; i++)
  {
      var len2 = jsondata.conversations.data[i].messages.data.length;
    for(var j = 0 ; j < len2 ; j++)
    {
      var msg = jsondata.conversations.data[i].messages.data[j].message;
      fs.appendFile('chat3.txt',msg + '\n');
    // var name = jsondata.conversations.data[i].messages.data[j].from.name;
    // if(name == 'Go Shop')
    // {
    //   var msg1 = jsondata.conversations.data[i].messages.data[j].message;
    //   // worksheet.cell(k,2).string('saad');
    //   // k++;
    //  fs.appendFile('awnser.txt',msg1 + '\n');
    //   console.log(msg1+'\n');
    // }else {
    //   var msg = jsondata.conversations.data[i].messages.data[j].message;
    //   // worksheet.cell(k,1).string(msg);
    //   // k++;
    //  fs.appendFile('userqueries.txt',msg + '\n');
    //   console.log(msg+'\n');
    // }

  }
}
});

