#
# coding=utf-8

from . import hr as hr_bp
from .main import Main
from .apply import Apply


def register_api(view, endpoint, url, pk='id', pk_type='string'):
    """ flask official recommend / and /<> method

    :param view: view function
    :param endpoint: endpoint
    :param url: url
    :param pk: 变量
    :param pk_type: 变量类型
    :return:
    """
    view_func = view.as_view(endpoint)
    hr_bp.add_url_rule(url, defaults={pk: None}, view_func=view_func, methods=['GET', ])
    hr_bp.add_url_rule('%s/<%s:%s>' % (url, pk_type, pk), view_func=view_func, methods=['GET', 'POST'])


hr_bp.add_url_rule('/', view_func=Main.as_view('main'), methods=['GET'])
register_api(Apply, 'apply', '/apply', pk='method')
