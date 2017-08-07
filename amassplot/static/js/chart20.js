  function doChart20(chartDataTwenty) {
      console.log('doChart20() called');
      anychart.licenseKey("bfef.biz-5e9092fb-70cd7951");
      anychart.theme('darkBlue');
      var gauge = anychart.fromJson(chartDataTwenty);
      var credits = gauge.credits();
      credits.enabled(false);
      gauge.container('container20');
      gauge.draw();

    };

