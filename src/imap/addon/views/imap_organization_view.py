# -*- coding: utf-8 -*-

# from imap.addon import _
from Products.Five.browser import BrowserView
from zope.interface import Interface

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class IImapOrganizationView(Interface):
    """ Marker Interface for IImapOrganizationView"""


class ImapOrganizationView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('imap_organization_view.pt')

    def __call__(self):
        # Implement your own actions:
        return self.index()
