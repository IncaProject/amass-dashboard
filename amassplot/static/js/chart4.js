   function doChart4(chartDataFour) {
        // create pie chart with passed data

        var chart = anychart.fromJson(chartDataFour|safe);
        chart.bounds(0, 160, '80%', '70%');
        chart.draw();

    };
