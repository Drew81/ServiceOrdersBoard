/*var today = new Date();
var hourNow = today.getHours();
var greeting;


if (hourNow > 18) {
  greeting = 'Good evening';
} else if (hourNow > 12) {
  greeting = 'Good Afternoon';
} else if (hourNow > 0 ) {
  greeting = 'Good morning!'
} else {
  greeting = 'Welcome!';
}

document.write('<h3>' + greeting + '</h3>');*/

var date = new Date();
var n = date.toDateString();
var time = date.toLocaleTimeString();

document.getElementById('time').innerHTML = n;



var x = 5;
var y = 353;
var a = x + y;


console.log(a);

$(document).ready(function(){
    $('.animated-icon1,.animated-icon3,.animated-icon4').click(function(){
        $(this).toggleClass('open');
    });
});
