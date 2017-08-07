    function doChart7(chartDataSeven) {
    console.log('doChart7() called');
    anychart.licenseKey("bfef.biz-5e9092fb-70cd7951");
    anychart.theme('darkBlue');
    var radar = anychart.fromJson(chartDataSeven);
    var credits = radar.credits();
    credits.enabled(false);
    radar.container('container7');
    radar.draw();

    };
