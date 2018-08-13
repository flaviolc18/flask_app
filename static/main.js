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

  var timer;
  var interval = 400;

  $("#comp, #serv, #subj, #reas, #expl, #add").keydown(function(){

    clearTimeout(timer);

  }).keyup(function(){

    clearTimeout(timer);
    timer = setTimeout(attCommField, interval);
  }).focusout(function(){

    attCommField();
  });

  $('input[type=radio][name=over]').change(function() {
    attCommField();
  });

});

function attCommField(){

  s = [];

  s[0] = "People " + $("input[name=over]:checked").val() + " this ad from '" + $("#comp").val() + " about " + $("#serv").val() + " because " + $("#reas").val() + ". ";
  s[1] = "I am " + $("input[name=over]:checked").val() + " this ad from '" + $("#comp").val() + "' about " + $("#serv").val() + " because " + $("#reas").val() + ". ";

  if($("input[name=over]:checked").val() == "not sure if people should or should not see"){
    i=1;
  }else{
    i=0;
  }

  if($("#expl").val().trim() != ""){
    s[i] += $("#expl").val() + ". ";
  }

  if($("#add").val().trim() != ""){
    s[i] += "Also, " + $("#add").val() + ".";
  }

  $("#comm").val( s[i] );

  translate();
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


