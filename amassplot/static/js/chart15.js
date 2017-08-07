  function doChart15(chartDataFifteen) {
        // create pie chart with passed data
            console.log('doChart15() called');
            anychart.licenseKey("bfef.biz-5e9092fb-70cd7951");
            anychart.theme('darkBlue');
            var chart = anychart.fromJson(chartDataFifteen);
            var credits = chart.credits();
            credits.enabled(false);
            chart.container('container15');
            chart.bounds(0, 0, '100%', '100%');
            chart.draw();

    };