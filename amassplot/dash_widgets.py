from django.template.loader import render_to_string
from django.conf import settings
import sqlalchemy as sqa
import pandas as pd
import json

dataFetched = False
engine = None
conn = None

def doConnection():
    global dataFetched
    global engine
    global conn
    if (dataFetched == False):
        # This following line needs to be changed on production
        #engine = sqa.create_engine("mysql+pymysql://mysqluser:mysqluser@localhost/amass",
        #                           connect_args=dict(host='localhost', port=3306))
        # engine = sqa.create_engine("mysql+pymysql://ak1aiyer:mysqluser@ak1aiyer.mysql.pythonanywhere-services.com/ak1aiyer$amass",
        #                    connect_args=dict(host='ak1aiyer.mysql.pythonanywhere-services.com', port=3306))
        import ConfigParser

        config = ConfigParser.RawConfigParser()
        defaultFile = settings.DATABASES['default']['OPTIONS']['read_default_file']
        config.read(defaultFile)
        database = config.get('client', 'database')
        host = config.get('client', 'host')
        uid = config.get('client', 'user')
        pwd = config.get('client', 'password').replace("'","")

        connectstr = "mysql+pymysql://" + uid + ":" + pwd + "@" + host + "/" + database
        engine = sqa.create_engine(connectstr,connect_args=dict(host = host, port = 3306))
        conn = engine.connect()
        if (conn is None):
            raise ValueError("DBConnection could not be completed")
        else:
            dataFetched = True

from dash.base import BaseDashboardPluginWidget

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'

# *************************************************************
# ***************** Base chart widget *************************
# *************************************************************
#

class BaseChartWidget(BaseDashboardPluginWidget):
    """Base chart widget."""

    _template = None

    def render(self, request=None):
        """Render."""

        context = {
            'plugin': self.plugin,
            'width': self.get_width(),
            'height': self.get_height(),
            'STATIC_URL': settings.STATIC_URL,
        }

        return render_to_string(
            self._template,
            context
        )


class BaseACChart1Widget(BaseChartWidget):
    """Base piechart widget."""

    media_js = (
        '/anychart/anychart.min.js',
        '/anychart/dark_blue.min.js',
        '/js/chart1.js'
    )
    _template = 'amassplot/plugins/render_chart1.html'

    def render(self, request=None):
        doConnection()
        sqlstr = "SELECT TOOL_NAME as toolname, COUNT(*) as " \
            "count FROM amass_source_gateway_cipres GROUP BY  TOOL_NAME "
        gatewaycipres = pd.read_sql(sqlstr,conn)

        context = {
            'plugin': self.plugin,
            'width': self.get_width(),
            'height': self.get_height(),
            'STATIC_URL': settings.STATIC_URL,
        }
        context.update(self.getChartData(gatewaycipres))

        return render_to_string(
            self._template,
            context
        )

    def getChartData(self, df):
        chartjsonone = countPieChartJson(df, colnamex="toolname", charttitle="Tool Name(Cipres)",
                                         chartcontainerstr="container1")
        return {"chartDataOne": chartjsonone}


class BaseACChart2Widget(BaseChartWidget):

    media_js = (
        '/anychart/anychart.min.js',
        '/anychart/dark_blue.min.js',
        '/js/chart2.js'
    )
    _template = 'amassplot/plugins/render_chart2.html'

    def render(self, request=None):
        doConnection()
        sqlstr = "SELECT ERROR_MSG as errormsg, COUNT(*) as " \
            "count from amass_source_gateway_cipres " \
            "WHERE ERROR_MSG IS NOT NULL AND ERROR_MSG NOT IN ('Task has been deleted', 'Task has been deleted.') " \
            "group by errormsg ORDER BY count DESC LIMIT 10 "
        gatewayciprestwo = pd.read_sql(sqlstr,conn)

        context = {
            'plugin': self.plugin,
            'width': self.get_width(),
            'height': self.get_height(),
            'STATIC_URL': settings.STATIC_URL,
        }
        context.update(self.getChartDataTwo(gatewayciprestwo))

        return render_to_string(
            self._template,
            context
        )

    def getChartDataTwo(self, df):
        chartjsontwo = countPieChartJson(df, colnamex="errormsg", charttitle="Error Msg(Cipres)",
                                         chartcontainerstr="container2")
        return {"chartDataTwo": chartjsontwo}

