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
        if(data.length > 0){html += '<input type="submit" value="Select Ad">';}

        $("div.div-search-content").html(html);
      }
    });

    e.preventDefault();
    
  });
  
  time = [];
  duration = [];
  i=0;

  $("#reas").keydown(function(){

    try{
      time.push($.now());
      duration.push(time[time.length - 1] - time[time.length - 2]);
      console.log(time);
      console.log(duration);
    }catch{
      
    }
  }).keyup(function(){

    if(duration[i] > 300){
      //make the request to get the comment and translate it
      //ao fazer a requisicao zerar as pilhas e o i
      time = [];
      duration = [];
      i=0;
      alert("working");
    }else{
      i++;
    }
  });

  $("#expl").keydown(function(){
    alert("test");
  });

  $("#add").keydown(function(){
    
  });
  
});
