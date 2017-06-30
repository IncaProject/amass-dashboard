# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import GatewayCipres
from django.shortcuts import render
import json
import pandas as pd

# Create your views here.
def index(request):
    data = GatewayCipres.objects.values("TOOL_NAME","ERROR_MSG")

    datalist = list(data)

    chartlist = [ [ x['TOOL_NAME'], x['ERROR_MSG'] ] for x in datalist ]
    # now get count for toolname and errormsg
    chartdf = pd.DataFrame(chartlist, columns =['toolname', 'errormsg'] )
    # form list of list needed for charting
    chartjsonone = countPieChartJson(chartdf, colnamex="toolname", charttitle="Tool Name", chartcontainerstr="chart")
    chartjsontwo = countPieChartJson(chartdf, colnamex="errormsg", charttitle="Error Msg", chartcontainerstr="chart")

    context = {"chartDataOne": chartjsonone, "chartDataTwo": chartjsontwo, "title": "AMASS Plot Dashboard"}


    return render(request, 'index.html', context)


def countPieChartJson(chartdf,colnamex, charttitle, chartcontainerstr):
    summary = pd.DataFrame(chartdf[colnamex].value_counts())
    chartdf = pd.DataFrame({colnamex: list(summary.index), 'count': summary[colnamex]})
    chartdf = chartdf[[colnamex, 'count']]
    chartdataone = chartdf.values.tolist()
    chart = {
        "chart": {
            "type": "pie",
            "title": charttitle,
            "data": chartdataone,
            "container": chartcontainerstr
        }
    }
    chartjson = json.dumps(chart)
    return chartjson