class BaseACChart3Widget(BaseChartWidget):


    media_js = (
        '/anychart/anychart.min.js',
        '/anychart/dark_blue.min.js',
        '/js/chart3.js'
    )
    _template = 'amassplot/plugins/render_chart3.html'

    def render(self, request=None):
        doConnection()
        sqlstr = "SELECT TOOL_NAME as toolname, COUNT(*) as " \
            "count FROM amass_source_gateway_cipres GROUP BY  TOOL_NAME "
        gatewaycipresthree = pd.read_sql(sqlstr,conn)

        context = {
            'plugin': self.plugin,
            'width': self.get_width(),
            'height': self.get_height(),
            'STATIC_URL': settings.STATIC_URL,
        }
        context.update(self.getChartDataThree(gatewaycipresthree))

        return render_to_string(
            self._template,
            context
        )

    def getChartDataThree(self, df):
        chartjsonthree = countBarChartJson(df, colnamex="toolname", charttitle="Tool Name(Cipres)",
                                       charttitlex="Tool Name", charttitley="Count", chartcontainerstr="container3")
        return {"chartDataThree": chartjsonthree}

class BaseACChart4Widget(BaseChartWidget):

    media_js = (
        '/anychart/anychart.min.js',
        '/anychart/dark_blue.min.js',
        '/js/chart4.js'
    )
    _template = 'amassplot/plugins/render_chart4.html'

    def render(self, request=None):
        doConnection()
        sqlstr = "SELECT TOOL_NAME as toolname, COUNT(*) as " \
            "count FROM amass_source_gateway_cipres GROUP BY  TOOL_NAME "
        gatewaycipresfour = pd.read_sql(sqlstr,conn)

        context = {
            'plugin': self.plugin,
            'width': self.get_width(),
            'height': self.get_height(),
            'STATIC_URL': settings.STATIC_URL,
        }
        context.update(self.getChartDataFour(gatewaycipresfour))

        return render_to_string(
            self._template,
            context
        )

    def getChartDataFour(self, df):
        # Bar Vertical == Column
        chartjsonfour = countBarVerticalChartJson(df, colnamex="toolname", charttitle="Tool Name(Cipres)",
                                       charttitlex="Tool Name", charttitley="Count", chartcontainerstr="container4")
        return {"chartDataFour": chartjsonfour}

class BaseACChart5Widget(BaseChartWidget):

    media_js = (
        '/anychart/anychart.min.js',
        '/anychart/dark_blue.min.js',
        '/js/chart5.js'
    )
    _template = 'amassplot/plugins/render_chart5.html'

    def render(self, request=None):
        doConnection()
        sqlstr = "SELECT RESULT as result, COUNT(*) as sucessfailjobs from amass_source_gateway_cipres " \
            "WHERE RESOURCE = 'comet' " \
            "GROUP BY RESULT " \
            "ORDER BY RESULT "
        gatewaycipresfive = pd.read_sql(sqlstr,conn)

        context = {
            'plugin': self.plugin,
            'width': self.get_width(),
            'height': self.get_height(),
            'STATIC_URL': settings.STATIC_URL,
        }
        context.update(self.getChartDataFive(gatewaycipresfive))

        return render_to_string(
            self._template,
            context
        )

    def getChartDataFive(self, df):
        chartjsonfive = countDonutChart(df, colnamex="result", charttitle="RESULT of Successful/Failed Jobs(Comet)", chartcontainerstr="container5")
        return {"chartDataFive": chartjsonfive}

class BaseACChart6Widget(BaseChartWidget):

    media_js = (
        '/anychart/anychart.min.js',
        '/anychart/dark_blue.min.js',
        '/js/chart6.js'
    )
    _template = 'amassplot/plugins/render_chart6.html'

    def render(self, request=None):
        doConnection()
        sqlstr = "SELECT RESOURCE as resource, COUNT(*) as " \
            "count FROM amass_source_gateway_cipres GROUP BY  RESOURCE "
        gatewaycipressix = pd.read_sql(sqlstr, conn)

        context = {
            'plugin': self.plugin,
            'width': self.get_width(),
            'height': self.get_height(),
            'STATIC_URL': settings.STATIC_URL,
        }
        context.update(self.getChartDataSix(gatewaycipressix))

        return render_to_string(
            self._template,
            context
        )

    def getChartDataSix(self, df):
        chartjsonsix = countColumnChart(df, colnamex="resource", charttitle="CIPRES", charttitlex="Resources", charttitley="Number of Jobs", chartcontainerstr="container6")
        return {"chartDataSix": chartjsonsix}



