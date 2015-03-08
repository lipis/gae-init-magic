&#35; coding: utf-8

from google.appengine.ext import ndb
from flask.ext import restful
import flask

from api import helpers
import auth
import model
import util

from main import api


{% raw -%}
###############################################################################
# Admin
###############################################################################
{%- endraw %}
@api.resource('/api/admin/v1/{{model_db.variable_plural_name}}/', endpoint='admin.api.{{model_db.variable_plural_name}}')
class Admin{{model_db.plural_name}}API(restful.Resource):
  @auth.admin_required
  def get(self):
    {{model_db.variable_name}}_keys = util.param('{{model_db.variable_name}}_keys', list)
    if {{model_db.variable_name}}_keys:
      {{model_db.variable_name}}_db_keys = [ndb.Key(urlsafe=k) for k in {{model_db.variable_name}}_keys]
      {{model_db.variable_name}}_dbs = ndb.get_multi({{model_db.variable_name}}_db_keys)
      return helpers.make_response({{model_db.variable_name}}_dbs, model.{{model_db.variable_name}}.FIELDS)

    {{model_db.variable_name}}_dbs, {{model_db.variable_name}}_cursor = model.{{model_db.name}}.get_dbs()
    return helpers.make_response({{model_db.variable_name}}_dbs, model.{{model_db.name}}.FIELDS, {{model_db.variable_name}}_cursor)


@api.resource('/api/admin/v1/{{model_db.variable_name}}/&lt;string:{{model_db.variable_name}}_key&gt;/', endpoint='admin.api.{{model_db.variable_name}}')
class Admin{{model_db.name}}API(restful.Resource):
  @auth.admin_required
  def get(self, {{model_db.variable_name}}_key):
    {{model_db.variable_name}}_db = ndb.Key(urlsafe={{model_db.variable_name}}_key).get()
    if not {{model_db.variable_name}}_db:
      helpers.make_not_found_exception('{{model_db.variable_name}} %s not found' % {{model_db.variable_name}}_key)
    return helpers.make_response({{model_db.variable_name}}_db, model.{{model_db.name}}.FIELDS)
