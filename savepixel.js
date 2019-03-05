


function myFunction() {
	   // your code here
  pixelbutton=document.createElement("button")
pixelbutton.textContent="Add tracker"
pixelbutton.onclick = function() {  var x = document.getElementsByClassName("gmail_signature")[0];
var img = document.createElement("img");
var emaillist = document.getElementsByClassName("vT")[0].textContent
img.src="" +   Math.floor(100000 + Math.random() * 90000000000).toString() + "&email=" + emaillist.toString() + "&subject="+document.getElementsByClassName("aYF")[0].textContent.toString()
img.hidden="True"
x.appendChild(img);
}
document.getElementsByClassName("bAK")[0].appendChild(pixelbutton);
console.log("SENT")
}

chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    // listen for messages sent from background.js
    if (request.message === 'hello!' ) {

    	if (request.url.search("compose=new") > -1) {
    		if (request.url.search("mail") > -1) {
    			      myFunction();// 
    			  }
    	else if (request.url.search("#inbox/") > -1) {

    		myFunction();
    		}
    	}
    	}
    
});
