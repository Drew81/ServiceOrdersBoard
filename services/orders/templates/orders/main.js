var today = new Date();
var hourNow = today.getHours();
var greeting;
var user = document.getElementById("greeting").innerHTML = '<p>{{ user }}</p>';

if (hourNow > 18) {
  greeting = 'Good evening';
} else if ( hourNow > 12) {
  greeting = 'Good Afternoon';
} else if (hourNow > 0 ) {
  greeting = 'Good morning!';
} else {
  greeting = 'Welcome!';
}

document.write('<h3>' + greeting + '</h3>');


