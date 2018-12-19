
var PROTOCOL = window.location.protocol;
var HOSTNAME = window.location.hostname;
var PORT = window.location.port;

var URL = PROTOCOL + "//" + HOSTNAME + ":" + PORT;

function deleteUOA(id) {
  $.ajax({
    url: URL + "/app/useOfAbstracts/" + id + "/",
    type: "DELETE",
    success: function(data) {
      window.location.replace(URL + "/app/");
    },
    error: function(data) {
      alert("Houve um problema ao tentar remover UOA.");
    }
  });
}

function loadAbstracts() {
  $.ajax({
      url: URL + "/app/abstracts/",
      type: "GET",
      success: function(data) {
        var origin = $("#uoa-origin");
        var destiny = $("#uoa-destiny");

        origin.empty();
        destiny.empty();

        for(index in data) {
          origin.append($("<option />").text(data[index]["name"]).attr("value", data[index]["code"]));
          destiny.append($("<option />").text(data[index]["name"]).attr("value", data[index]["code"]));

        }
        $('select').formSelect();
      },
      error: function() {
        console.log("Houve um problema obter cadeiras.");
      }
    });
}

$(document).ready(function(){
  $('.sidenav').sidenav();

  $('select').formSelect();

  $('.modal').modal();

  $('.fixed-action-btn').floatingActionButton();

  $("#uoa-createdAt").val(new Date());

  loadAbstracts();

  $("#btnCreateUOA").click(function(event) {
    var origin = $("#uoa-origin").val();
    var destiny = $("#uoa-destiny").val();

    var menu = $('#uoa-menu').prop('files');

    var createdAt = $("#uoa-createdAt").val();

    $.ajax({
      url : URL + "/app/useOfAbstracts/",
      type : "POST",
      data : {"origin": origin, "destiny": destiny, "menu": menu, "createdAt": createdAt},
      processData: false,  // tell jQuery not to process the data
      contentType: false,  // tell jQuery not to set contentType
      success : function(data) {
        console.log(data);
      }
    });

  });

});
