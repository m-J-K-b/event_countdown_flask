from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from .config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__, template_folder="templates")
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from .calendar_feed_bp.models import CalendarFeed
    from .calendar_feed_bp.routes import calendar_feed_bp
    from .event_bp.models import Event
    from .event_bp.routes import event_bp
    from .routes import main

    app.register_blueprint(calendar_feed_bp, url_prefix="/calendar_feeds")
    app.register_blueprint(event_bp, url_prefix="/events")
    app.register_blueprint(main)

    return app