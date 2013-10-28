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
    $('#myModal').modal('hide');
  });
  
});


