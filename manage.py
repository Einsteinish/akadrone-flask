import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from aka import app, db

app.config.from_object('config')
app_settings = app.config['APP_SETTINGS']

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()

