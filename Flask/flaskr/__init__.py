import os

from flask import Flask

def create_app(test_condif=None):
    #crea e configura l'app
    app = Flask(__name__, instance_relative_config=True) #crea l'istanza Flask, __name__ è il nome del modulo Python corrente
    app.config.from_mapping( #setta alcune configurazioni base che userà l'app
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        #Carica l'istanza del config, se esiste, quando non la sta testando
        app.config.from_pyfile('config.py', silent=True) #cabia le configurazioni base con quelle prese da config.py se esiste
    else:
        #Carica il test config se l'ha superato
        app.config.from_mapping(test_config)

    #Assicura che l'istanza della cartella esista
    try:
        os.makedirs(app.instance_path) #assicura che app.instance_path esista
    except OSError:
        pass

    #una semplice pagina che dice hellp
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
