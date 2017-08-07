       function doChart6(chartDataSix) {
    console.log('doChart6() called');
    anychart.licenseKey("bfef.biz-5e9092fb-70cd7951");
    anychart.theme('darkBlue');
    var chart = anychart.fromJson(chartDataSix);
    var credits = chart.credits();
    credits.enabled(false);
    chart.container('container6');
    chart.bounds(0, 0, '100%', '100%');
    chart.draw();

    };
