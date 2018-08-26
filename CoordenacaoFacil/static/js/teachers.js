
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

  $("#btnCreateTeacher").on("click", function(event){
    var name = $("#teacher-name").val();
    var code = $("#teacher-code").val();
    var course = $("#teacher-course").val();

    $.ajax({
      url: URL + "/app/teachers/",
      type: "POST",
      data: {"name": name, "code": code, "course": course}
    });
  });
});
