   function doChart4(chartDataFour) {
        // create pie chart with passed data
        console.log('doChart4() called');
        anychart.licenseKey("bfef.biz-5e9092fb-70cd7951");
        anychart.theme('darkBlue');
        var chart = anychart.fromJson(chartDataFour);
        var credits = chart.credits();
        credits.enabled(false);
        chart.bounds(0, 0, '100%', '100%');
        chart.container('container4');
        chart.draw();

    };
