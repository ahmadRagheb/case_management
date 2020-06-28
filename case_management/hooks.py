# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "case_management"
app_title = "case_management"
app_publisher = "kamal"
app_description = "case_management"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "kaml@k.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/case_management/css/case_management.css"
# app_include_js = "/assets/case_management/js/case_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/case_management/css/case_management.css"
# web_include_js = "/assets/case_management/js/case_management.js"

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
# get_website_user_home_page = "case_management.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "case_management.install.before_install"
# after_install = "case_management.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "case_management.notifications.get_notification_config"

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
# 		"case_management.tasks.all"
# 	],
# 	"daily": [
# 		"case_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"case_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"case_management.tasks.weekly"
# 	]
# 	"monthly": [
# 		"case_management.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "case_management.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "case_management.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "case_management.task.get_dashboard_data"
# }

fixtures = [
    {
        "dt": "Role",
        "filters": [ ["name", "in", ["Developer"]]]
    }
]