from django.utils.translation import ugettext_lazy as _

from dash.base import BaseDashboardPlugin
from dash.factory import plugin_factory, plugin_widget_factory

from .dash_widgets import (
    BaseACChart1Widget, BaseACChart2Widget, BaseACChart3Widget, BaseACChart4Widget, BaseACChart5Widget,
BaseACChart6Widget, BaseACChart7Widget, BaseACChart8Widget, BaseACChart9Widget
)
from .forms import ChartForm

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'

# *****************************************************************************
# *************************** Base chart plugin *******************************
# *****************************************************************************


class BaseChartPlugin(BaseDashboardPlugin):
    """Base chart plugin."""

    group = _("AnyChart plugins")
    form = ChartForm
    html_classes = ['chartonic']


class BaseChart1Plugin(BaseChartPlugin):
    """Base any chart plugin."""

    name = _("Chart1")
    html_classes = ['chartonic', 'any-chart-plugin']

class BaseChart2Plugin(BaseChartPlugin):
    """Base any chart plugin."""

    name = _("Chart2")
    html_classes = ['chartonic', 'any-chart-plugin']

class BaseChart3Plugin(BaseChartPlugin):
    """Base any chart plugin."""

    name = _("Chart3")
    html_classes = ['chartonic', 'any-chart-plugin']

class BaseChart4Plugin(BaseChartPlugin):
    """Base any chart plugin."""

    name = _("Chart4")
    html_classes = ['chartonic', 'any-chart-plugin']

class BaseChart5Plugin(BaseChartPlugin):
    """Base any chart plugin."""

    name = _("Chart5")
    html_classes = ['chartonic', 'any-chart-plugin']

class BaseChart6Plugin(BaseChartPlugin):
    """Base any chart plugin."""

    name = _("Chart6")
    html_classes = ['chartonic', 'any-chart-plugin']

class BaseChart7Plugin(BaseChartPlugin):
    """Base any chart plugin."""

    name = _("Chart7")
    html_classes = ['chartonic', 'any-chart-plugin']

class BaseChart8Plugin(BaseChartPlugin):
    """Base any chart plugin."""

    name = _("Chart8")
    html_classes = ['chartonic', 'any-chart-plugin']

class BaseChart9Plugin(BaseChartPlugin):
    """Base any chart plugin."""

    name = _("Chart9")
    html_classes = ['chartonic', 'any-chart-plugin']


# *****************************************************************************
# ********** Generating and registering the plugins using factory *************
# *****************************************************************************


sizes = (
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
)

plugin_factory(BaseChart1Plugin,
               'any_chart',
               sizes)

plugin_factory(BaseChart2Plugin,
               'any_chart',
               sizes)

plugin_factory(BaseChart3Plugin,
               'any_chart',
               sizes)

plugin_factory(BaseChart4Plugin,
               'any_chart',
               sizes)

plugin_factory(BaseChart5Plugin,
               'any_chart',
               sizes)

plugin_factory(BaseChart6Plugin,
               'any_chart',
               sizes)

plugin_factory(BaseChart7Plugin,
               'any_chart',
               sizes)

plugin_factory(BaseChart8Plugin,
               'any_chart',
               sizes)

plugin_factory(BaseChart9Plugin,
               'any_chart',
               sizes)


# *****************************************************************************
# ********************************* Registering widgets ***********************
# *****************************************************************************

# Registering chart plugin widgets

# Any Chart
plugin_widget_factory(BaseACChart1Widget,
                      'android',
                      'main',
                      'any_chart',
                      sizes)
plugin_widget_factory(BaseACChart1Widget,
                      'windows8',
                      'main',
                      'any_chart',
                      sizes)
plugin_widget_factory(BaseACChart1Widget,
                      'bootstrap2_fluid',
                      'main',
                      'any_chart',
                      sizes)

plugin_widget_factory(BaseACChart2Widget,
                      'android',
                      'main',
                      'any_chart',
                      sizes)
plugin_widget_factory(BaseACChart2Widget,
                      'windows8',
                      'main',
                      'any_chart',
                      sizes)
plugin_widget_factory(BaseACChart2Widget,
                      'bootstrap2_fluid',
                      'main',
                      'any_chart',
                      sizes)

plugin_widget_factory(BaseACChart3Widget,
                      'android',
                      'main',
                      'any_chart',
                      sizes)
plugin_widget_factory(BaseACChart3Widget,
                      'windows8',
                      'main',
                      'any_chart',
                      sizes)
plugin_widget_factory(BaseACChart3Widget,
                      'bootstrap2_fluid',
                      'main',
                      'any_chart',
                      sizes)

plugin_widget_factory(BaseACChart4Widget,
                      'android',
                      'main',
                      'any_chart',
                      sizes)
plugin_widget_factory(BaseACChart4Widget,
                      'windows8',
                      'main',
                      'any_chart',
                      sizes)
plugin_widget_factory(BaseACChart4Widget,
                      'bootstrap2_fluid',
                      'main',
                      'any_chart',
                      sizes)

plugin_widget_factory(BaseACChart5Widget,
                      'android',
                      'main',
                      'any_chart',
                      sizes)
plugin_widget_factory(BaseACChart5Widget,
                      'windows8',
                      'main',
                      'any_chart',
                      sizes)
plugin_widget_factory(BaseACChart5Widget,
                      'bootstrap2_fluid',
                      'main',
                      'any_chart',
                      sizes)

plugin_widget_factory(BaseACChart6Widget,
                      'android',
                      'main',
                      'any_chart',
                      sizes)
plugin_widget_factory(BaseACChart6Widget,
                      'windows8',
                      'main',
                      'any_chart',
                      sizes)
plugin_widget_factory(BaseACChart6Widget,
                      'bootstrap2_fluid',
                      'main',
                      'any_chart',
                      sizes)

plugin_widget_factory(BaseACChart7Widget,
                      'android',
                      'main',
                      'any_chart',
                      sizes)
plugin_widget_factory(BaseACChart7Widget,
                      'windows8',
                      'main',
                      'any_chart',
                      sizes)
plugin_widget_factory(BaseACChart7Widget,
                      'bootstrap2_fluid',
                      'main',
                      'any_chart',
                      sizes)

plugin_widget_factory(BaseACChart8Widget,
                      'android',
                      'main',
                      'any_chart',
                      sizes)
plugin_widget_factory(BaseACChart8Widget,
                      'windows8',
                      'main',
                      'any_chart',
                      sizes)
plugin_widget_factory(BaseACChart8Widget,
                      'bootstrap2_fluid',
                      'main',
                      'any_chart',
                      sizes)

plugin_widget_factory(BaseACChart9Widget,
                      'android',
                      'main',
                      'any_chart',
                      sizes)
plugin_widget_factory(BaseACChart9Widget,
                      'windows8',
                      'main',
                      'any_chart',
                      sizes)
plugin_widget_factory(BaseACChart9Widget,
                      'bootstrap2_fluid',
                      'main',
                      'any_chart',
                      sizes)










