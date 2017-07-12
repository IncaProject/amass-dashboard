"""
This file was generated with the custom dashboard management command, it
contains the two classes for the main dashboard and app index dashboard.
You can customize these classes as you want.

To activate your index dashboard add the following to your settings.py::

    ADMIN_TOOLS_INDEX_DASHBOARD = 'admin_tools_dashboard.CustomIndexDashboard'

And to activate the app index dashboard::

    ADMIN_TOOLS_APP_INDEX_DASHBOARD = \
        'admin_tools_dashboard.CustomAppIndexDashboard'
"""
from django.utils.translation import ugettext_lazy as _

from admin_tools.dashboard import (
    AppIndexDashboard,
    Dashboard,
    modules,
)

from . import conf


class CustomIndexDashboard(Dashboard):
    """Custom index dashboard."""

    columns = 3

    def init_with_context(self, context):
        # Foo
        self.children.append(
            modules.ModelList(
                _('Foo'),
                models=conf.foo_apps,
                collapsible=False,
                deletable=False
            )
        )

        # News
        self.children.append(
            modules.ModelList(
                _('News'),
                models=conf.news_apps,
                collapsible=False,
                deletable=False
            )
        )

        # Bookmarks
        self.children.append(
            modules.ModelList(
                _('Bookmarks'),
                models=conf.bookmark_apps,
                collapsible=False,
                deletable=False
            )
        )

        # Dash
        self.children.append(
            modules.ModelList(
                _('Dash'),
                models=conf.dash_apps,
                collapsible=False,
                deletable=False
            )
        )

        # Registration
        self.children.append(
            modules.ModelList(
                _('Registration'),
                models=conf.registration_apps,
                collapsible=False,
                deletable=False
            )
        )

        # Append an app list module for "Administration"
        self.children.append(
            modules.AppList(
                _('Administration'),
                models=['django.contrib.*'],
                collapsible=False,
                deletable=False
            )
        )

        # Append a recent actions module
        self.children.append(
            modules.RecentActions(_('Recent Actions'), 10)
        )


class CustomAppIndexDashboard(AppIndexDashboard):
    """Custom app index dashboard."""

    # We disable title because its redundant with the model list module
    title = ''

    def __init__(self, *args, **kwargs):
        AppIndexDashboard.__init__(self, *args, **kwargs)

        self.children.append(
            modules.RecentActions(
                _('Recent Actions'),
                include_list=self.get_app_content_types(),
                limit=10
            )
        )

    def init_with_context(self, context):
        """Use this method if you need to access the request context."""
        return super(CustomAppIndexDashboard, self).init_with_context(context)
