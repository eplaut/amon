from amon.web.views.app import DashboardView, SystemView, ProcessesView, ExceptionsView, LogsView
from amon.web.views.auth import LoginView, CreateUserView
from amon.web.settings import PROJECT_ROOT
from amon.web.views.api import ApiLogs, ApiException
import os
import tornado.web
import base64
import uuid
	
app_settings = {
	"static_path": os.path.join(PROJECT_ROOT, "media"),
	"debug": "True",
	"cookie_secret": base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)  
}

handlers = [
	# App
	(r"/", DashboardView),
	(r"/system", SystemView),
	(r"/processes", ProcessesView),
	(r"/exceptions", ExceptionsView),
	(r"/logs", LogsView),
	# Auth
	(r"/login", LoginView),
	(r"/create_user", CreateUserView),
	# API
	(r"/api/log", ApiLogs),
	(r"/api/exception", ApiException),
	# Static
	(r"/media/(.*)", tornado.web.StaticFileHandler, {"path": app_settings['static_path']}),
]
application = tornado.web.Application(handlers, **app_settings)
