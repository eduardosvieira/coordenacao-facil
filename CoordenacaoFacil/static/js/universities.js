
var PROTOCOL = window.location.protocol;
var HOSTNAME = window.location.hostname;
var PORT = window.location.port;

var URL = PROTOCOL + "//" + HOSTNAME + ":" + PORT;

$(document).ready(function(){
  $('.sidenav').sidenav();

  $('.tabs').tabs();

  $('.modal').modal();

  $('select').formSelect();

  $("#btnCreateUniversity").on("click", function(event){
    var name = $("#university-name").val();
    var code = $("#university-code").val();

    $.ajax({
      url: URL + "/app/universities/",
      type: "POST",
      data: {"name": name, "code": code}
    });
  });
});
