# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import GatewayCipres
from django.shortcuts import render
import json
import pandas as pd


# Create your views here.
def index(request):
    data = GatewayCipres.objects.values("TOOL_NAME", "ERROR_MSG")

    datalist = list(data)

    chartlist = [[x['TOOL_NAME'], x['ERROR_MSG']] for x in datalist]
    # now get count for toolname and errormsg
    chartdf = pd.DataFrame(chartlist, columns=['toolname', 'errormsg'])
    # form list of list needed for charting
    chartjsonone = countPieChartJson(chartdf, colnamex="toolname", charttitle="Tool Name", chartcontainerstr="chart")
    chartjsontwo = countPieChartJson(chartdf, colnamex="errormsg", charttitle="Error Msg", chartcontainerstr="chart")
    chartjsonthree = countBarChartJson(chartdf, colnamex="toolname", charttitle="Tool Name",
                                       charttitlex="Tool Name", charttitley="Count", chartcontainerstr="chart")

    context = {"chartDataOne": chartjsonone, "chartDataTwo": chartjsontwo, "chartDataThree": chartjsonthree,
               "title": "AMASS Plot Dashboard"}

    return render(request, 'index.html', context)


def countPieChartJson(chartdf, colnamex, charttitle, chartcontainerstr):
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


def countBarChartJson(chartdf, colnamex, charttitle, charttitlex, charttitley, chartcontainerstr):
    summary = pd.DataFrame(chartdf[colnamex].value_counts())
    chartdf = pd.DataFrame({colnamex: list(summary.index), 'count': summary[colnamex]})
    chartdf = chartdf[[colnamex, 'count']]
    chartdataone = chartdf.values.tolist()

    chart = {
        "chart": {
        "container": chartcontainerstr,
        "enabled": True,
        "title": {
            "enabled": True,
            "text": charttitle,
        },
        "padding": {
            "left": 20,
            "top": 10,
            "bottom": 5,
            "right": 40
        },
        "animation": {
            "enabled": True
        },
        "tooltip": {
            "positionMode": "point",
            "enabled": True
        },

        "selectMarqueeFill": {
            "color": "#d3d3d3",
            "opacity": 0.4
        },
        "interactivity": {
            "hoverMode": "byX"
        },
        "xScale": 0,
        "yScale": 1,
        "series": [
            {
                "enabled": True,
                "seriesType": "bar",
                "tooltip": {
                    "titleFormat": "{%X}",
                    "format": "{%Value}",
                    "position": "rightCenter",
                    "anchor": "leftCenter",
                    "offsetX": 5,
                    "offsetY": 0
                },
                "data": chartdataone,
                "xScale": 0,
                "yScale": 1
            }
        ],
        "xAxes": [
            {
                "enabled": True,
                "title": {
                    "enabled": True,
                    "text": charttitlex
                }
            }
        ],
        "yAxes": [
            {
                "enabled": True,
                "title": {
                    "enabled": True,
                    "text": charttitley
                },
                "labels": {
                    "enabled": True,
                    "format": "{%Value}{groupsSeparator: }"
                }
            }
        ],
        "scales": [
            {},
            {
                "minimum": 0
            }
        ],
        "type": "bar"
        }
    }
    chartjson = json.dumps(chart)
    return chartjson
