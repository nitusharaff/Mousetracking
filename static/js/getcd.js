

 function coord()
{
id= document.getElementsByTagName("html")[0].id
type=document.getElementsByTagName("body")[0].id

var rectques = document.getElementById("ques").getBoundingClientRect();
var ques = [rectques.left, rectques.top, rectques.right, rectques.bottom];
var rectsubmit = document.getElementById("submit").getBoundingClientRect();
var sub = [rectsubmit.left, rectsubmit.top, rectsubmit.right, rectsubmit.bottom];

if(type=="text-rating")
  {
   var rectrate=document.getElementById("range").getBoundingClientRect();
   var rate = [rectrate.left, rectrate.top, rectrate.right, rectrate.bottom];
   var recttext=document.getElementById("textInput").getBoundingClientRect();
   var text = [recttext.left, recttext.top, recttext.right, recttext.bottom];
  }

else
{

var rectyes = document.getElementById("yes").getBoundingClientRect();
var yes = [rectyes.left, rectyes.top, rectyes.right, rectyes.bottom];
var rectno = document.getElementById("no").getBoundingClientRect();
var no = [rectno.left, rectno.top, rectno.right, rectno.bottom];
var rectmaybe = document.getElementById("maybe").getBoundingClientRect();
var maybe = [rectmaybe.left, rectmaybe.top, rectmaybe.right, rectmaybe.bottom];
if(type=="audio")
{

   var rectaudio=document.getElementById("aud").getBoundingClientRect();
var audio = [rectaudio.left, rectaudio.top, rectaudio.right, rectaudio.bottom];
var auddur= document.getElementById("aud").duration
  }

else if(type=="image")
{

      var rectimage=document.getElementById("imagefile").getBoundingClientRect();
var image = [rectimage.left, rectimage.top, rectimage.right, rectimage.bottom];





  }

else if(type=="video")
{
   var rectvideo=document.getElementById("videofile").getBoundingClientRect();
var video = [rectvideo.left, rectvideo.top, rectvideo.right, rectvideo.bottom];
var viddur= document.getElementById("videofile").duration
  }


}





ques= JSON.stringify(ques)
    sub= JSON.stringify(sub)

    if(yes==undefined)
    {
        yes="none"
    }
    else {
        yes = JSON.stringify(yes)
    }

    if(no==undefined)
    {
        no="none"
    }
    else {
        no = JSON.stringify(no)
    }
    if(maybe==undefined)
    {
        maybe="none"
    }
    else {
        maybe = JSON.stringify(maybe)
    }

    if(rate==undefined)
    {
        rate="none"
    }
    else {
        rate = JSON.stringify(rate)
    }if(text==undefined)
    {
        text="none"
    }
    else {
        text = JSON.stringify(text)
    }

    if(audio==undefined)
    {
        audio="none"
        auddur="none"
    }
    else {
        audio = JSON.stringify(audio)
     auddur=auddur.toString()
    }
    if(video==undefined)
    {
        video="none"
        viddur="none"
    }
    else {
        video = JSON.stringify(video)
        viddur=viddur.toString()


}
    if(image==undefined)
    {
        image="none"
    }
    else {
        image = JSON.stringify(image)
    }





  $.post("/coord",
    {   id:id,
        type:type,
        ques:ques,
        yes:yes,
        no:no,
        maybe:maybe,
        rate:rate,
        text:text,
        audio:audio,
        viddur:viddur,
        auddur:auddur,
        video:video,
        image:image,
        sub:sub

    },
    function(data, status){
        console.log("Data: " + data + "\nStatus: " + status);
    });




}
