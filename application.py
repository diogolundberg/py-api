from app import application


@application.route('/health_check')
def health_check(request):
    return text('ready')

if __name__ == "__main__":
    application.run()
