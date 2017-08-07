from django.utils.translation import ugettext_lazy as _

from dash.base import BaseDashboardPlugin
from dash.factory import plugin_factory, plugin_widget_factory

from .dash_widgets import (
    BaseACChart1Widget, BaseACChart2Widget, BaseACChart3Widget, BaseACChart4Widget, BaseACChart5Widget,
BaseACChart6Widget, BaseACChart7Widget, BaseACChart8Widget, BaseACChart9Widget, BaseACChart10Widget, BaseACChart11Widget,
BaseACChart12Widget, BaseACChart13Widget, BaseACChart14Widget, BaseACChart15Widget, BaseACChart16Widget, BaseACChart17Widget, BaseACChart18Widget,
BaseACChart19Widget, BaseACChart20Widget
)
from .forms import *

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
    form = ChartForm1
    html_classes = ['chartonic']

class BaseChart2Plugin(BaseChartPlugin):
    """Base any chart plugin."""

    name = _("Chart2")
    html_classes = ['chartonic']

class BaseChart3Plugin(BaseChartPlugin):
    """Base any chart plugin."""

    name = _("Chart3")
    html_classes = ['chartonic']

class BaseChart4Plugin(BaseChartPlugin):
    """Base any chart plugin."""

    name = _("Chart4")
    html_classes = ['chartonic']

class BaseChart5Plugin(BaseChartPlugin):
    """Base any chart plugin."""

    name = _("Chart5")
    html_classes = ['chartonic']

class BaseChart6Plugin(BaseChartPlugin):
    """Base any chart plugin."""

    name = _("Chart6")
    html_classes = ['chartonic']

class BaseChart7Plugin(BaseChartPlugin):
    """Base any chart plugin."""

    name = _("Chart7")
    html_classes = ['chartonic']

class BaseChart8Plugin(BaseChartPlugin):
    """Base any chart plugin."""

    name = _("Chart8")
    html_classes = ['chartonic']

class BaseChart9Plugin(BaseChartPlugin):
    """Base any chart plugin."""

    name = _("Chart9")
    html_classes = ['chartonic']

class BaseChart10Plugin(BaseChartPlugin):
    """Base any chart plugin."""

    name = _("Chart10")
    html_classes = ['chartonic']

class BaseChart11Plugin(BaseChartPlugin):
    """Base any chart plugin."""

    name = _("Chart11")
    html_classes = ['chartonic']
class BaseChart12Plugin(BaseChartPlugin):
    """Base any chart plugin."""

    name = _("Chart12")
    html_classes = ['chartonic']

class BaseChart13Plugin(BaseChartPlugin):
    """Base any chart plugin."""

    name = _("Chart13")
    html_classes = ['chartonic']
class BaseChart14Plugin(BaseChartPlugin):
    """Base any chart plugin."""

    name = _("Chart14")
    html_classes = ['chartonic']
class BaseChart15Plugin(BaseChartPlugin):
    """Base any chart plugin."""

    name = _("Chart15")
    html_classes = ['chartonic']
class BaseChart16Plugin(BaseChartPlugin):
    """Base any chart plugin."""

    name = _("Chart16")
    html_classes = ['chartonic']
class BaseChart17Plugin(BaseChartPlugin):
    """Base any chart plugin."""

    name = _("Chart17")
    html_classes = ['chartonic']
class BaseChart18Plugin(BaseChartPlugin):
    """Base any chart plugin."""

    name = _("Chart18")
    html_classes = ['chartonic']

class BaseChart19Plugin(BaseChartPlugin):
    """Base any chart plugin."""

    name = _("Chart19")
    html_classes = ['chartonic']

class BaseChart20Plugin(BaseChartPlugin):
    """Base any chart plugin."""

    name = _("Chart20")
    html_classes = ['chartonic']


# *****************************************************************************
# ********** Generating and registering the plugins using factory *************
# *****************************************************************************


sizes = (
  # (4, 4),
    (5, 5),
    #(10, 10)
   # (6, 6),
    #(7, 7),
)

plugin_factory(BaseChart1Plugin,
               'Chart1',
               sizes)