class BaseACChart7Widget(BaseChartWidget):

    media_js = (
        '/anychart/anychart.min.js',
        '/anychart/dark_blue.min.js',
        '/js/chart7.js'
    )
    _template = 'amassplot/plugins/render_chart7.html'


    def render(self, request=None):
        doConnection()
        sqlstr = "SELECT RESOURCE as resource, TIMESTAMPDIFF(MINUTE , USER_SUBMIT_DATE, TERMINATE_DATE)  as turnaroundtime " \
            "from amass_source_gateway_cipres where RESOURCE = 'comet' "
        sqlstrtwo = "SELECT RESOURCE as resource, TIMESTAMPDIFF(MINUTE , USER_SUBMIT_DATE, TERMINATE_DATE)  as turnaroundtime " \
                 "from amass_source_gateway_cipres where RESOURCE = 'gordon' "
        gatewaycipresseven = pd.read_sql(sqlstr,conn)
        gatewayciressevenrev = pd.read_sql(sqlstrtwo,conn)

        context = {
            'plugin': self.plugin,
            'width': self.get_width(),
            'height': self.get_height(),
            'STATIC_URL': settings.STATIC_URL,
        }
        context.update(self.getChartDataSeven(gatewaycipresseven, gatewayciressevenrev))

        return render_to_string(
            self._template,
            context
        )

    def getChartDataSeven(self, df, dft):
        chartjsonseven = radarChart(df, dft, colnamex="turnaroundtime", charttitle="Turnaround Times for Cipres(Minutes)", chartcontainerstr="container7")
        return {"chartDataSeven": chartjsonseven}

class BaseACChart8Widget(BaseChartWidget):

    media_js = (
        '/anychart/anychart.min.js',
        '/anychart/dark_blue.min.js',
        '/js/chart8.js'
    )
    _template = 'amassplot/plugins/render_chart8.html'

    def render(self, request=None):
        doConnection()
        sqlstr = "SELECT RESULT as result, COUNT(*) as sucessfailjobs " \
            "from amass_source_gateway_cipres where RESULT = 1 group by RESOURCE"
        sqlstrtwo = "SELECT RESULT as result, COUNT(*) as sucessfailjobs " \
                 "from amass_source_gateway_cipres where RESULT = 0 group by RESOURCE"
        gatewaycipreseight = pd.read_sql(sqlstr,conn)
        gatewaycireseightrev = pd.read_sql(sqlstrtwo,conn)

        context = {
            'plugin': self.plugin,
            'width': self.get_width(),
            'height': self.get_height(),
            'STATIC_URL': settings.STATIC_URL,
        }
        context.update(self.getChartDataEight(gatewaycipreseight, gatewaycireseightrev))

        return render_to_string(
            self._template,
            context
        )

    def getChartDataEight(self, df, dft):
        chartjsoneight = gaugeChart(df, dft, colnamex="result", charttitle="Success Rates for Jobs(Cipres)", chartcontainerstr="container8")
        return {"chartDataEight": chartjsoneight}


class BaseACChart9Widget(BaseChartWidget):

    media_js = (
        '/anychart/anychart.min.js',
        '/anychart/dark_blue.min.js',
        '/js/chart9.js'
    )
    _template = 'amassplot/plugins/render_chart9.html'

    def render(self, request=None):
        doConnection()
        sqlstr = "SELECT RESULT as result, COUNT(*) as sucessfailjobs from amass_source_gateway_cipres " \
                 "WHERE RESOURCE = 'gordon' " \
                 "GROUP BY RESULT " \
                 "ORDER BY RESULT "
        gatewaycipresnine = pd.read_sql(sqlstr, conn)

        context = {
            'plugin': self.plugin,
            'width': self.get_width(),
            'height': self.get_height(),
            'STATIC_URL': settings.STATIC_URL,
        }
        context.update(self.getChartDataNine(gatewaycipresnine))

        return render_to_string(
            self._template,
            context
        )

    def getChartDataNine(self, df):
        chartjsonnine = countDonutTwoChart(df, colnamex="result", charttitle="RESULT of Successful/Failed Jobs(Gordon)", chartcontainerstr="container9")
        return {"chartDataNine": chartjsonnine}
    
