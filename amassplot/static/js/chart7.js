    function doChartSeven(chartDataSix) {
        // create pie chart with passed data
         var chart = anychart.fromJson(chartDataSix|safe);
        chart.bounds(0, 160, '80%', '70%');
        chart.draw();

    };
