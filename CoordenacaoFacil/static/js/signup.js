
var PROTOCOL = window.location.protocol;
var HOSTNAME = window.location.hostname;
var PORT = window.location.port;

var URL = PROTOCOL + "//" + HOSTNAME + ":" + PORT;

function loadCourses() {
  $.ajax({
      url: URL + "/app/courses/",
      type: "GET",
      success: function(data) {
        var course = $("#course");
        course.empty();

        for(index in data) {
          course.append($("<option />").text(data[index]["name"]).attr("value", data[index]["code"]));
        }
        $('select').formSelect();
      },
      error: function() {
        console.log("Houve um problema obter cursos.");
      }
    });
}


$(document).ready(function(){
  $('.sidenav').sidenav();

  $('select').formSelect();

  $("#createdAt").val(new Date());

  loadCourses();

});
