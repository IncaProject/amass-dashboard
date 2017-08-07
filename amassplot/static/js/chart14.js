  function doChart14(chartDataFourteen) {
        // create pie chart with passed data
        console.log('doChart14() called');
        anychart.licenseKey("bfef.biz-5e9092fb-70cd7951");
        anychart.theme('darkBlue');
        var chart = anychart.fromJson(chartDataFourteen);
        var credits = chart.credits();
        credits.enabled(false);
        chart.innerRadius('40%');
        // set chart labels position to outside
        //create variables for legends
        chart.labels().position('outside');
         // legends
        var legend = chart.legend();
        legend.enabled(true);
        // Set maximum width and height.
        legend.maxWidth("80%");
        legend.maxHeight("20%");
        // set position mode
        legend.positionMode("outside");
        // set position and alignement
        legend.position("bottom");
        legend.align("center");
        legend.itemsLayout("verticalExpandable");
        // paginator position
        legend.paginator().orientation("bottom");
        // initiate chart drawing
        chart.bounds(0, 0, '100%', '100%');
        chart.container('container14');
        chart.draw();

    };