plugin_factory(BaseChart2Plugin,
               'Chart2',
               sizes)

plugin_factory(BaseChart3Plugin,
               'Chart3',
               sizes)

plugin_factory(BaseChart4Plugin,
               'Chart4',
               sizes)

plugin_factory(BaseChart5Plugin,
               'Chart5',
               sizes)

plugin_factory(BaseChart6Plugin,
               'Chart6',
               sizes)

plugin_factory(BaseChart7Plugin,
               'Chart7',
               sizes)

plugin_factory(BaseChart8Plugin,
               'Chart8',
               sizes)

plugin_factory(BaseChart9Plugin,
               'Chart9',
               sizes)
plugin_factory(BaseChart10Plugin,
               'Chart10',
               sizes)
plugin_factory(BaseChart11Plugin,
               'Chart11',
               sizes)
plugin_factory(BaseChart12Plugin,
               'Chart12',
               sizes)
plugin_factory(BaseChart13Plugin,
               'Chart13',
               sizes)
plugin_factory(BaseChart14Plugin,
               'Chart14',
               sizes)
plugin_factory(BaseChart15Plugin,
               'Chart15',
               sizes)
plugin_factory(BaseChart16Plugin,
               'Chart16',
               sizes)
plugin_factory(BaseChart17Plugin,
               'Chart17',
               sizes)
plugin_factory(BaseChart18Plugin,
               'Chart18',
               sizes)

plugin_factory(BaseChart19Plugin,
               'Chart19',
               sizes)

plugin_factory(BaseChart20Plugin,
               'Chart20',
               sizes)



# *****************************************************************************
# ********************************* Registering widgets ***********************
# *****************************************************************************

# Registering chart plugin widgets

# Any Chart
plugin_widget_factory(BaseACChart1Widget,
                      'android',
                      'main',
                      'Chart1',
                      sizes)
plugin_widget_factory(BaseACChart1Widget,
                      'windows8',
                      'main',
                      'Chart1',
                      sizes)
plugin_widget_factory(BaseACChart1Widget,
                      'bootstrap2_fluid',
                      'main',
                      'Chart1',
                      sizes)
plugin_widget_factory(BaseACChart1Widget,
                      'example',
                      'main',
                      'Chart1',
                      sizes)

plugin_widget_factory(BaseACChart2Widget,
                      'android',
                      'main',
                      'Chart2',
                      sizes)
plugin_widget_factory(BaseACChart2Widget,
                      'windows8',
                      'main',
                      'Chart2',
                      sizes)
plugin_widget_factory(BaseACChart2Widget,
                      'bootstrap2_fluid',
                      'main',
                      'Chart2',
                      sizes)
plugin_widget_factory(BaseACChart2Widget,
                      'example',
                      'main',
                      'Chart2',
                      sizes)

plugin_widget_factory(BaseACChart3Widget,
                      'android',
                      'main',
                      'Chart3',
                      sizes)
plugin_widget_factory(BaseACChart3Widget,
                      'windows8',
                      'main',
                      'Chart3',
                      sizes)
plugin_widget_factory(BaseACChart3Widget,
                      'bootstrap2_fluid',
                      'main',
                      'Chart3',
                      sizes)

plugin_widget_factory(BaseACChart3Widget,
                      'example',
                      'main',
                      'Chart3',
                      sizes)

plugin_widget_factory(BaseACChart4Widget,
                      'android',
                      'main',
                      'Chart4',
                      sizes)
plugin_widget_factory(BaseACChart4Widget,
                      'windows8',
                      'main',
                      'Chart4',
                      sizes)
plugin_widget_factory(BaseACChart4Widget,
                      'bootstrap2_fluid',
                      'main',
                      'Chart4',
                      sizes)

plugin_widget_factory(BaseACChart4Widget,
                      'example',
                      'main',
                      'Chart4',
                      sizes)

plugin_widget_factory(BaseACChart5Widget,
                      'android',
                      'main',
                      'Chart5',
                      sizes)
plugin_widget_factory(BaseACChart5Widget,
                      'windows8',
                      'main',
                      'Chart5',
                      sizes)
