# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import GatewayCipres, CometCipres, GordonCipres, IncaCipres
from decimal import *
from django.shortcuts import render
import json
import pandas as pd
import numpy
import statistics
import cPickle as pickle

# Create your views here.
def index(request):
    data = GatewayCipres.objects.values("TOOL_NAME", "ERROR_MSG", "RESULT", "TERMINATE_DATE", "REMOTE_JOB_SUBMIT_DATE")
    datatwo = CometCipres.objects.values("resource_id")
    datathree= GordonCipres.objects.values("resource_id")
    datafour = CometCipres.objects.values("newturnaroundtime")
    datafive = GordonCipres.objects.values("newturnaroundtime")
    datasix = GatewayCipres.objects.values("RESULT")
    dataseven = IncaCipres.objects.values("RESULT")
    datalist = list(data)
    datalisttwo = list(datatwo) + list(datathree)
    datalistthree = list(datafour)
    datalistfour = list(datafive)
    datalistfive = list(datasix)
    datalistsix = list(dataseven)


    chartlist = [[x['TOOL_NAME'], x['ERROR_MSG'], x['RESULT'], x['REMOTE_JOB_SUBMIT_DATE'], x['TERMINATE_DATE']] for x in datalist]
    chartlisttwo = [[x['resource_id']] for x in datalisttwo]
    chartlistthree = [[x['newturnaroundtime']] for x in datalistthree]
    chartlistfour = [[x['newturnaroundtime']] for x in datalistfour]
    chartlistfive =  [[x['RESULT']] for x in datalistfive]
    chartlistsix =  [[x['RESULT']] for x in datalistsix]
    chartlistseven = [[x['RESULT']] for x in datalistsix]

    # now get count for toolname and errormsg
    chartdf = pd.DataFrame(chartlist, columns=['toolname', 'errormsg', 'result','remotejbsubdate','termdate'])
    chartdftwo = pd.DataFrame(chartlisttwo, columns=['resourceid'] )
    chartdfthree = pd.DataFrame(chartlistthree, columns=['newturnaroundtime'])
    chartdffour = pd.DataFrame(chartlistfour, columns=['newturnaroundtime'])
    chartdffive = pd.DataFrame(chartlistfive, columns=['result'])
    chartdfsix = pd.DataFrame(chartlistsix, columns=['result'])
    chartdfseven = pd.DataFrame(chartlistseven, columns=['result'])



    # now transform column names as needed
    chartdf['result'].replace([0, 1], ['Failed Jobs', 'Successful Jobs'], inplace=True)
    #chartdf['dff'] = chartdf['termdate'] - chartdf['remotejbsubdate']
    chartdftwo['resourceid'].replace([2814, 2796], ['Comet', 'Gordon'], inplace=True)
    chartdftwo = chartdftwo.loc[(chartdftwo!=0).any(axis=1)]
    chartdfseven['result'].replace([0, 1], ['Failed Jobs', 'Successful Jobs'], inplace=True)

    a = int((chartdffive['result'] == 1).sum())
    b = int((chartdfsix['result'] == 1).sum())
    x = float(int((chartdffive['result'] == 1).sum() + (chartdffive['result'] == 0).sum()))
    y = float(int((chartdfsix['result'] == 1).sum() + (chartdfsix['result'] == 0).sum()))
    e =a / x
    f = b/ y
    print e
    print f

    #for turnaround times, this is getting standard deviation, mean, median, min value, and max value
    #COMET DATA
    # print(chartdfthree['newturnaroundtime'].mean(),
    # chartdfthree['newturnaroundtime'].median(),
    # chartdfthree['newturnaroundtime'].std(),
    # chartdfthree['newturnaroundtime'].min(),
    # chartdfthree['newturnaroundtime'].max())
    # # #GORDON DATA
    # print(chartdffour['newturnaroundtime'].mean(),
    #       chartdffour['newturnaroundtime'].median(),
    #       chartdffour['newturnaroundtime'].std(),
    #       chartdffour['newturnaroundtime'].min(),
    #       chartdffour['newturnaroundtime'].max())



    # chartdfthree['end_time']= pd.to_datetime(chartdfthree['end_time']).apply(lambda x: x.date())
    # chartdfthree['start_time'] = pd.to_datetime(chartdfthree['start_time']).apply(lambda x: x.date())
    # chartdfthree['turnaroundtime'] = chartdfthree['end_time'] - chartdfthree['start_time']
    #chartdfthree['resourceid'].replace([2814, 2796], ['Comet', 'Gordon'], inplace=True)
    # form list of list needed for charting
    chartjsonone = countPieChartJson(chartdf, colnamex="toolname", charttitle="Tool Name", chartcontainerstr="chart")
    chartjsontwo = countPieChartJson(chartdf, colnamex="errormsg", charttitle="Error Msg", chartcontainerstr="chart")
    chartjsonthree = countBarChartJson(chartdf, colnamex="toolname", charttitle="Tool Name",
                                       charttitlex="Tool Name", charttitley="Count", chartcontainerstr="chart")
    chartjsonfour = countBarVerticalChartJson(chartdf, colnamex="toolname", charttitle="Tool Name",
                                       charttitlex="Tool Name", charttitley="# of Jobs", chartcontainerstr="chart")
    chartjsonfive = countDonutChart(chartdf, colnamex="result", charttitle="RESULT of Successful/Failed Jobs(Comet)", chartcontainerstr="chart")
    chartjsonsix = countColumnChart(chartdftwo, colnamex="resourceid", charttitle="CIPRES", charttitlex="Resources", charttitley="Number of Jobs", chartcontainerstr="chart")
    chartjsonseven = radarChart(chartdfthree, chartdffour, colnamex="newturnaroundtime", charttitle="Turnaround Times for Cipres(Hours)", chartcontainerstr="chart")
    chartjsoneight = gaugeChart(chartdffive, chartdfsix, colnamex="result", charttitle="Success Rates for Jobs", chartcontainerstr="chart")
    chartjsonnine = countDonutTwoChart(chartdfseven, colnamex="result", charttitle="RESULT of Successful/Failed Jobs(Gordon)", chartcontainerstr="chart")
    context = {"chartDataOne": chartjsonone, "chartDataTwo": chartjsontwo, "chartDataThree": chartjsonthree, "chartDataFour": chartjsonfour,
               "chartDataFive": chartjsonfive,
               "chartDataSix": chartjsonsix,
               "chartDataSeven": chartjsonseven,
               "chartDataEight": chartjsoneight,
               "chartDataNine": chartjsonnine,
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

def countBarVerticalChartJson(chartdf, colnamex, charttitle, charttitlex, charttitley, chartcontainerstr):
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
    "tooltip": {
      "anchor": "leftTop",
      "displayMode": "union",
      "enabled": True
    },
    "credits": {
      "text": "AnyChart",
      "url": "https://www.anychart.com/?utm_source=registered",
      "alt": "AnyChart - JavaScript Charts designed to be embedded and integrated",
      "imgAlt": "AnyChart - JavaScript Charts",
      "logoSrc": "https://static.anychart.com/logo.png",
      "enabled": False
    },
    "selectMarqueeFill": {
      "color": "#d3d3d3",
      "opacity": 0.4
    },
    "interactivity": {
      "hoverMode": "byX"
    },
    "xScale": 0,
    "yScale": 20000,
    "series": [
      {
        "enabled": True,
        "seriesType": "bar",
        "name": "Actual",
        "data":
         chartdataone,
        "xScale": 0,
        "yScale": 20000,
      },
      {
        "enabled": True,
        "seriesType": "line",
        "name": "Optimal",
        "markers": {
          "enabled": True,
          "size": 5
        },
        "stroke": {
          "color": "#f18126",
          "thickness": 3
        },
        "data":
          chartdataone,
        "xScale": 0,
        "yScale": 20000
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
        }
      }
    ],
    "scales": [
      {},
      {
        "maximum": 20000,
        "minimum": 0
      }
    ],
    "type": "bar"
  }
    }
    chartjson = json.dumps(chart)
    return chartjson

