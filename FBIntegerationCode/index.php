<?php

// parameters
$hubVerifyToken = 'TOKEN1234GGGSS';
$accessToken = "EAAQ8poRtX3QBADlLXhsd3PZAZADGmDXdZAZAa5EPt41u83ZBHWoITmJ3nqpfLGSGJFQVJA3gE5TfEvkiNfSM9ZCVVqZBq85PtZC1WQHa0aheGQDs4JdKnwaYC8M4eVB1TI5XWsKQH6juioZC1Yreoj5sVcUUwgEboeg1yjbHnLRw1iAZDZD";

// check token at setup
if ($_REQUEST['hub_verify_token'] === $hubVerifyToken) {
  echo $_REQUEST['hub_challenge'];
  exit;
}

// handle bot's anwser
$input = json_decode(file_get_contents('php://input'), true);

$senderId = $input['entry'][0]['messaging'][0]['sender']['id'];
$messageText = $input['entry'][0]['messaging'][0]['message']['text'];
$messageText = strtolower($messageText);
$query = str_replace(' ', '-', $messageText);
$fbapi=curl_init();
curl_setopt($fbapi,CURLOPT_URL,'http://139.162.7.166:8000/users/'.$query);
curl_setopt($fbapi,CURLOPT_RETURNTRANSFER,1);
$answer=curl_exec($fbapi);
echo $answer;
list($intent ,$fbreply, $g) = explode('|', $answer);
curl_close($fbapi);

$pcode = array("gsw-501");
$answer = "I don't understand.";
$code = "";
$i = 0;
$connn = OpenCon();
      $sql = "SELECT product_code FROM products";
      $resultt = $connn->query($sql);
      if ($resultt->num_rows > 0) {
         while($roww = $resultt->fetch_assoc()) {
            $pcode[$i] = $roww["product_code"];
			$i++;
		 }
        } else {
               echo "0 results";
        }
		 $connn->close();
if($messageText == "hi"){

		$fbreply = "Hi, Welcome To GO SHOP! How Can I Help You ?";

	 $response = [
    'recipient' => [ 'id' => $senderId ],
    'message' => [ 'text' => $fbreply ]
];
}else if($intent == "['Price']")
{  
    
    for ($x = 0; $x <= 2; $x++) {
    if (strpos($messageText, $pcode[$x]) !== false) {
        $code = $pcode[$x];
    }
    } 
    $deliverycharges = 150;
    if (strpos($messageText, $code) !== false) {
      $conn = OpenCon();
      $sql = "SELECT product_price FROM products WHERE product_code= '".$code."'";
      $result = $conn->query($sql);
      if ($result->num_rows > 0) {
         while($row = $result->fetch_assoc()) {
            $price = $row["product_price"];
         }
        } else {
               echo "0 results";
        }
        $total = $price + $deliverycharges;
        $fbreply = "Price of " .$code." is Rs ".$price. "+ delivery charges Rs ".$deliverycharges.".Total Rs ".$total;
      $conn->close();
    }else
    {
        $fbreply = "Please mention correct product code";  
    }
     $response = [
    'recipient' => [ 'id' => $senderId ],
    'message' => [ 'text' => $fbreply ]
];
}else if($intent == "['Availability']"){
	for ($x = 0; $x <= 2; $x++) {
    if (strpos($messageText, $pcode[$x]) !== false) {
        $code = $pcode[$x];
		$code = 1;
    }
    }
	if($code)
	{
		$fbreply = "This product is available";
	}else
	{
		$fbreply = "This product is not available,We will inform you when product will back in our stock";	
	}
	 $response = [
    'recipient' => [ 'id' => $senderId ],
    'message' => [ 'text' => $fbreply ]
];
}else if($intent == "['Contact']"){

  $answer = ["attachment"=>[

      "type"=>"template",

      "payload"=>[

        "template_type"=>"button",

        "text"=>"FOR CONTACT US : +923-218-769-321 /n We dont have any outlet ,We are dealing online and deliver our products all over in Pakistan",

        "buttons"=>[

          [

            "type"=>"web_url",

            "url"=>"https://petersapparel.parseapp.com",

            "title"=>"Show Website"

          ],

          [

            "type"=>"postback",

            "title"=>"Whatsapp Calling",

            "payload"=>"USER_DEFINED_PAYLOAD"

          ]

        ]

      ]

      ]];

      $response = [

    'recipient' => [ 'id' => $senderId ],

    'message' => $answer

];
}else 
{
     $response = [
    'recipient' => [ 'id' => $senderId ],
    'message' => [ 'text' => $fbreply ]
];
}




if($messageText == "blog"){

     $answer = ["attachment"=>[

      "type"=>"template",

      "payload"=>[

        "template_type"=>"generic",

        "elements"=>[

          [

            "title"=>"Welcome to Peter\'s Hats",

            "item_url"=>"https://www.cloudways.com/blog/migrate-symfony-from-cpanel-to-cloud-hosting/",

            "image_url"=>"https://www.cloudways.com/blog/wp-content/uploads/Migrating-Your-Symfony-Website-To-Cloudways-Banner.jpg",

            "subtitle"=>"We\'ve got the right hat for everyone.",

            "buttons"=>[

              [

                "type"=>"web_url",

                "url"=>"https://",

                "title"=>"Our Website"

              ],

              [

                "type"=>"postback",

                "title"=>"Start Chatting",

                "payload"=>"DEVELOPER_DEFINED_PAYLOAD"

              ]              

            ]

          ]

        ]

      ]

    ]];

     $response = [

    'recipient' => [ 'id' => $senderId ],

    'message' => $answer 

];}



$ch = curl_init('https://graph.facebook.com/v2.6/me/messages?access_token='.$accessToken);
//$apibot = curl_init('Authorization: Bearer 1324389900ac4fc98d9763b7dc6aa525 ////https://api.api.ai/v1/query?v=20150910&query=weather&timezone=Europe/Paris&lang=en&contexts=weather&contexts=europe&latitude=37.459157&longitude=-122.17926&sessionId=1234567890');

curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($response));
curl_setopt($ch, CURLOPT_HTTPHEADER, ['Content-Type: application/json']);
curl_exec($ch);
curl_close($ch);
//curl_setopt($apibot, CURLOPT_POST, 1);
//curl_setopt($apibot, CURLOPT_POSTFIELDS, json_encode($response));
//curl_setopt($apibot, CURLOPT_HTTPHEADER, ['Content-Type: application/json']);
//$res = curl_exec($apibot);
//echo $res;
//curl_close($apibot);


function OpenCon()
 {
 $dbhost = "localhost";
 $dbuser = "id736683_saadabid15";
 $dbpass = "saarim123";
 $db = "id736683_chatbot";


 $conn = new mysqli($dbhost, $dbuser, $dbpass,$db) or die("Connect failed: %s\n". $conn -> error);

 
 return $conn;
 }
 
function CloseCon($conn)
 {
 $conn -> close();
 }
 

?>