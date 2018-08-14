$(function(){

  $("#form_search_ads").submit(function(e){

    $.ajax({

      url: "/ads/show_all",
      type: "GET",
      data: $(this).serialize(),
      timeout: 12000,
      dataType: "json",
      success: function(data){
        html = "<div class='col-md-12 text-center'><h3>Search results:</h3></div>";
        //for each add
        for(var i=0; i<data.length; i++){

          if(i%4 == 0){
            html += '<div class="row row-eq-height">';
          }

          html += 
          '<div class="col-md-3">'+
            '<ul class="list-group ads-list">'+
              '<li class="list-group-item active ads-list-title text-center">'+data[i].company+'</li>'+
             '<li class="list-group-item"><b>Offensive:</b> '+data[i].rate.offensive+'</li>'+
              '<li class="list-group-item"><b>Misleading:</b> '+data[i].rate.misleading+'</li>'+
              '<li class="list-group-item"><b>Inappropriate:</b> '+data[i].rate.inappropriate+'</li>'+
              '<li class="list-group-item"><b>Overall:</b> '+data[i].rate.overall+'</li>'+
              '<li class="list-group-item comment-item"><b>Comment:</b> '+data[i].rate.comment+'</li>'+
              '<li class="list-group-item text-center"><a class="btn btn-default" href="/ads/show?ad_id='+data[i].id+'">Select</a></li>'+
            '</ul>'+
          '</div>';

          if(i%4 == 3){
            html += '</div>';
          }
        }

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


