$(function(){

  $("#form_search_ads").submit(function(e){

    $.ajax({

      url: "/ads/show_all",
      type: "GET",
      data: $(this).serialize(),
      timeout: 12000,
      dataType: "json",
      success: function(data){
        alert(JSON.stringify(data));
      }
    });

    e.preventDefault();
    
  });
});
