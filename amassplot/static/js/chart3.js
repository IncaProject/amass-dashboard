 function doChart3(chartDataThree) {
        // create pie chart with passed data
        anychart.theme('darkBlue');

        var chart = anychart.fromJson(chartDataThree|safe);
        chart.bounds(0, 20, '80%', '80%');
        chart.draw();

    };
