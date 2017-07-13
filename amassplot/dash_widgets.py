from django.template.loader import render_to_string
from django.conf import settings

from dash.base import BaseDashboardPluginWidget

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'

# *************************************************************
# ***************** Base chart widget *************************
# *************************************************************


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
        'https://cdn.anychart.com/js/7.14.0/anychart-bundle.min.js',
        'https://cdn.anychart.com/themes/latest/dark_blue.min.js'
    )
    _template = 'amass/plugins/render_chart1.html'

class BaseACChart2Widget(BaseChartWidget):

    media_js = (
        'https://cdn.anychart.com/js/7.14.0/anychart-bundle.min.js',
        'https://cdn.anychart.com/themes/latest/dark_blue.min.js'
    )
    _template = 'amass/plugins/render_chart2.html'

class BaseACChart3Widget(BaseChartWidget):


    media_js = (
        'https://cdn.anychart.com/js/7.14.0/anychart-bundle.min.js',
        'https://cdn.anychart.com/themes/latest/dark_blue.min.js'
    )
    _template = 'amass/plugins/render_chart3.html'

class BaseACChart4Widget(BaseChartWidget):

    media_js = (
        'https://cdn.anychart.com/js/7.14.0/anychart-bundle.min.js',
        'https://cdn.anychart.com/themes/latest/dark_blue.min.js'
    )
    _template = 'amass/plugins/render_chart4.html'

class BaseACChart5Widget(BaseChartWidget):

    media_js = (
        'https://cdn.anychart.com/js/7.14.0/anychart-bundle.min.js',
        'https://cdn.anychart.com/themes/latest/dark_blue.min.js'
    )
    _template = 'amass/plugins/render_chart5.html'

class BaseACChart6Widget(BaseChartWidget):

    media_js = (
        'https://cdn.anychart.com/js/7.14.0/anychart-bundle.min.js',
        'https://cdn.anychart.com/themes/latest/dark_blue.min.js'
    )
    _template = 'amass/plugins/render_chart6.html'

class BaseACChart7Widget(BaseChartWidget):

    media_js = (
        'https://cdn.anychart.com/js/7.14.0/anychart-bundle.min.js',
        'https://cdn.anychart.com/themes/latest/dark_blue.min.js'
    )
    _template = 'amass/plugins/render_chart7.html'

class BaseACChart8Widget(BaseChartWidget):

    media_js = (
        'https://cdn.anychart.com/js/7.14.0/anychart-bundle.min.js',
        'https://cdn.anychart.com/themes/latest/dark_blue.min.js'
    )
    _template = 'amass/plugins/render_chart8.html'

class BaseACChart9Widget(BaseChartWidget):

    media_js = (
        'https://cdn.anychart.com/js/7.14.0/anychart-bundle.min.js',
        'https://cdn.anychart.com/themes/latest/dark_blue.min.js'
    )
    _template = 'amass/plugins/render_chart9.html'

