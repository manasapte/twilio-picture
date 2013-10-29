$(document).ready(function() {
  $('#closemodal').click(function(){
    $('#myModal').modal('hide'); 
  });
  $('#myModal').modal();
  $('#error-name, #error-phone').hide();
  $("#twipic-play").click(function(){
    console.log('here');
    if($('#twipic-name').val().trim() == ''){
      $('#error-name').show();
      return;
    }
    //$.post( "/text", {name:$('#twipic-name').val(),phone:$('#twipic-phone').val()},function( data ) {
    $.post( "/text", {name:'stuff'},function( data ) {
      $('#myModal').modal('hide');
      console.log("data after success: "+data);
    });
  });
  
});


