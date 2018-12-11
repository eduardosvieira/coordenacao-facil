
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

  $('select').formSelect();

  $("#createdAt").val(new Date());

  /*Carregando universidades*/
  loadUniversities();

  /*Carregando coordenadores*/
  loadCoordinators();

});
