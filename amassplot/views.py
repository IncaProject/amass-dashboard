# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import GatewayCipres, CometCipres, GordonCipres

from django.shortcuts import render
import json
import pandas as pd
import cPickle as pickle

# Create your views here.
def index(request):
    data = GatewayCipres.objects.values("TOOL_NAME", "ERROR_MSG", "RESULT", "TERMINATE_DATE", "REMOTE_JOB_SUBMIT_DATE")
    datatwo = CometCipres.objects.values("resource_id")
    datathree= GordonCipres.objects.values("resource_id")
    datalist = list(data)
    datalisttwo = list(datatwo) + list(datathree)


    chartlist = [[x['TOOL_NAME'], x['ERROR_MSG'], x['RESULT'], x['REMOTE_JOB_SUBMIT_DATE'], x['TERMINATE_DATE']] for x in datalist]
    chartlisttwo = [[x['resource_id']] for x in datalisttwo]
    chartlistthree = [[x['resource_id']] for x in datalisttwo]
    # now get count for toolname and errormsg
    chartdf = pd.DataFrame(chartlist, columns=['toolname', 'errormsg', 'result','remotejbsubdate','termdate'])
    chartdftwo = pd.DataFrame(chartlisttwo, columns=['resourceid'] )
    #chartdfthree = pd.DataFrame(chartlistthree, columns=['resourceid'])

    # now transform column names as needed
    chartdf['result'].replace([0, 1], ['Failed Jobs', 'Successful Jobs'], inplace=True)
    #chartdf['dff'] = chartdf['termdate'] - chartdf['remotejbsubdate']
    chartdftwo['resourceid'].replace([2814, 2796], ['Comet', 'Gordon'], inplace=True)
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
    chartjsonfive = countDonutChart(chartdf, colnamex="result", charttitle="RESULT of Successful/Failed Jobs", chartcontainerstr="chart")
    chartjsonsix = countColumnChart(chartdftwo, colnamex="resourceid", charttitle="CIPRES", charttitlex="Resources", charttitley="Number of Jobs", chartcontainerstr="chart")
    chartjsonseven = countGaugeChart(chartdftwo, colnamex="resourceid", charttitle="Different Companies Success Rates", chartcontainerstr="chart")
    context = {"chartDataOne": chartjsonone, "chartDataTwo": chartjsontwo, "chartDataThree": chartjsonthree, "chartDataFour": chartjsonfour,
               "chartDataFive": chartjsonfive,
               "chartDataSix": chartjsonsix,
               "chartDataSeven": chartjsonseven,
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

# def countComparisonChart(chartdf, colnamex, colnamextwo, charttitle, chartcontainerstr):
#     summary = pd.DataFrame(chartdf[colnamex].value_counts(), chartdf[colnamextwo].value_counts())
#     chartdf = pd.DataFrame({colnamex: list(summary.index), colnamextwo: list(summary.index), 'count': summary[colnamex], 'counttwo':summary[colnamextwo]})
#     chartdf = chartdf[[colnamex, colnamextwo, 'count', 'counttwo']]
#     chartdataone = chartdf.values.tolist()
#
#     chart = {
#         "chart": {
#     "enabled": True,
#     "container": chartcontainerstr,
#     "title": {
#       "enabled": True,
#       "text": charttitle
#     },
#     "credits": {
#       "text": "AnyChart",
#       "url": "https://www.anychart.com/?utm_source=registered",
#       "alt": "AnyChart - JavaScript Charts designed to be embedded and integrated",
#       "imgAlt": "AnyChart - JavaScript Charts",
#       "logoSrc": "https://static.anychart.com/logo.png",
#       "enabled": False
#     },
#     "selectMarqueeFill": {
#       "color": "#d3d3d3",
#       "opacity": 0.4
#     },
#     "legend": {
#       "enabled": True,
#       "position": "bottom"
#     },
#     "defaultSeriesType": "area",
#     "xScale": 0,
#     "yScale": 1,
#     "series": [
#       {
#         "enabled": True,
#         "seriesType": "area",
#         "meta": {},
#         "name": "Arizona",
#         "data": [
#          chartdataone,
#         ],
#         "xScale": 0,
#         "yScale": 1
#       },
#       {
#         "enabled": True,
#         "seriesType": "area",
#         "meta": {},
#         "name": "Florida",
#         "data": [
#           chartdataone
#         ],
#         "xScale": 0,
#         "yScale": 1
#       },
#       {
#         "enabled": True,
#         "seriesType": "area",
#         "meta": {},
#         "name": "Nevada",
#         "data": [
#          chartdataone
#         ],
#         "xScale": 0,
#         "yScale": 1
#       }
#     ],
#     "yAxis": {
#       "enabled": True,
#       "labels": {
#         "enabled": True,
#         "fontColor": "#545f69",
#         "format": "{%Value}{scale:(1000000)|(M)}"
#       },
#       "ticks": {
#         "enabled": True,
#         "stroke": "#545f69"
#       },
#       "stroke": "#545f69"
#     },
#     "scales": [
#       {},
#       {
#         "stackMode": "value"
#       }
#     ],
#     "type": "radar"
#   }
#
#     }
#     chartjson = json.dumps(chart)
#     return chartjson

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

def countGaugeChart(chartdftwo, colnamex, charttitle, chartcontainerstr):
    summary = pd.DataFrame(chartdftwo[colnamex].value_counts())
    chartdftwo = pd.DataFrame({colnamex: list(summary.index), 'count': summary[colnamex]})
    chartdftwo = chartdftwo[[colnamex, 'count']]
    chartdftwo.values.tolist()
    chart = {
  "gauge": {
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
        "text": "Temazepam, <span style=\"\">23%</span>",
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
        "text": "Guaifenesin, <span style=\"\">34%</span>",
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
        "offsetY": "60%",
        "text": "Salicylic Acid, <span style=\"\">67%</span>",
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
        "offsetY": "40%",
        "text": "Fluoride, <span style=\"\">93%</span>",
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
        "offsetY": "20%",
        "text": "Zinc Oxide, <span style=\"\">56%</span>",
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

    "selectMarqueeFill": {
      "color": "#d3d3d3",
      "opacity": 0.4
    },
    "type": "circular",
    "fill": "#fff",
    "stroke": "none",
    "sweepAngle": 270,
    "data": [
      chartdftwo
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
      },
    #   {
    #     "enabled": True,
    #     "zIndex": 5,
    #     "fill": "#ef6c00",
    #     "stroke": "none",
    #     "hatchFill": "none",
    #     "axisIndex": 0,
    #     "dataIndex": 2,
    #     "position": "center",
    #     "width": "17%",
    #     "radius": "60%"
    #   },
    #   {
    #     "enabled": True,
    #     "zIndex": 5,
    #     "fill": "#ffd54f",
    #     "stroke": "none",
    #     "hatchFill": "none",
    #     "axisIndex": 0,
    #     "dataIndex": 3,
    #     "position": "center",
    #     "width": "17%",
    #     "radius": "40%"
    #   },
    #   {
    #     "enabled": True,
    #     "zIndex": 5,
    #     "fill": "#455a64",
    #     "stroke": "none",
    #     "hatchFill": "none",
    #     "axisIndex": 0,
    #     "dataIndex": 4,
    #     "position": "center",
    #     "width": "17%",
    #     "radius": "20%"
    #   },
    #   {
    #     "enabled": True,
    #     "zIndex": 4,
    #     "fill": "#F5F4F4",
    #     "stroke": "none",
    #     "hatchFill": "none",
    #     "axisIndex": 0,
    #     "dataIndex": 5,
    #     "position": "center",
    #     "width": "17%",
    #     "radius": "100%"
    #   },
    #   {
    #     "enabled": True,
    #     "zIndex": 4,
    #     "fill": "#F5F4F4",
    #     "stroke": "none",
    #     "hatchFill": "none",
    #     "axisIndex": 0,
    #     "dataIndex": 5,
    #     "position": "center",
    #     "width": "17%",
    #     "radius": "80%"
    #   },
    #   {
    #     "enabled": True,
    #     "zIndex": 4,
    #     "fill": "#F5F4F4",
    #     "stroke": "none",
    #     "hatchFill": "none",
    #     "axisIndex": 0,
    #     "dataIndex": 5,
    #     "position": "center",
    #     "width": "17%",
    #     "radius": "60%"
    #   },
    #   {
    #     "enabled": True,
    #     "zIndex": 4,
    #     "fill": "#F5F4F4",
    #     "stroke": "none",
    #     "hatchFill": "none",
    #     "axisIndex": 0,
    #     "dataIndex": 5,
    #     "position": "center",
    #     "width": "17%",
    #     "radius": "40%"
    #   },
    #   {
    #     "enabled": True,
    #     "zIndex": 4,
    #     "fill": "#F5F4F4",
    #     "stroke": "none",
    #     "hatchFill": "none",
    #     "axisIndex": 0,
    #     "dataIndex": 5,
    #     "position": "center",
    #     "width": "17%",
    #     "radius": "20%"
    #   }
     ]
  }

}

    chartjson = pickle.dumps(chart)
    return chartjson

