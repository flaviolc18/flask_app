$(function(){

  $("#form_search_ads").submit(function(e){

    $.ajax({

      url: "/ads/show_all",
      type: "GET",
      data: $(this).serialize(),
      timeout: 12000,
      dataType: "json",
      success: function(data){
        html = "<table>";

        //for each add
        for(var i=0; i<data.length; i++){

          html += "<tr><td><input type='radio' name='ad_id' value='"+data[i].id+"'></td>";

            Object.keys(data[i]).forEach(function(key){

              if(typeof(data[i][key]) == "object"){
                Object.keys(data[i][key]).forEach(function(key2){

                  html += "<td>"+ key2 +":"+ data[i][key][key2] +"</td>";
                });
              }else{
                
                html += "<td>"+ key +":"+ data[i][key] +"</td>";
              }
            });

          html +="</tr>";
        }

        html += "</table>";

        $("div.div-search-content").html(html);
      }
    });

    e.preventDefault();
    
  });
});
