 function doChart2(chartDataTwo) {
        anychart.theme('darkBlue');

        // create pie chart with passed data
        var chart = anychart.fromJson(chartDataTwo|safe);
        chart.innerRadius('40%');
        // set chart labels position to outside
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
        chart.bounds(0,  0, '80%', '60%');
        chart.draw();

    };