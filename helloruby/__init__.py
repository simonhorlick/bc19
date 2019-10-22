import check50


@check50.check()
def hello_world():
    """hello world"""
    check50.include("hello_spec.rb")
    check50.run("rspec --no-colour hello_spec.rb").stdout("0 failures").exit(0)
