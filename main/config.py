# coding: utf-8

import os

PRODUCTION = os.environ.get('SERVER_SOFTWARE', '').startswith('Google App Eng')
DEBUG = DEVELOPMENT = not PRODUCTION

try:
  # This part is surrounded in try/except because the config.py file is
  # also used in the run.py script which is used to compile/minify the client
  # side files (*.less, *.coffee, *.js) and is not aware of the GAE
  from google.appengine.api import app_identity

  APPLICATION_ID = app_identity.get_application_id()
except (ImportError, AttributeError):
  pass
else:
  from datetime import datetime

  CURRENT_VERSION_ID = os.environ.get('CURRENT_VERSION_ID')
  CURRENT_VERSION_NAME = CURRENT_VERSION_ID.split('.')[0]
  CURRENT_VERSION_TIMESTAMP = long(CURRENT_VERSION_ID.split('.')[1]) >> 28
  if DEVELOPMENT:
    import calendar

    CURRENT_VERSION_TIMESTAMP = calendar.timegm(datetime.utcnow().timetuple())
  CURRENT_VERSION_DATE = datetime.utcfromtimestamp(CURRENT_VERSION_TIMESTAMP)
  USER_AGENT = '%s/%s' % (APPLICATION_ID, CURRENT_VERSION_ID)

  import model

  CONFIG_DB = model.Config.get_master_db()
  SECRET_KEY = CONFIG_DB.flask_secret_key.encode('ascii')
  RECAPTCHA_PUBLIC_KEY = CONFIG_DB.recaptcha_public_key
  RECAPTCHA_PRIVATE_KEY = CONFIG_DB.recaptcha_private_key
  RECAPTCHA_LIMIT = 8

DEFAULT_DB_LIMIT = 64
MAX_DB_LIMIT = 1024
SIGNIN_RETRY_LIMIT = 4
TAG_SEPARATOR = ' '


###############################################################################
# Properties
###############################################################################
GENERIC_PROPERIES = [
    ('', '-'),
    ('boolean', 'Boolean'),
    ('computed', 'Computed'),
    ('date', 'Date'),
    ('datetime', 'DateTime'),
    ('float', 'Float'),
    ('integer', 'Integer'),
    ('json', 'JSON'),
    ('key', 'Key'),
    ('string', 'String (single-line)'),
    ('string_text', 'String (multi-line)'),
    ('string_tags', 'String (tags)'),
    ('text', 'Text (long)'),
  ]


NDB_PROPERIES = [
    ('', '-'),
    ('ndb.BlobKeyProperty', 'BlobKeyProperty'),
    ('ndb.BlobProperty', 'BlobProperty'),
    ('ndb.BooleanProperty', 'BooleanProperty'),
    ('ndb.ComputedProperty', 'ComputedProperty'),
    ('ndb.DateProperty', 'DateProperty'),
    ('ndb.DateTimeProperty', 'DateTimeProperty'),
    ('ndb.FloatProperty', 'FloatProperty'),
    ('ndb.GenericProperty', 'GenericProperty'),
    ('ndb.GeoPtProperty', 'GeoPtProperty'),
    ('ndb.IntegerProperty', 'IntegerProperty'),
    ('ndb.JsonProperty', 'JsonProperty'),
    ('ndb.KeyProperty', 'KeyProperty'),
    ('ndb.LocalStructuredProperty', 'LocalStructuredProperty'),
    ('ndb.PickleProperty', 'PickleProperty'),
    ('ndb.StringProperty', 'StringProperty'),
    ('ndb.StructuredProperty', 'StructuredProperty'),
    ('ndb.TextProperty', 'TextProperty'),
    ('ndb.TimeProperty', 'TimeProperty'),
    ('ndb.UserProperty', 'UserProperty'),
  ]

FIELD_PROPERIES = [
    ('', '-'),
    ('fields.Arbitrary', 'Arbitrary'),
    ('fields.Blob', 'Blob'),
    ('fields.BlobKey', 'BlobKey'),
    ('fields.Boolean', 'Boolean'),
    ('fields.DateTime', 'DateTime'),
    ('fields.Fixed', 'Fixed'),
    ('fields.Float', 'Float'),
    ('fields.FormattedString', 'FormattedString'),
    ('fields.GeoPt', 'GeoPt'),
    ('fields.Id', 'Id'),
    ('fields.Integer', 'Integer'),
    ('fields.Key', 'Key'),
    ('fields.List', 'List'),
    ('fields.Nested', 'Nested'),
    ('fields.Price', 'Price'),
    ('fields.Raw', 'Raw'),
    ('fields.String', 'String'),
    ('fields.Url', 'Url'),
  ]

