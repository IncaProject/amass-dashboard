   function doChart13(chartDataThirteen) {
        // create pie chart with passed data
        console.log('doChart13() called');
        anychart.licenseKey("bfef.biz-5e9092fb-70cd7951");
        anychart.theme('darkBlue');
        var chart = anychart.fromJson(chartDataThirteen);
        var credits = chart.credits();
        credits.enabled(false);
        chart.bounds(0, 0, '100%', '100%');
        chart.container('container13');
        chart.draw();

    };
