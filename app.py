from utils.app_factory import create_app

app = create_app({'MODE': 'PROD'})

if __name__ == '__main__':
    app.run(debug=True)

