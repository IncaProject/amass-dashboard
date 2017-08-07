  function doChart17(chartDataSeventeen) {
      console.log('doChart17() called');
      anychart.licenseKey("bfef.biz-5e9092fb-70cd7951");
      anychart.theme('darkBlue');
      var gauge = anychart.fromJson(chartDataSeventeen);
      var credits = gauge.credits();
      credits.enabled(false);
      gauge.container('container17');
      gauge.draw();

    };