class BaseACChart10Widget(BaseChartWidget):
    """Base piechart widget."""

    media_js = (
        '/anychart/anychart.min.js',
        '/anychart/dark_blue.min.js',
        '/js/chart10.js'
    )
    _template = 'amassplot/plugins/render_chart10.html'

    def render(self, request=None):
        doConnection()
        sqlstr = "SELECT TOOL_NAME as toolname, COUNT(*) as " \
            "count FROM amass_source_gateway_nsg GROUP BY  TOOL_NAME "
        gatewaycipres = pd.read_sql(sqlstr,conn)

        context = {
            'plugin': self.plugin,
            'width': self.get_width(),
            'height': self.get_height(),
            'STATIC_URL': settings.STATIC_URL,
        }
        context.update(self.getChartDataTen(gatewaycipres))

        return render_to_string(
            self._template,
            context
        )

    def getChartDataTen(self, df):
        doConnection()
        chartjsonten = countPieChartJson(df, colnamex="toolname", charttitle="Tool Name(NSG)",
                                         chartcontainerstr="container10")
        return {"chartDataTen": chartjsonten}


class BaseACChart11Widget(BaseChartWidget):

    media_js = (
        '/anychart/anychart.min.js',
        '/anychart/dark_blue.min.js',
        '/js/chart11.js'
    )
    _template = 'amassplot/plugins/render_chart11.html'

    def render(self, request=None):
        doConnection()
        sqlstr = "SELECT ERROR_MSG as errormsg, COUNT(*) as " \
            "count from amass_source_gateway_nsg " \
            "WHERE ERROR_MSG IS NOT NULL AND ERROR_MSG NOT IN ('Task has been deleted', 'Task has been deleted.') " \
            "group by errormsg ORDER BY count DESC LIMIT 10 "
        gatewayciprestwo = pd.read_sql(sqlstr,conn)

        context = {
            'plugin': self.plugin,
            'width': self.get_width(),
            'height': self.get_height(),
            'STATIC_URL': settings.STATIC_URL,
        }
        context.update(self.getChartDataEleven(gatewayciprestwo))

        return render_to_string(
            self._template,
            context
        )

    def getChartDataEleven(self, df):
        chartjsoneleven = countPieChartJson(df, colnamex="errormsg", charttitle="Error Msg(NSG)",
                                         chartcontainerstr="container11")
        return {"chartDataEleven": chartjsoneleven}

class BaseACChart12Widget(BaseChartWidget):


    media_js = (
        '/anychart/anychart.min.js',
        '/anychart/dark_blue.min.js',
        '/js/chart12.js'
    )
    _template = 'amassplot/plugins/render_chart12.html'

    def render(self, request=None):
        doConnection()
        sqlstr = "SELECT TOOL_NAME as toolname, COUNT(*) as " \
            "count FROM amass_source_gateway_nsg GROUP BY  TOOL_NAME "
        gatewaycipresthree = pd.read_sql(sqlstr,conn)

        context = {
            'plugin': self.plugin,
            'width': self.get_width(),
            'height': self.get_height(),
            'STATIC_URL': settings.STATIC_URL,
        }
        context.update(self.getChartDataTwelve(gatewaycipresthree))

        return render_to_string(
            self._template,
            context
        )

    def getChartDataTwelve(self, df):
        chartjsontwelve = countBarChartJson(df, colnamex="toolname", charttitle="Tool Name(NSG)",
                                       charttitlex="Tool Name", charttitley="Count", chartcontainerstr="container12")
        return {"chartDataTwelve": chartjsontwelve}

class BaseACChart13Widget(BaseChartWidget):

    media_js = (
        '/anychart/anychart.min.js',
        '/anychart/dark_blue.min.js',
        '/js/chart13.js'
    )
    _template = 'amassplot/plugins/render_chart13.html'

    def render(self, request=None):
        doConnection()
        sqlstr = "SELECT TOOL_NAME as toolname, COUNT(*) as " \
            "count FROM amass_source_gateway_nsg GROUP BY  TOOL_NAME "
        gatewaycipresfour = pd.read_sql(sqlstr,conn)

        context = {
            'plugin': self.plugin,
            'width': self.get_width(),
            'height': self.get_height(),
            'STATIC_URL': settings.STATIC_URL,
        }
        context.update(self.getChartDataThirteen(gatewaycipresfour))

        return render_to_string(
            self._template,
            context
        )

    def getChartDataThirteen(self, df):
        # Bar Vertical == Column
        chartjsonthirteen = countBarVerticalChartJson(df, colnamex="toolname", charttitle="Tool Name(NSG)",
                                       charttitlex="Tool Name", charttitley="Count", chartcontainerstr="container13")
        return {"chartDataThirteen": chartjsonthirteen}