WTF_PROPERIES = [
    ('', '-'),
    ('wtforms.BooleanField', 'BooleanField'),
    ('wtforms.DateField', 'DateField'),
    ('wtforms.DateTimeField', 'DateTimeField'),
    ('wtforms.DecimalField', 'DecimalField'),
    ('wtforms.FieldList', 'FieldList'),
    ('wtforms.FloatField', 'FloatField'),
    ('wtforms.IntegerField', 'IntegerField'),
    ('wtforms.RadioField', 'RadioField'),
    ('wtforms.SelectField', 'SelectField'),
    ('wtforms.SelectMultipleField', 'SelectMultipleField'),
    ('wtforms.StringField', 'StringField'),
    ('wtforms.TextAreaField', 'TextAreaField'),
  ]

FORMS_PROPERIES = [
    ('', '-'),
    ('forms.checkbox_field', 'checkbox_field'),
    ('forms.date_field', 'date_field'),
    ('forms.datetime_field', 'datetime_field'),
    ('forms.email_field', 'email_field'),
    ('forms.hidden_field', 'hidden_field'),
    ('forms.input_field', 'input_field'),
    ('forms.list_input_field', 'list_input_field'),
    ('forms.multiple_checkbox_field', 'multiple_checkbox_field'),
    ('forms.number_field', 'number_field'),
    ('forms.password_field', 'password_field'),
    ('forms.password_visible_field', 'password_visible_field'),
    ('forms.radio_field', 'radio_field'),
    ('forms.recaptcha_field', 'recaptcha_field'),
    ('forms.select_field', 'select_field'),
    ('forms.text_field', 'text_field'),
    ('forms.textarea_field', 'textarea_field'),
  ]

