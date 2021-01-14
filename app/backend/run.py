from api.src import create_app

app = create_app()
app.run(debug = True)
#import the create_app function from api.src and call it using app.run