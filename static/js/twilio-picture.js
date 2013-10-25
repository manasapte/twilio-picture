$(document).ready(function() {
  $('#closemodal').click(function(){
    $('#myModal').modal('hide'); 
  });
  $('#myModal').modal();
  $('#error-name, #error-phone').hide();
  $("#tetris-play").click(
    if($('#twipic-name').val().trim() == '') {
      $('#error-name).show();
      return;
    } 
    $('#myModal').modal('hide');
  );
  
});


