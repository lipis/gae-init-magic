$ ->
  init_common()
  hljs.initHighlightingOnLoad()

  $('#icon').selectize
    sortField: 'text'
    render:
      item: (item, escape) ->
        return "<div> <i class='fa fa-#{item.value} fa-fw'></i> #{item.text}</div>"

      option: (item, escape) ->
        "<div> <i class='fa fa-#{item.value} fa-fw'></i> #{item.text}</div>"


$ -> $('html.auth').each ->
  init_auth()

$ -> $('html.user-list').each ->
  init_user_list()

$ -> $('html.user-merge').each ->
  init_user_merge()

$ -> $('html.model-view').each ->
  init_model_view()

$ -> $('html.project-update').each ->
  init_project_update()

$ -> $('html.model-update').each ->
  init_model_update()

$ -> $('html.property-update').each ->
  init_property_update()
