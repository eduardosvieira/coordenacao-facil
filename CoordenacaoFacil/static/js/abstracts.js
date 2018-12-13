
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

  $("#abstract-createdAt").val(new Date());

  $("#btnCreateAbstract").on("click", function(event){
    var name = $("#abstract-name").val();
    var code = $("#abstract-code").val();
    var createdAt = $("#abstract-createdAt").val();

    $.ajax({
      url: URL + "/app/abstracts/",
      type: "POST",
      data: {"name": name, "code": code, "createdAt": createdAt}
    });
  });
});
