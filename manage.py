from flask_script import Manager, Server
from app import create_app,db
from app.models import User,Comment,Pitch,Category,Role
from flask_migrate import Migrate, MigrateCommand


app=create_app('development')
migrate=Migrate(app,db)
manager=Manager(app)
manager.add_command('server', Server)
manager.add_command('db',MigrateCommand)


@app.cli.command()
def test():
  """
  Run unit tests
  """
  import unittest

  tests=unittest.TestLoader().discover('tests')
  unittest.TextTestRunner(verbosity=2).run(tests)

@app.shell_context_processor
def make_shell_context():
  return dict(app=app,db=db,User=User,Comment=Comment,Pitch=Pitch,Category=Category,Role=Role)

if __name__=='__main__':
  app.run()