class BaseACChart14Widget(BaseChartWidget):

    media_js = (
        '/anychart/anychart.min.js',
        '/anychart/dark_blue.min.js',
        '/js/chart14.js'
    )
    _template = 'amassplot/plugins/render_chart14.html'

    def render(self, request=None):
        doConnection()
        sqlstr = "SELECT RESULT as result, COUNT(*) as sucessfailjobs from amass_source_gateway_nsg " \
            "WHERE RESOURCE = 'comet' " \
            "GROUP BY RESULT " \
            "ORDER BY RESULT "
        gatewaycipresfive = pd.read_sql(sqlstr,conn)

        context = {
            'plugin': self.plugin,
            'width': self.get_width(),
            'height': self.get_height(),
            'STATIC_URL': settings.STATIC_URL,
        }
        context.update(self.getChartDataFourteen(gatewaycipresfive))

        return render_to_string(
            self._template,
            context
        )

    def getChartDataFourteen(self, df):
        chartjsonfourteen = countDonutChart(df, colnamex="result", charttitle="RESULT of Successful/Failed Jobs(Comet)", chartcontainerstr="container14")
        return {"chartDataFourteen": chartjsonfourteen}

class BaseACChart15Widget(BaseChartWidget):

    media_js = (
        '/anychart/anychart.min.js',
        '/anychart/dark_blue.min.js',
        '/js/chart15.js'
    )
    _template = 'amassplot/plugins/render_chart15.html'

    def render(self, request=None):
        doConnection()
        sqlstr = "SELECT RESOURCE as resource, COUNT(*) as " \
            "count FROM amass_source_gateway_nsg GROUP BY RESOURCE "
        gatewaycipressix = pd.read_sql(sqlstr, conn)

        context = {
            'plugin': self.plugin,
            'width': self.get_width(),
            'height': self.get_height(),
            'STATIC_URL': settings.STATIC_URL,
        }
        context.update(self.getChartDataFifteen(gatewaycipressix))

        return render_to_string(
            self._template,
            context
        )

    def getChartDataFifteen(self, df):
        chartjsonfifteen = countColumnChart(df, colnamex="resource", charttitle="NSG", charttitlex="Resources", charttitley="Number of Jobs", chartcontainerstr="container15")
        return {"chartDataFifteen": chartjsonfifteen}



class BaseACChart16Widget(BaseChartWidget):

    media_js = (
        '/anychart/anychart.min.js',
        '/anychart/dark_blue.min.js',
        '/js/chart16.js'
    )
    _template = 'amassplot/plugins/render_chart16.html'


    def render(self, request=None):
        doConnection()
        sqlstr = "SELECT RESOURCE as resource, TIMESTAMPDIFF(MINUTE , USER_SUBMIT_DATE, TERMINATE_DATE)  as turnaroundtime " \
            "from amass_source_gateway_nsg where RESOURCE = 'comet' "
        sqlstrtwo = "SELECT RESOURCE as resource, TIMESTAMPDIFF(MINUTE , USER_SUBMIT_DATE, TERMINATE_DATE)  as turnaroundtime " \
                 "from amass_source_gateway_nsg where RESOURCE = 'stampede' "
        gatewaycipresseven = pd.read_sql(sqlstr,conn)
        gatewayciressevenrev = pd.read_sql(sqlstrtwo,conn)

        context = {
            'plugin': self.plugin,
            'width': self.get_width(),
            'height': self.get_height(),
            'STATIC_URL': settings.STATIC_URL,
        }
        context.update(self.getChartDataSixteen(gatewaycipresseven, gatewayciressevenrev))

        return render_to_string(
            self._template,
            context
        )

    def getChartDataSixteen(self, df, dft):
        chartjsonsixteen = radarChartTwo(df, dft, colnamex="turnaroundtime", charttitle="Turnaround Times for NSG(Minutes)", chartcontainerstr="container16")
        return {"chartDataSixteen": chartjsonsixteen}

class BaseACChart17Widget(BaseChartWidget):

    media_js = (
        '/anychart/anychart.min.js',
        '/anychart/dark_blue.min.js',
        '/js/chart17.js'
    )
    _template = 'amassplot/plugins/render_chart17.html'

    def render(self, request=None):
        doConnection()
        sqlstr = "SELECT RESULT as result, COUNT(*) as sucessfailjobs " \
            "from amass_source_gateway_nsg where RESULT = 1 group by RESOURCE"
        sqlstrtwo = "SELECT RESULT as result, COUNT(*) as sucessfailjobs " \
                 "from amass_source_gateway_nsg where RESULT = 0 group by RESOURCE"
        gatewaycipreseight = pd.read_sql(sqlstr,conn)
        gatewaycireseightrev = pd.read_sql(sqlstrtwo,conn)

        context = {
            'plugin': self.plugin,
            'width': self.get_width(),
            'height': self.get_height(),
            'STATIC_URL': settings.STATIC_URL,
        }
        context.update(self.getChartDataSeventeen(gatewaycipreseight, gatewaycireseightrev))

        return render_to_string(
            self._template,
            context
        )

    def getChartDataSeventeen(self, df, dft):
        chartjsoneseventeen = gaugeChartTwo(df, dft, colnamex="result", charttitle="Success Rates for NSG", chartcontainerstr="container17")
        return {"chartDataSeventeen": chartjsoneseventeen}


