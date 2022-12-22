$(document).ready(function(){$(".section1").hide();$(".less1").hide(); });
// ]]></script><script>
$(document).ready(function(){
  $(".less1").click(function(){
$(".section1").toggle();$(".more1").toggle();$(".less1").toggle();
  });
  $(".more1").click(function(){  $(".section1").toggle();$(".less1").toggle();$(".more1").toggle();
  });
});

$(document).ready(function(){$(".section2").hide();$(".less2").hide(); });
// ]]></script><script>
$(document).ready(function(){
  $(".less2").click(function(){
$(".section2").toggle();$(".more2").toggle();$(".less2").toggle();
  });
  $(".more2").click(function(){  $(".section2").toggle();$(".less2").toggle();$(".more2").toggle();
  });
});