plugin_widget_factory(BaseACChart5Widget,
                      'bootstrap2_fluid',
                      'main',
                      'Chart5',
                      sizes)

plugin_widget_factory(BaseACChart5Widget,
                      'example',
                      'main',
                      'Chart5',
                      sizes)

plugin_widget_factory(BaseACChart6Widget,
                      'android',
                      'main',
                      'Chart6',
                      sizes)
plugin_widget_factory(BaseACChart6Widget,
                      'windows8',
                      'main',
                      'Chart6',
                      sizes)
plugin_widget_factory(BaseACChart6Widget,
                      'bootstrap2_fluid',
                      'main',
                      'Chart6',
                      sizes)

plugin_widget_factory(BaseACChart6Widget,
                      'example',
                      'main',
                      'Chart6',
                      sizes)

plugin_widget_factory(BaseACChart7Widget,
                      'android',
                      'main',
                      'Chart7',
                      sizes)
plugin_widget_factory(BaseACChart7Widget,
                      'windows8',
                      'main',
                      'Chart7',
                      sizes)
plugin_widget_factory(BaseACChart7Widget,
                      'bootstrap2_fluid',
                      'main',
                      'Chart7',
                      sizes)
plugin_widget_factory(BaseACChart7Widget,
                      'example',
                      'main',
                      'Chart7',
                      sizes)

plugin_widget_factory(BaseACChart8Widget,
                      'android',
                      'main',
                      'Chart8',
                      sizes)
plugin_widget_factory(BaseACChart8Widget,
                      'windows8',
                      'main',
                      'Chart8',
                      sizes)
plugin_widget_factory(BaseACChart8Widget,
                      'bootstrap2_fluid',
                      'main',
                      'Chart8',
                      sizes)

plugin_widget_factory(BaseACChart8Widget,
                      'example',
                      'main',
                      'Chart8',
                      sizes)

plugin_widget_factory(BaseACChart9Widget,
                      'android',
                      'main',
                      'Chart9',
                      sizes)
plugin_widget_factory(BaseACChart9Widget,
                      'windows8',
                      'main',
                      'Chart9',
                      sizes)
plugin_widget_factory(BaseACChart9Widget,
                      'bootstrap2_fluid',
                      'main',
                      'Chart9',
                      sizes)

plugin_widget_factory(BaseACChart9Widget,
                      'example',
                      'main',
                      'Chart9',
                      sizes)
plugin_widget_factory(BaseACChart10Widget,
                      'android',
                      'main',
                      'Chart10',
                      sizes)
plugin_widget_factory(BaseACChart10Widget,
                      'windows8',
                      'main',
                      'Chart10',
                      sizes)
plugin_widget_factory(BaseACChart10Widget,
                      'bootstrap2_fluid',
                      'main',
                      'Chart10',
                      sizes)

plugin_widget_factory(BaseACChart10Widget,
                      'example',
                      'main',
                      'Chart10',
                      sizes)
plugin_widget_factory(BaseACChart11Widget,
                      'android',
                      'main',
                      'Chart11',
                      sizes)
plugin_widget_factory(BaseACChart11Widget,
                      'windows8',
                      'main',
                      'Chart11',
                      sizes)
plugin_widget_factory(BaseACChart11Widget,
                      'bootstrap2_fluid',
                      'main',
                      'Chart11',
                      sizes)

plugin_widget_factory(BaseACChart11Widget,
                      'example',
                      'main',
                      'Chart11',
                      sizes)
plugin_widget_factory(BaseACChart12Widget,
                      'android',
                      'main',
                      'Chart12',
                      sizes)
plugin_widget_factory(BaseACChart12Widget,
                      'windows8',
                      'main',
                      'Chart12',
                      sizes)
plugin_widget_factory(BaseACChart12Widget,
                      'bootstrap2_fluid',
                      'main',
                      'Chart12',
                      sizes)

plugin_widget_factory(BaseACChart12Widget,
                      'example',
                      'main',
                      'Chart12',
                      sizes)
plugin_widget_factory(BaseACChart13Widget,
                      'android',
                      'main',
                      'Chart13',
                      sizes)
