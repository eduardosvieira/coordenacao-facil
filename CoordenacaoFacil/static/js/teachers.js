
var PROTOCOL = window.location.protocol;
var HOSTNAME = window.location.hostname;
var PORT = window.location.port;

var URL = PROTOCOL + "//" + HOSTNAME + ":" + PORT;

function loadCoursesT() {
  $.ajax({
      url: URL + "/app/courses/",
      type: "GET",
      success: function(data) {
        var course = $("#teacher-course");
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

function loadUniversitiesT() {
  $.ajax({
      url: URL + "/app/universities/",
      type: "GET",
      success: function(data) {
        var university = $("#teacher-university");
        university.empty();

        for(index in data) {
          university.append($("<option />").text(data[index]["name"]).attr("value", data[index]["code"]));
        }
        $('select').formSelect();
      },
      error: function() {
        console.log("Houve um problema obter universidades.");
      }
    });
}

$(document).ready(function(){
  $('.sidenav').sidenav();

  $('.tabs').tabs();

  $('.modal').modal();

  $('select').formSelect();

  $('.fixed-action-btn').floatingActionButton();

  loadCoursesT();
  loadUniversitiesT();

  $("#btnCreateTeacher").on("click", function(event){
    var name = $("#teacher-name").val();
    var code = $("#teacher-code").val();
    var email = $("#teacher-email").val();
    var university = $("#teacher-university").val();
    var course = $("#teacher-course").val();
    var password = $("#teacher-password").val();
    var createdAt = $("#teacher-createdAt").val();

    $.ajax({
      url: URL + "/app/teachers/",
      type: "POST",
      data: {"name": name, "email": email, "code": code, "university": university, "course": course, "password": password, "createdAt": createdAt},
      success: function(data) {
        window.location.replace(URL + "/app/coordinator/");
      },
      error: function(data) {
        alert("Houve um problema ao criar novo professor.");
      }
    });
  });
});