class BaseACChart18Widget(BaseChartWidget):

    media_js = (
        '/anychart/anychart.min.js',
        '/anychart/dark_blue.min.js',
        '/js/chart18.js'
    )
    _template = 'amassplot/plugins/render_chart18.html'

    def render(self, request=None):
        doConnection()
        sqlstr = "SELECT RESULT as result, COUNT(*) as sucessfailjobs from amass_source_gateway_nsg " \
                 "WHERE RESOURCE = 'stampede' " \
                 "GROUP BY RESULT " \
                 "ORDER BY RESULT "
        gatewaycipresnine = pd.read_sql(sqlstr, conn)

        context = {
            'plugin': self.plugin,
            'width': self.get_width(),
            'height': self.get_height(),
            'STATIC_URL': settings.STATIC_URL,
        }
        context.update(self.getChartDataEighteen(gatewaycipresnine))

        return render_to_string(
            self._template,
            context
        )

    def getChartDataEighteen(self, df):
        chartjsoneighteen = countDonutTwoChart(df, colnamex="result", charttitle="RESULT of Successful/Failed Jobs(Stampede)", chartcontainerstr="container18")
        return {"chartDataEighteen": chartjsoneighteen}
class BaseACChart19Widget(BaseChartWidget):

    media_js = (
        '/anychart/anychart.min.js',
        '/anychart/dark_blue.min.js',
        '/js/chart19.js'
    )
    _template = 'amassplot/plugins/render_chart19.html'

    def render(self, request=None):
        doConnection()
        sqlstr = "SELECT TARGET_RESOURCE as resource, COUNT(*) as " \
            "count FROM amass_source_gateway_inca GROUP BY TARGET_RESOURCE "
        gatewaycipressix = pd.read_sql(sqlstr, conn)

        context = {
            'plugin': self.plugin,
            'width': self.get_width(),
            'height': self.get_height(),
            'STATIC_URL': settings.STATIC_URL,
        }
        context.update(self.getChartDataNinteen(gatewaycipressix))

        return render_to_string(
            self._template,
            context
        )

    def getChartDataNinteen(self, df):
        chartjsonninteen = countColumnChart(df, colnamex="resource", charttitle="INCA", charttitlex="Resources", charttitley="Number of Jobs", chartcontainerstr="container19")
        return {"chartDataNineteen": chartjsonninteen}


class BaseACChart20Widget(BaseChartWidget):

    media_js = (
        '/anychart/anychart.min.js',
        '/anychart/dark_blue.min.js',
        '/js/chart20.js'
    )
    _template = 'amassplot/plugins/render_chart20.html'

    def render(self, request=None):
        doConnection()
        sqlstr = "SELECT RESULT as result, COUNT(*) as sucessfailjobs " \
            "from amass_source_gateway_inca where RESULT = 1 group by TARGET_RESOURCE"
        sqlstrtwo = "SELECT RESULT as result, COUNT(*) as sucessfailjobs " \
                 "from amass_source_gateway_inca where RESULT = 0 group by TARGET_RESOURCE"
        gatewaycipreseight = pd.read_sql(sqlstr,conn)
        gatewaycireseightrev = pd.read_sql(sqlstrtwo,conn)

        context = {
            'plugin': self.plugin,
            'width': self.get_width(),
            'height': self.get_height(),
            'STATIC_URL': settings.STATIC_URL,
        }
        context.update(self.getChartDataTwenty(gatewaycipreseight, gatewaycireseightrev))

        return render_to_string(
            self._template,
            context
        )

    def getChartDataTwenty(self, df, dft):
        chartjsonetwenty = gaugeChartThree(df, dft, colnamex="result", charttitle="Success Rates for INCA", chartcontainerstr="container20")
        return {"chartDataTwenty": chartjsonetwenty}



def countPieChartJson(chartdf, colnamex, charttitle, chartcontainerstr):
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
        "name": "Actual",
        "data":
         chartdataone,
        "xScale": 0,
        "yScale": 1,
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