def countDonutChart(chartdf, colnamex, charttitle, chartcontainerstr):
    summary = pd.DataFrame(chartdf[colnamex].value_counts())
    chartdf = pd.DataFrame({colnamex: list(summary.index), 'count': summary[colnamex]})
    chartdf = chartdf[[colnamex, 'count']]
    chartdataone = chartdf.values.tolist()

    chart = {
        "chart": {
        "enabled": True,
            "container": chartcontainerstr,
        "title": {

          "enabled": True,
            "text": charttitle,

         },
            "credits": {
                "text": "AnyChart",
                "url": "https://www.anychart.com/?utm_source=registered",
                "alt": "AnyChart - JavaScript Charts designed to be embedded and integrated",
                "imgAlt": "AnyChart - JavaScript Charts",
                "logoSrc": "https://static.anychart.com/logo.png",
                "enabled": False
            },
            "selectMarqueeFill": {
                "color": "#d3d3d3",
                "opacity": 0.4
            },
            "type": "pie",
            "data": chartdataone
            ,
            "labels": {
                "enabled": True,
                "disablePointerEvents": True
            },
            "radius": "43%",
            "innerRadius": "30%",
            "hoverHatchFill": "none"
        }




  }


    chartjson = json.dumps(chart)
    return chartjson

def countColumnChart(chartdftwo, colnamex, charttitle, charttitlex, charttitley, chartcontainerstr):

    summary = pd.DataFrame(chartdftwo[colnamex].value_counts())
    chartdftwo = pd.DataFrame({colnamex: list(summary.index), 'count': summary[colnamex]})
    chartdftwo = chartdftwo[[colnamex, 'count']]
    chartdataone = chartdftwo.values.tolist()




    chart = {
        "chart": {
            "container": chartcontainerstr,
            "enabled": True,
            "title": {
                "enabled": True,
                "text": charttitle,
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
                    "seriesType": "column",
                    "tooltip": {
                        "titleFormat": "{%X}",
                        "format": "{%Value}",
                        "position": "centerTop",
                        "anchor": "centerBottom",
                        "offsetX": 5,
                        "offsetY": 0
                    },
                    "data":chartdataone,



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
            "type": "column"
        }
    }



    chartjson = json.dumps(chart)
    return chartjson

def radarChart(chartdfthree, chartdffour, colnamex, charttitle, chartcontainerstr):

    chart = {
        "chart": {
    "enabled": True,
    "container": chartcontainerstr,
    "title": {
      "enabled": True,
      "text": charttitle
    },
    "tooltip": {
      "format": "Value: {%Value}",
      "enabled": True
    },
    "credits": {
      "text": "AnyChart",
      "url": "https://www.anychart.com/?utm_source=registered",
      "alt": "AnyChart - JavaScript Charts designed to be embedded and integrated",
      "imgAlt": "AnyChart - JavaScript Charts",
      "logoSrc": "https://static.anychart.com/logo.png",
      "enabled": False
    },
    "selectMarqueeFill": {
      "color": "#d3d3d3",
      "opacity": 0.4
    },
    "legend": {
      "enabled": True
    },
    "xScale": 0,
    "yScale": 1,
    "series": [
      {
        "enabled": True,
        "seriesType": "line",
        "meta": {},
        "name": "Comet",
        "markers": {
          "enabled": True,
          "type": "circle",
          "size": 2
        },
        "data": [
            {
                "x": "Mean",
                "value": chartdfthree[colnamex].mean()
            },
            {
                "x": "Median",
                "value": chartdfthree[colnamex].median()
            },
            {
                "x": "Standard Deviation",
                "value": chartdfthree[colnamex].std()
            },
            {
                "x": "Longest",
                "value": chartdfthree[colnamex].max()
            },
            {
                "x": "Shortest",
                "value": chartdfthree[colnamex].min()
            }

        ],
        "xScale": 0,
        "yScale": 1
      },

      {
        "enabled": True,
        "seriesType": "line",
        "meta": {},
        "name": "gordon",
        "markers": {
          "enabled": True,
          "type": "circle",
          "size": 2
        },
        "data": [
            {
                "x": "Mean",
                "value": chartdffour[colnamex].mean()
            },
            {
                "x": "Median",
                "value": chartdffour[colnamex].median()
            },
            {
                "x": "Standard Deviation",
                "value": chartdffour[colnamex].std()
            },
            {
                "x": "Longest",
                "value": chartdffour[colnamex].max()
            },
            {
                "x": "Shortest",
                "value": chartdffour[colnamex].min()
            }

        ],
        "xScale": 0,
        "yScale": 1
      }
    ],
    "xAxis": {
      "enabled": True,
      "labels": {
        "enabled": True,
        "padding": {
          "left": 5,
          "top": 5,
          "bottom": 5,
          "right": 5
        }
      }
    },
    "scales": [
      {},
      {
         "type": "log",
        "maximum": 22000,
        "minimum": 0,
        "ticks": {
          "mode": "logarithmic"
        },
        "minorTicks": {
          "mode": "logarithmic"
        },
        "logBase": 7.58
      }
    ],
    "type": "radar"
  }
    }
    chartjson = json.dumps(chart)
    return chartjson

def gaugeChart(chartdffive, chartdfsix, colnamex, charttitle, chartcontainerstr):
    a = int((chartdffive['result'] == 1).sum())
    b = int((chartdfsix['result'] == 1).sum())
    x = float(int((chartdffive['result'] == 1).sum() + (chartdffive['result'] == 0).sum()))
    y = float(int((chartdfsix['result'] == 1).sum() + (chartdfsix['result'] == 0).sum()))
    e = (a / x) * 100
    f = (b / y) * 100

    chart = {"gauge": {
    "enabled": True,
    "container": chartcontainerstr,
    "title": {
      "enabled": True,
      "useHtml": True,
      "text": charttitle,
      "margin": {
        "bottom": 20
      },
      "padding": {
        "left": 0,
        "top": 0,
        "bottom": 0,
        "right": 0
      }
    },
    "margin": {
      "left": 50,
      "top": 50,
      "bottom": 50,
      "right": 50
    },
    "padding": {
      "left": 0,
      "top": 0,
      "bottom": 0,
      "right": 0
    },
    "chartLabels": [
      {
        "enabled": True,
        "zIndex": 50,
        "fontSize": 13,
        "fontFamily": "Verdana, Helvetica, Arial, sans-serif",
        "fontColor": "#7c868e",
        "fontOpacity": 1,
        "fontDecoration": "none",
        "fontStyle": "normal",
        "fontVariant": "normal",
        "fontWeight": "normal",
        "letterSpacing": "normal",
        "textDirection": "ltr",
        "lineHeight": "normal",
        "textIndent": 0,
        "vAlign": "middle",
        "hAlign": "center",
        "textWrap": "byLetter",
        "textOverflow": "",
        "selectable": False,
        "disablePointerEvents": False,
        "useHtml": True,
        "background": {
          "zIndex": 0,
          "enabled": False,
          "fill": "#ffffff",
          "stroke": "none",
          "disablePointerEvents": False,
          "cornerType": "round",
          "corners": 0
        },
        "padding": {
          "left": 10,
          "top": 0,
          "bottom": 0,
          "right": 10
        },
        "height": "8.5%",
        "anchor": "rightCenter",
        "offsetX": 0,
        "offsetY": "100%",
        "text": "Comet, <span style=\"\">93.6%</span>",
        "minFontSize": 8,
        "maxFontSize": 72,
        "adjustFontSize": {
          "width": False,
          "height": False
        },
        "rotation": 0,
        "position": "leftTop"
      },
      {
        "enabled": True,
        "zIndex": 50,
        "fontSize": 13,
        "fontFamily": "Verdana, Helvetica, Arial, sans-serif",
        "fontColor": "#7c868e",
        "fontOpacity": 1,
        "fontDecoration": "none",
        "fontStyle": "normal",
        "fontVariant": "normal",
        "fontWeight": "normal",
        "letterSpacing": "normal",
        "textDirection": "ltr",
        "lineHeight": "normal",
        "textIndent": 0,
        "vAlign": "middle",
        "hAlign": "center",
        "textWrap": "byLetter",
        "textOverflow": "",
        "selectable": False,
        "disablePointerEvents": False,
        "useHtml": True,
        "background": {
          "zIndex": 0,
          "enabled": False,
          "fill": "#ffffff",
          "stroke": "none",
          "disablePointerEvents": False,
          "cornerType": "round",
          "corners": 0
        },
        "padding": {
          "left": 10,
          "top": 0,
          "bottom": 0,
          "right": 10
        },
        "height": "8.5%",
        "anchor": "rightCenter",
        "offsetX": 0,
        "offsetY": "80%",
        "text": "Gordon, <span style=\"\">96.6%</span>",
        "minFontSize": 8,
        "maxFontSize": 72,
        "adjustFontSize": {
          "width": False,
          "height": False
        },
        "rotation": 0,
        "position": "leftTop"
      }
    ],
    "credits": {
      "text": "AnyChart",
      "url": "https://www.anychart.com/?utm_source=registered",
      "alt": "AnyChart - JavaScript Charts designed to be embedded and integrated",
      "imgAlt": "AnyChart - JavaScript Charts",
      "logoSrc": "https://static.anychart.com/logo.png",
      "enabled": False
    },
    "selectMarqueeFill": {
      "color": "#d3d3d3",
      "opacity": 0.4
    },
    "type": "circular",
    "fill": "#fff",
    "stroke": "none",
    "sweepAngle": 270,
    "data": [
      round(e,1),
      round(f,1)
    ],
    "axes": [
      {
        "enabled": True,
        "scale": {
          "type": "linear",
          "inverted": False,
          "maximum": 100,
          "minimum": 0,
          "minimumGap": 0.1,
          "maximumGap": 0.1,
          "softMinimum": None,
          "softMaximum": None,
          "maxTicksCount": 1000,
          "ticks": {
            "mode": "linear",
            "base": 0,
            "interval": 1
          },
          "minorTicks": {
            "mode": "linear",
            "base": 0,
            "interval": 1
          },
          "stackMode": "none",
          "stickToZero": True
        },
        "ticks": {
          "enabled": False,
          "zIndex": 10
        },
        "minorTicks": {
          "enabled": False,
          "zIndex": 10
        },
        "labels": {
          "enabled": False,
          "zIndex": 10.00004
        },
        "minorLabels": {
          "enabled": False,
          "zIndex": 10.00004
        },
        "width": "1%",
        "radius": "100%",
        "fill": "none"
      }
    ],
    "bars": [
      {
        "enabled": True,
        "zIndex": 5,
        "fill": "#64b5f6",
        "stroke": "none",
        "hatchFill": "none",
        "axisIndex": 0,
        "dataIndex": 0,
        "position": "center",
        "width": "17%",
        "radius": "100%"
      },
      {
        "enabled": True,
        "zIndex": 5,
        "fill": "#1976d2",
        "stroke": "none",
        "hatchFill": "none",
        "axisIndex": 0,
        "dataIndex": 1,
        "position": "center",
        "width": "17%",
        "radius": "80%"
      }
    ]
  }
}
    chartjson = json.dumps(chart)
    return chartjson

def countDonutTwoChart(chartdfseven, colnamex, charttitle, chartcontainerstr):
    summary = pd.DataFrame(chartdfseven[colnamex].value_counts())
    chartdfseven = pd.DataFrame({colnamex: list(summary.index), 'count': summary[colnamex]})
    chartdfseven = chartdfseven[[colnamex, 'count']]
    chartdataone = chartdfseven.values.tolist()

    chart = {
        "chart": {
        "enabled": True,
            "container": chartcontainerstr,
        "title": {

          "enabled": True,
            "text": charttitle,

         },
            "credits": {
                "text": "AnyChart",
                "url": "https://www.anychart.com/?utm_source=registered",
                "alt": "AnyChart - JavaScript Charts designed to be embedded and integrated",
                "imgAlt": "AnyChart - JavaScript Charts",
                "logoSrc": "https://static.anychart.com/logo.png",
                "enabled": False
            },
            "selectMarqueeFill": {
                "color": "#d3d3d3",
                "opacity": 0.4
            },
            "type": "pie",
            "data": chartdataone
            ,
            "labels": {
                "enabled": True,
                "disablePointerEvents": True
            },
            "radius": "43%",
            "innerRadius": "30%",
            "hoverHatchFill": "none"
        }




  }


    chartjson = json.dumps(chart)
    return chartjson
