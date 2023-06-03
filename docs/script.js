$(function(){
  let color=0;
  let colors=['lightyellow','lightgray','lightpink','lightblue'];
  $("#button").on("click",function(){
    if(color>=colors.length)color=0;
    $('body').css('background-color',colors[color]);
    color++;
  });
});