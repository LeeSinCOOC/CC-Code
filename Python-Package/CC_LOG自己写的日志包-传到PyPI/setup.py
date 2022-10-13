from setuptools import setup,find_packages
setup(name='cclog',
      version='1.0',
      description='chen\'s log config package',
      author='chen',
      author_email='690246265@qq.com',
      requires= ['yaml','logging'],
      packages=find_packages(),
      license="apache 3.0",
      package_data={"":['*.yaml']}
      )
