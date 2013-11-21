from flask import url_for, Markup

ASSET_TAG_TEMPLATES = {
	'css': '<link rel="stylesheet" type="text/css" href=%s>',
	'js': "<script src=%s></script>"
}

def _file_ext(filename):
	return filename.split('.')[-1]

def _asset_category(filename):
	ext = _file_ext(filename)
	if ext == 'sass' or ext == 'scss':
		ext = 'css'
	return ext

def _asset_url(filename):
	category = _asset_category(filename)
	path = ''.join([category, '/', filename])
	return url_for('static', filename=path)

def asset_tag(filename):
	category = _asset_category(filename)
	tag = ASSET_TAG_TEMPLATES[category]
	return Markup(tag%_asset_url(filename))
