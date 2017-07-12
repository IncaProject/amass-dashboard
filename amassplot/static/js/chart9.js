  function doChartNine(chartDataEight) {
        // create pie chart with passed data
        var gauge = anychart.fromJson(chartDataEight|safe);
        gauge.draw();

    };
