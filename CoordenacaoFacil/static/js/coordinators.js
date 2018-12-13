
var PROTOCOL = window.location.protocol;
var HOSTNAME = window.location.hostname;
var PORT = window.location.port;

var URL = PROTOCOL + "//" + HOSTNAME + ":" + PORT;

function btnSendToTeacher(id) {
  $("#uoa-code").val(id);
}

function loadTeachers() {
  $.ajax({
      url: URL + "/app/teachers/",
      type: "GET",
      success: function(data) {
        var teacher = $("#teacher");
        teacher.empty();

        for(index in data) {
          teacher.append($("<option />").text(data[index]["name"]).attr("value", data[index]["code"]));
        }
        $('select').formSelect();
      },
      error: function() {
        console.log("Houve um problema obter Professores.");
      }
    });
}

function loadCourses() {
  $.ajax({
      url: URL + "/app/courses/",
      type: "GET",
      success: function(data) {
        var course = $("#coordinator-course");
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

function loadUniversitiesC() {
  $.ajax({
      url: URL + "/app/universities/",
      type: "GET",
      success: function(data) {
        var university = $("#coordinator-university");
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
  $('.tabs').tabs();

  $('.modal').modal();

  $('.fixed-action-btn').floatingActionButton();

  $('.sidenav').sidenav();

  $('select').formSelect();

  $("#coordinator-createdAt").val(new Date());

  loadTeachers();
  loadCourses();
  loadUniversitiesC();


  $("#btnCreateCoordinator").on("click", function(event){
    var name = $("#coordinator-name").val();
    var code = $("#coordinator-code").val();
    var email = $("#coordinator-email").val();
    var university = $("#coordinator-university").val();
    var course = $("#coordinator-course").val();
    var password = $("#coordinator-password").val();
    var createdAt = $("#coordinator-createdAt").val();

    $.ajax({
      url: URL + "/app/coordinators/",
      type: "POST",
      data: {"name": name, "email": email, "code": code, "university": university, "course": course, "password": password, "createdAt": createdAt},
      success: function(data) {
        window.location.replace(URL + "/app/administrator/");
      },
      error: function(data) {
        alert("Houve um problema ao criar novo coordenador.");
        window.location.replace(URL + "/app/administrator/");
      }
    });
  });
});
