
var PROTOCOL = window.location.protocol;
var HOSTNAME = window.location.hostname;
var PORT = window.location.port;

var URL = PROTOCOL + "//" + HOSTNAME + ":" + PORT;

function loadUniversities() {
  $.ajax({
      url: URL + "/app/universities/",
      type: "GET",
      success: function(data) {
        var university = $("#university");
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

function loadCoordinators() {
  $.ajax({
      url: URL + "/app/coordinators/",
      type: "GET",
      success: function(data) {
        var coordinator = $("#coordinator");
        coordinator.empty();

        for(index in data) {
          coordinator.append($("<option />").text(data[index]["name"]).attr("value", data[index]["code"]));
        }
        $('select').formSelect();
      },
      error: function() {
        console.log("Houve um problema obter coordenadores.");
      }
    });
}

$(document).ready(function(){
  $('.sidenav').sidenav();

  $('.tabs').tabs();

  $('.modal').modal();

  $('select').formSelect();

  $('.fixed-action-btn').floatingActionButton();

  /*Carregando universidades*/
  loadUniversities();

  /*Carregando coordenadores*/
  loadCoordinators();

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
        window.location.replace(URL + "/app/administrator/");
      },
      error: function(data) {
        alert("Houve um problema ao criar uma nova universidade.");
        window.location.replace(URL + "/app/administrator/");
      }
    });
  });
});
