var slider = d3.slider().min(0).max(1).value(1).ticks(1).showRange(true);
  d3.select('#testslider').call(slider);

  var slider2 = d3.slider();
  d3.select('#testslider2').call(slider2);