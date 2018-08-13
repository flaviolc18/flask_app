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

  $("#reas, #expl, #add").keypress(function(){

    try{
      time.push($.now());
      duration.push(time[time.length - 1] - time[time.length - 2]);
    }catch{
      
    }

    if(duration[i] > 300){
      
      time = [];
      duration = [];
      i=0;

      attCommField();
      translate();

    }else{
      i++;
    }
  }).focusout(function(){

    attCommField();
    translate();
  });

});

function attCommField(){
  $("#comm").val($("#reas").val() +" "+ $("#expl").val() +" "+ $("#add").val());
}

function translate(){
  $.ajax({
    url: "https://translate.yandex.net/api/v1.5/tr.json/translate",
    type: "POST",
    data: {
      "key":"trnsl.1.1.20180811T235235Z.208a03afda2184fc.78e1084fc806716fcd4018dac14ee49532074e2e",
      "text": $("#comm").val(),
      "lang": "en-pt",
      "format":"plain"
    },
    timeout: 12000,
    dataType: "json",
    success: function(data){
      $("#trans").val(data['text']);
    }
  });
}


