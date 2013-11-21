from flask import url_for, Markup
from os import path

ASSET_TAG_TEMPLATES = {
	'css': '<link rel="stylesheet" type="text/css" href=%s>',
	'js': "<script src=%s></script>"
}

def file_ext(filename):
	return filename.split('.')[-1]

def asset_category(filename):
	ext = file_ext(filename)
	if ext == 'sass' or ext == 'scss':
		ext = 'css'
	return ext

def asset_url(filename):
	category = asset_category(filename)
	path = ''.join([category, '/', filename])
	return url_for('static', filename=path)

def asset_tag(filename):
	category = asset_category(filename)
	tag = ASSET_TAG_TEMPLATES[category]
	return Markup(tag%asset_url(filename))
