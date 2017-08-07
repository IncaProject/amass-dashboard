    function doChart16(chartDataSixteen) {
    console.log('doChart16() called');
    anychart.licenseKey("bfef.biz-5e9092fb-70cd7951");
    anychart.theme('darkBlue');
    var radar = anychart.fromJson(chartDataSixteen);
    var credits = radar.credits();
    credits.enabled(false);
    radar.container('container16');
    radar.draw();

    };
