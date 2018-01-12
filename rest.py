import web

urls = (
    '/test', 'test_class',
    '/', 'test_class'
)
#Above are the urls that will be served by the server

app = web.application(urls, globals())
#Application is being created using the aforementioned urls

class test_class:
    def GET(self):
        return "No data yet - test_class GET being called"
    def POST(self):
        post_data = web.data()
        return post_data
#Definition of test_class which will be called on /test and /

if __name__ == "__main__":
    app.run()
#run the previously created application
