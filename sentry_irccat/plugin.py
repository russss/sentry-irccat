import socket

from django import forms
from sentry.conf import settings
from sentry.plugins import Plugin
from sentry.plugins.bases.notify import NotificationPlugin, NotificationConfigurationForm
import sentry_irccat


class IRCCatConfigurationForm(NotificationConfigurationForm):
    host = forms.CharField(label='Host', required=False, help_text='irccat host')
    port = forms.IntegerField(label='Port', required=False, help_text='irccat port')
    channel = forms.CharField(label='Channel', required=False, help_text='channel')


class IRCCatMessage(Plugin):
    title = 'IRCCat'
    conf_key = 'irccat'
    slug = 'irccat'
    version = sentry_irccat.VERSION
    author = 'Russ Garrett'
    author_url = 'http://www.github.com/russss'
    project_conf_form = IRCCatConfigurationForm

    def is_configured(self, project):
        return all(self.get_option(k, project) for k in ('host', 'port', 'channel'))

    def post_process(self, group, event, is_new, is_sample, **kwargs):
        if not is_new or not self.is_configured(event.project):
            return
        link = '%s/%s/group/%d/' % (settings.URL_PREFIX, group.project.slug,
                                    group.id)
        message = '[sentry %s] %s (%s)' % (event.server_name, event.message, link)
        self.send_payload(event.project, message)

    def send_payload(self, project, message):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.get_option('host', project), self.get_option('port', project)))
        msg = "%s %s\r\n" % (self.get_option('channel', project), message)
        sock.send(msg)
        sock.close()

