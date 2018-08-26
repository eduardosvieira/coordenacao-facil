
var PROTOCOL = window.location.protocol;
var HOSTNAME = window.location.hostname;
var PORT = window.location.port;

var URL = PROTOCOL + "//" + HOSTNAME + ":" + PORT;

$(document).ready(function(){
  $('.sidenav').sidenav();

  $('.tabs').tabs();

  $('.modal').modal();

  $('select').formSelect();

  $('.fixed-action-btn').floatingActionButton();

  $("#btnCreateCoordinator").on("click", function(event){
    var name = $("#coordinator-name").val();
    var code = $("#coordinator-code").val();
    var course = $("#coordinator-course").val();

    $.ajax({
      url: URL + "/app/coordinators/",
      type: "POST",
      data: {"name": name, "code": code, "course": course}
    });
  });
});
