
var PROTOCOL = window.location.protocol;
var HOSTNAME = window.location.hostname;
var PORT = window.location.port;

var URL = PROTOCOL + "//" + HOSTNAME + ":" + PORT;

$(document).ready(function(){
  $('.sidenav').sidenav();

  $('select').formSelect();

  $('.modal').modal();

  $('.fixed-action-btn').floatingActionButton();

  $("#createdAt").val(new Date());

});