def countDonutChart(chartdf, colnamex, charttitle, chartcontainerstr):
    chartdataone = chartdf.values.tolist()

    chart = {
        "chart": {
        "enabled": True,
            "container": chartcontainerstr,
        "title": {

          "enabled": True,
            "text": charttitle,

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
    a = chartdfthree[colnamex]
    b = chartdffour[colnamex]
    c = chartdfthree[colnamex].mean()
    d = chartdfthree[colnamex].median()
    e = chartdfthree[colnamex].std()
    f = chartdfthree[colnamex].max()
    g = chartdfthree[colnamex].min()
    h = chartdffour[colnamex].mean()
    i = chartdffour[colnamex].median()
    j = chartdffour[colnamex].std()
    k = chartdffour[colnamex].max()
    l = chartdffour[colnamex].min()
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
        "name": "Gordon",
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
        "maximum": 14641,
        "minimum": 0,
        "ticks": {
          "mode": "logarithmic"
        },
        "minorTicks": {
          "mode": "logarithmic"
        },
        "logBase": 11
      }
    ],
    "type": "radar"
  }
    }
    chartjson = json.dumps(chart)
    return chartjson

def gaugeChart(chartdffive, chartdfsix, colnamex, charttitle, chartcontainerstr):
    a = int((chartdffive.values[0][1]).sum())
    b = int((chartdffive.values[1][1]).sum())
    x = float(int(((chartdffive.values[0][1]).sum() + ((chartdfsix.values[0][1]).sum()))))
    y = float(int(((chartdffive.values[1][1]).sum() + ((chartdfsix.values[1][1]).sum()))))
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
        "bottom": 0
      },
      "padding": {
        "left": 0,
        "top": 0,
        "bottom": 0,
        "right": 0
      }
    },
    "margin": {
      "left": 0,
      "top": 0,
      "bottom": 0,
      "right": 0
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
          "left": 0,
          "top": 0,
          "bottom": 0,
          "right": 20
        },
        "height": "8.5%",
        "anchor": "rightCenter",
        "offsetX": 0,
        "offsetY": "100%",
        "text": "Comet, <span style=\"\">93.5%</span>",
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
          "left": 0,
          "top": 0,
          "bottom": 0,
          "right": 20
        },
        "height": "8.5%",
        "anchor": "rightCenter",
        "offsetX": 0,
        "offsetY": "80%",
        "text": "Gordon, <span style=\"\">93.9%</span>",
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
    chartdataone = chartdfseven.values.tolist()

    chart = {
        "chart": {
        "enabled": True,
            "container": chartcontainerstr,
        "title": {

          "enabled": True,
            "text": charttitle,

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

def gaugeChartTwo(chartdffive, chartdfsix, colnamex, charttitle, chartcontainerstr):
    a = int((chartdffive.values[0][1]).sum())
    b = int((chartdffive.values[1][1]).sum())
    x = float(int(((chartdffive.values[0][1]).sum() + ((chartdfsix.values[0][1]).sum()))))
    y = float(int(((chartdffive.values[1][1]).sum() + ((chartdfsix.values[1][1]).sum()))))
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
        "bottom": 0
      },
      "padding": {
        "left": 0,
        "top": 0,
        "bottom": 0,
        "right": 0
      }
    },
    "margin": {
      "left": 0,
      "top": 0,
      "bottom": 0,
      "right": 0
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
          "left": 0,
          "top": 0,
          "bottom": 0,
          "right": 20
        },
        "height": "8.5%",
        "anchor": "rightCenter",
        "offsetX": 0,
        "offsetY": "100%",
        "text": "Comet, <span style=\"\">82.4%</span>",
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
          "left": 0,
          "top": 0,
          "bottom": 0,
          "right": 20
        },
        "height": "8.5%",
        "anchor": "rightCenter",
        "offsetX": 0,
        "offsetY": "80%",
        "text": "Stampede, <span style=\"\">77.3%</span>",
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

def radarChartTwo(chartdfthree, chartdffour, colnamex, charttitle, chartcontainerstr):
    a = chartdfthree[colnamex]
    b = chartdffour[colnamex]
    c = chartdfthree[colnamex].mean()
    d = chartdfthree[colnamex].median()
    e = chartdfthree[colnamex].std()
    f = chartdfthree[colnamex].max()
    g = chartdfthree[colnamex].min()
    h = chartdffour[colnamex].mean()
    i = chartdffour[colnamex].median()
    j = chartdffour[colnamex].std()
    k = chartdffour[colnamex].max()
    l = chartdffour[colnamex].min()
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
        "name": "Stampede",
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
        "maximum": 4356,
        "minimum": 0,
        "ticks": {
          "mode": "logarithmic"
        },
        "minorTicks": {
          "mode": "logarithmic"
        },
        "logBase": 66
      }
    ],
    "type": "radar"
  }
    }
    chartjson = json.dumps(chart)
    return chartjson
