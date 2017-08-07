  function doChart8(chartDataEight) {
      console.log('doChart8() called');
      anychart.licenseKey("bfef.biz-5e9092fb-70cd7951");
      anychart.theme('darkBlue');
      var gauge = anychart.fromJson(chartDataEight);
      var credits = gauge.credits();
      credits.enabled(false);
      gauge.container('container8');
      gauge.draw();

    };