ICONS = [
    'adjust',
    'adn',
    'align-center',
    'align-justify',
    'align-left',
    'align-right',
    'ambulance',
    'anchor',
    'android',
    'angellist',
    'angle-double-down',
    'angle-double-left',
    'angle-double-right',
    'angle-double-up',
    'angle-down',
    'angle-left',
    'angle-right',
    'angle-up',
    'apple',
    'archive',
    'area-chart',
    'arrow-circle-down',
    'arrow-circle-left',
    'arrow-circle-o-down',
    'arrow-circle-o-left',
    'arrow-circle-o-right',
    'arrow-circle-o-up',
    'arrow-circle-right',
    'arrow-circle-up',
    'arrow-down',
    'arrow-left',
    'arrow-right',
    'arrow-up',
    'arrows-alt',
    'arrows-h',
    'arrows-v',
    'arrows',
    'asterisk',
    'at',
    'automobile',
    'backward',
    'ban',
    'bank',
    'bar-chart-o',
    'bar-chart',
    'barcode',
    'bars',
    'bed',
    'beer',
    'behance-square',
    'behance',
    'bell-o',
    'bell-slash-o',
    'bell-slash',
    'bell',
    'bicycle',
    'binoculars',
    'birthday-cake',
    'bitbucket-square',
    'bitbucket',
    'bitcoin',
    'bold',
    'bolt',
    'bomb',
    'book',
    'bookmark-o',
    'bookmark',
    'briefcase',
    'btc',
    'bug',
    'building-o',
    'building',
    'bullhorn',
    'bullseye',
    'bus',
    'buysellads',
    'cab',
    'calculator',
    'calendar-o',
    'calendar',
    'camera-retro',
    'camera',
    'car',
    'caret-down',
    'caret-left',
    'caret-right',
    'caret-square-o-down',
    'caret-square-o-left',
    'caret-square-o-right',
    'caret-square-o-up',
    'caret-up',
    'cart-arrow-down',
    'cart-plus',
    'cc-amex',
    'cc-discover',
    'cc-mastercard',
    'cc-paypal',
    'cc-stripe',
    'cc-visa',
    'cc',
    'certificate',
    'chain',
    'chain-broken',
    'check-circle-o',
    'check-circle',
    'check-square-o',
    'check-square',
    'check',
    'chevron-circle-down',
    'chevron-circle-left',
    'chevron-circle-right',
    'chevron-circle-up',
    'chevron-down',
    'chevron-left',
    'chevron-right',
    'chevron-up',
    'child',
    'circle-o-notch',
    'circle-o',
    'circle-thin',
    'circle',
    'clipboard',
    'clock-o',
    'close',
    'cloud-download',
    'cloud-upload',
    'cloud',
    'cny',
    'code-fork',
    'code',
    'codepen',
    'coffee',
    'cog',
    'cogs',
    'columns',
    'comment-o',
    'comment',
    'comments-o',
    'comments',
    'compass',
    'compress',
    'connectdevelop',
    'copy',
    'copyright',
    'credit-card',
    'crop',
    'crosshairs',
    'css3',
    'cube',
    'cubes',
    'cut',
    'cutlery',
    'dashboard',
    'dashcube',
    'database',
    'dedent',
    'delicious',
    'desktop',
    'deviantart',
    'diamond',
    'digg',
    'dollar',
    'dot-circle-o',
    'download',
    'dribbble',
    'dropbox',
    'drupal',
    'edit',
    'eject',
    'ellipsis-h',
    'ellipsis-v',
    'empire',
    'envelope-o',
    'envelope-square',
    'envelope',
    'eraser',
    'eur',
    'euro',
    'exchange',
    'exclamation-circle',
    'exclamation-triangle',
    'exclamation',
    'external-link-square',
    'external-link',
    'eye-slash',
    'eye',
    'eyedropper',
    'facebook-f',
    'facebook-official',
    'facebook-square',
    'facebook',
    'fast-backward',
    'fast-forward',
    'fax',
    'female',
    'fighter-jet',
    'file-archive-o',
    'file-audio-o',
    'file-code-o',
    'file-excel-o',
    'file-image-o',
    'file-movie-o',
    'file-o',
    'file-pdf-o',
    'file-photo-o',
    'file-picture-o',
    'file-powerpoint-o',
    'file-sound-o',
    'file-text-o',
    'file-text',
    'file-video-o',
    'file-word-o',
    'file-zip-o',
    'file',
    'files-o',
    'film',
    'filter',
    'fire-extinguisher',
    'fire',
    'flag-checkered',
    'flag-o',
    'flag',
    'flash',
    'flask',
    'flickr',
    'floppy-o',
    'folder-o',
    'folder-open-o',
    'folder-open',
    'folder',
    'font',
    'forumbee',
    'forward',
    'foursquare',
    'frown-o',
    'futbol-o',
    'gamepad',
    'gavel',
    'gbp',
    'ge',
    'gear',
    'gears',
    'genderless',
    'gift',
    'git-square',
    'git',
    'github-alt',
    'github-square',
    'github',
    'gittip',
    'glass',
    'globe',
    'google-plus-square',
    'google-plus',
    'google-wallet',
    'google',
    'graduation-cap',
    'gratipay',
    'group',
    'h-square',
    'hacker-news',
    'hand-o-down',
    'hand-o-left',
    'hand-o-right',
    'hand-o-up',
    'hdd-o',
    'header',
    'headphones',
    'heart-o',
    'heart',
    'heartbeat',
    'history',
    'home',
    'hospital-o',
    'hotel',
    'html5',
    'ils',
    'image',
    'inbox',
    'indent',
    'info-circle',
    'info',
    'inr',
    'instagram',
    'institution',
    'ioxhost',
    'italic',
    'joomla',
    'jpy',
    'jsfiddle',
    'key',
    'keyboard-o',
    'krw',
    'language',
    'laptop',
    'lastfm-square',
    'lastfm',
    'leaf',
    'leanpub',
    'legal',
    'lemon-o',
    'level-down',
    'level-up',
    'life-bouy',
    'life-buoy',
    'life-ring',
    'life-saver',
    'lightbulb-o',
    'line-chart',
    'link',
    'linkedin-square',
    'linkedin',
    'linux',
    'list-alt',
    'list-ol',
    'list-ul',
    'list',
    'location-arrow',
    'lock',
    'long-arrow-down',
    'long-arrow-left',
    'long-arrow-right',
    'long-arrow-up',
    'magic',
    'magnet',
    'mail-forward',
    'mail-reply',
    'mail-reply-all',
    'male',
    'map-marker',
    'mars-double',
    'mars-stroke-h',
    'mars-stroke-v',
    'mars-stroke',
    'mars',
    'maxcdn',
    'meanpath',
    'medium',
    'medkit',
    'meh-o',
    'mercury',
    'microphone-slash',
    'microphone',
    'minus-circle',
    'minus-square-o',
    'minus-square',
    'minus',
    'mobile-phone',
    'mobile',
    'money',
    'moon-o',
    'mortar-board',
    'motorcycle',
    'music',
    'navicon',
    'neuter',
    'newspaper-o',
    'openid',
    'outdent',
    'pagelines',
    'paint-brush',
    'paper-plane-o',
    'paper-plane',
    'paperclip',
    'paragraph',
    'paste',
    'pause',
    'paw',
    'paypal',
    'pencil-square-o',
    'pencil-square',
    'pencil',
    'phone-square',
    'phone',
    'photo',
    'picture-o',
    'pie-chart',
    'pied-piper-alt',
    'pied-piper',
    'pinterest-p',
    'pinterest-square',
    'pinterest',
    'plane',
    'play-circle-o',
    'play-circle',
    'play',
    'plug',
    'plus-circle',
    'plus-square-o',
    'plus-square',
    'plus',
    'power-off',
    'print',
    'puzzle-piece',
    'qq',
    'qrcode',
    'question-circle',
    'question',
    'quote-left',
    'quote-right',
    'ra',
    'random',
    'rebel',
    'recycle',
    'reddit-square',
    'reddit',
    'refresh',
    'remove',
    'renren',
    'reorder',
    'repeat',
    'reply-all',
    'reply',
    'retweet',
    'rmb',
    'road',
    'rocket',
    'rotate-left',
    'rotate-right',
    'rouble',
    'rss-square',
    'rss',
    'rub',
    'ruble',
    'rupee',
    'save',
    'scissors',
    'search-minus',
    'search-plus',
    'search',
    'sellsy',
    'send',
    'send-o',
    'server',
    'share-alt-square',
    'share-alt',
    'share-square-o',
    'share-square',
    'share',
    'shekel',
    'sheqel',
    'shield',
    'ship',
    'shirtsinbulk',
    'shopping-cart',
    'sign-in',
    'sign-out',
    'signal',
    'simplybuilt',
    'sitemap',
    'skyatlas',
    'skype',
    'slack',
    'sliders',
    'slideshare',
    'smile-o',
    'soccer-ball-o',
    'sort-alpha-asc',
    'sort-alpha-desc',
    'sort-amount-asc',
    'sort-amount-desc',
    'sort-asc',
    'sort-desc',
    'sort-down',
    'sort-numeric-asc',
    'sort-numeric-desc',
    'sort-up',
    'sort',
    'soundcloud',
    'space-shuttle',
    'spinner',
    'spoon',
    'spotify',
    'square-o',
    'square',
    'stack-exchange',
    'stack-overflow',
    'star-half-empty',
    'star-half-full',
    'star-half-o',
    'star-half',
    'star-o',
    'star',
    'steam-square',
    'steam',
    'step-backward',
    'step-forward',
    'stethoscope',
    'stop',
    'street-view',
    'strikethrough',
    'stumbleupon-circle',
    'stumbleupon',
    'subscript',
    'subway',
    'suitcase',
    'sun-o',
    'superscript',
    'support',
    'table',
    'tablet',
    'tachometer',
    'tag',
    'tags',
    'tasks',
    'taxi',
    'tencent-weibo',
    'terminal',
    'text-height',
    'text-width',
    'th-large',
    'th-list',
    'th',
    'thumb-tack',
    'thumbs-down',
    'thumbs-o-down',
    'thumbs-o-up',
    'thumbs-up',
    'ticket',
    'times-circle-o',
    'times-circle',
    'times',
    'tint',
    'toggle-down',
    'toggle-left',
    'toggle-off',
    'toggle-on',
    'toggle-right',
    'toggle-up',
    'train',
    'transgender-alt',
    'transgender',
    'trash-o',
    'trash',
    'tree',
    'trello',
    'trophy',
    'truck',
    'try',
    'tty',
    'tumblr-square',
    'tumblr',
    'turkish-lira',
    'twitch',
    'twitter-square',
    'twitter',
    'umbrella',
    'underline',
    'undo',
    'university',
    'unlink',
    'unlock-alt',
    'unlock',
    'unsorted',
    'upload',
    'usd',
    'user-md',
    'user-plus',
    'user-secret',
    'user-times',
    'user',
    'users',
    'venus-double',
    'venus-mars',
    'venus',
    'viacoin',
    'video-camera',
    'vimeo-square',
    'vine',
    'vk',
    'volume-down',
    'volume-off',
    'volume-up',
    'warning',
    'wechat',
    'weibo',
    'weixin',
    'whatsapp',
    'wheelchair',
    'wifi',
    'windows',
    'won',
    'wordpress',
    'wrench',
    'xing-square',
    'xing',
    'yahoo',
    'yelp',
    'yen',
    'youtube-play',
    'youtube-square',
    'youtube',
  ]

ICON_CHOICES = [(icon, icon) for icon in ICONS]
