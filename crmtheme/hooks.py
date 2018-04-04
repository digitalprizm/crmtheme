# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "crmtheme"
app_title = "Crmtheme"
app_publisher = "DigitalPrizm"
app_description = "Manages CRM menus"
app_icon = "octicon octicon-file-directory"
app_color = "green"
app_email = "contact@digitalprizm.net"
app_license = "MIT"

# Includes in <head>
# ------------------
# include js, css files in header of desk.html
# app_include_css = "/assets/crmtheme/css/crmtheme.css"
# app_include_js = "/assets/crmtheme/js/crmtheme.js"
app_include_css = [
    "/assets/crmtheme/css/crmtheme.css",
    "/assets/crmtheme/css/skin-blue.css",
    "/assets/crmtheme/css/custom.css",
    "/assets/crmtheme/css/temp.css",
] 
app_include_js = [
    "/assets/crmtheme/js/crmtheme.js",
    "/assets/crmtheme/js/custom.js",
    "/assets/js/crmtheme-template.min.js",
]

# include js, css files in header of web template
web_include_css = "/assets/crmtheme/css/crmtheme-web.css"
# web_include_js = "/assets/crmtheme/js/crmtheme.js"

# include js, css files in header of web template
# web_include_css = "/assets/crmtheme/css/crmtheme.css"
# web_include_js = "/assets/crmtheme/js/crmtheme.js"
# include js, css files in header of desk.html
# app_include_css = "/assets/crmtheme/css/crmtheme.css"
# app_include_js = "/assets/crmtheme/js/crmtheme.js"

# include js, css files in header of web template
# web_include_css = "/assets/crmtheme/css/crmtheme.css"
# web_include_js = "/assets/crmtheme/js/crmtheme.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "crmtheme.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "crmtheme.install.before_install"
# after_install = "crmtheme.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "crmtheme.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"crmtheme.tasks.all"
# 	],
# 	"daily": [
# 		"crmtheme.tasks.daily"
# 	],
# 	"hourly": [
# 		"crmtheme.tasks.hourly"
# 	],
# 	"weekly": [
# 		"crmtheme.tasks.weekly"
# 	]
# 	"monthly": [
# 		"crmtheme.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "crmtheme.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "crmtheme.event.get_events"
# }