plugin_widget_factory(BaseACChart13Widget,
                      'windows8',
                      'main',
                      'Chart13',
                      sizes)
plugin_widget_factory(BaseACChart13Widget,
                      'bootstrap2_fluid',
                      'main',
                      'Chart13',
                      sizes)

plugin_widget_factory(BaseACChart13Widget,
                      'example',
                      'main',
                      'Chart13',
                      sizes)
plugin_widget_factory(BaseACChart14Widget,
                      'android',
                      'main',
                      'Chart14',
                      sizes)
plugin_widget_factory(BaseACChart14Widget,
                      'windows8',
                      'main',
                      'Chart14',
                      sizes)
plugin_widget_factory(BaseACChart14Widget,
                      'bootstrap2_fluid',
                      'main',
                      'Chart14',
                      sizes)

plugin_widget_factory(BaseACChart14Widget,
                      'example',
                      'main',
                      'Chart14',
                      sizes)
plugin_widget_factory(BaseACChart15Widget,
                      'android',
                      'main',
                      'Chart15',
                      sizes)
plugin_widget_factory(BaseACChart15Widget,
                      'windows8',
                      'main',
                      'Chart15',
                      sizes)
plugin_widget_factory(BaseACChart15Widget,
                      'bootstrap2_fluid',
                      'main',
                      'Chart15',
                      sizes)

plugin_widget_factory(BaseACChart15Widget,
                      'example',
                      'main',
                      'Chart15',
                      sizes)
plugin_widget_factory(BaseACChart16Widget,
                      'android',
                      'main',
                      'Chart16',
                      sizes)
plugin_widget_factory(BaseACChart16Widget,
                      'windows8',
                      'main',
                      'Chart16',
                      sizes)
plugin_widget_factory(BaseACChart16Widget,
                      'bootstrap2_fluid',
                      'main',
                      'Chart16',
                      sizes)

plugin_widget_factory(BaseACChart16Widget,
                      'example',
                      'main',
                      'Chart16',
                      sizes)
plugin_widget_factory(BaseACChart17Widget,
                      'android',
                      'main',
                      'Chart17',
                      sizes)
plugin_widget_factory(BaseACChart17Widget,
                      'windows8',
                      'main',
                      'Chart17',
                      sizes)
plugin_widget_factory(BaseACChart17Widget,
                      'bootstrap2_fluid',
                      'main',
                      'Chart17',
                      sizes)

plugin_widget_factory(BaseACChart17Widget,
                      'example',
                      'main',
                      'Chart17',
                      sizes)
plugin_widget_factory(BaseACChart18Widget,
                      'android',
                      'main',
                      'Chart18',
                      sizes)
plugin_widget_factory(BaseACChart18Widget,
                      'windows8',
                      'main',
                      'Chart18',
                      sizes)
plugin_widget_factory(BaseACChart18Widget,
                      'bootstrap2_fluid',
                      'main',
                      'Chart18',
                      sizes)

plugin_widget_factory(BaseACChart18Widget,
                      'example',
                      'main',
                      'Chart18',
                      sizes)

plugin_widget_factory(BaseACChart19Widget,
                      'android',
                      'main',
                      'Chart19',
                      sizes)
plugin_widget_factory(BaseACChart19Widget,
                      'windows8',
                      'main',
                      'Chart19',
                      sizes)
plugin_widget_factory(BaseACChart19Widget,
                      'bootstrap2_fluid',
                      'main',
                      'Chart19',
                      sizes)

plugin_widget_factory(BaseACChart19Widget,
                      'example',
                      'main',
                      'Chart19',
                      sizes)
plugin_widget_factory(BaseACChart20Widget,
                      'android',
                      'main',
                      'Chart20',
                      sizes)
plugin_widget_factory(BaseACChart20Widget,
                      'windows8',
                      'main',
                      'Chart20',
                      sizes)
plugin_widget_factory(BaseACChart20Widget,
                      'bootstrap2_fluid',
                      'main',
                      'Chart20',
                      sizes)

plugin_widget_factory(BaseACChart20Widget,
                      'example',
                      'main',
                      'Chart20',
                      sizes)









