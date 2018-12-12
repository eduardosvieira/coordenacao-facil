
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

  $("#btnCreateCourse").on("click", function(event){
    var name = $("#course-name").val();
    var code = $("#course-code").val();
    var coordinator = $("#coordinator").val();
    var university = $("#university").val();
    var createdAt = $("#createdAt").val();

    $.ajax({
      url: URL + "/app/courses/",
      type: "POST",
      data: {"name": name, "code": code, "coordinator": coordinator, "university": university, "createdAt": createdAt},
      success: function(data) {
        console.log("Ol");
        window.location.replace(URL + "/app/administrator/");
      },
      error: function(data) {
        alert("Houve um problema ao criar uma nova universidade.");
        window.location.replace(URL + "/app/administrator/");
      }
    });
  });
});