def gaugeChartThree(chartdffive, chartdfsix, colnamex, charttitle, chartcontainerstr):
    a = int((chartdffive.values[0][1]).sum())
    b = int((chartdffive.values[1][1]).sum())
    c = int((chartdffive.values[2][1]).sum())
    x = float(int(((chartdffive.values[0][1]).sum() + ((chartdfsix.values[0][1]).sum()))))
    y = float(int(((chartdffive.values[1][1]).sum() + ((chartdfsix.values[1][1]).sum()))))
    z = float(int(((chartdffive.values[2][1]).sum() + ((chartdfsix.values[2][1]).sum()))))
    e = (a / x) * 100
    f = (b / y) * 100
    g = (c / z) * 100

    chart = {"gauge": {
    "enabled": True,
    "container": chartcontainerstr,
    "title": {
      "enabled": True,
      "useHtml": True,
      "text": charttitle,
      "margin": {
        "bottom": 0
      },
      "padding": {
        "left": 0,
        "top": 0,
        "bottom": 0,
        "right": 0
      }
    },
    "margin": {
      "left": 0,
      "top": 0,
      "bottom": 0,
      "right": 0
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
          "left": 0,
          "top": 0,
          "bottom": 0,
          "right": 20
        },
        "height": "8.5%",
        "anchor": "rightCenter",
        "offsetX": 0,
        "offsetY": "100%",
        "text": "Comet, <span style=\"\">98.8%</span>",
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
          "left": 0,
          "top": 0,
          "bottom": 0,
          "right": 20
        },
        "height": "8.5%",
        "anchor": "rightCenter",
        "offsetX": 0,
        "offsetY": "80%",
        "text": "Gordon, <span style=\"\">91.9%</span>",
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
                "left": 0,
                "top": 0,
                "bottom": 0,
                "right": 20
            },
            "height": "8.5%",
            "anchor": "rightCenter",
            "offsetX": 0,
            "offsetY": "60%",
            "text": "Trestles, <span style=\"\">55.1%</span>",
            "minFontSize": 8,
            "maxFontSize": 72,
            "adjustFontSize": {
                "width": False,
                "height": False
            },
            "rotation": 0,
            "position": "leftTop"
        },
    #     {
    #
    #     "enabled": True,
    #     "zIndex": 50,
    #     "fontSize": 13,
    #     "fontFamily": "Verdana, Helvetica, Arial, sans-serif",
    #     "fontColor": "#7c868e",
    #     "fontOpacity": 1,
    #     "fontDecoration": "none",
    #     "fontStyle": "normal",
    #     "fontVariant": "normal",
    #     "fontWeight": "normal",
    #     "letterSpacing": "normal",
    #     "textDirection": "ltr",
    #     "lineHeight": "normal",
    #     "textIndent": 0,
    #     "vAlign": "middle",
    #     "hAlign": "center",
    #     "textWrap": "byLetter",
    #     "textOverflow": "",
    #     "selectable": False,
    #     "disablePointerEvents": False,
    #     "useHtml": True,
    #     "background": {
    #         "zIndex": 0,
    #         "enabled": False,
    #         "fill": "#ffffff",
    #         "stroke": "none",
    #         "disablePointerEvents": False,
    #         "cornerType": "round",
    #         "corners": 0
    #     },
    #     "padding": {
    #         "left": 0,
    #         "top": 0,
    #         "bottom": 0,
    #          "right": 20
    #     },
    #     "height": "8.5%",
    #     "anchor": "rightCenter",
    #     "offsetX": 0,
    #     "offsetY": "100%",
    #     "text": "Trestles, <span style=\"\">55.1%</span>",
    #     "minFontSize": 8,
    #     "maxFontSize": 72,
    #     "adjustFontSize": {
    #          "width": False,
    #         "height": False
    #     },
    #     "rotation": 0,
    #     "position": "leftTop"
    # }
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
      round(f,1),
      round(g,1)
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

      {
        "enabled": True,
        "zIndex": 5,
        "fill": "#ef6c00",
        "stroke": "none",
        "hatchFill": "none",
        "axisIndex": 0,
        "dataIndex": 2,
        "position": "center",
        "width": "17%",
        "radius": "60%"
      }
    ]
  }
}
    chartjson = json.dumps(chart)
    return chartjson

