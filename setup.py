from setuptools import setup

setup(
    name='rq-cli',
    version='0.1',
    py_modules=['rq_cli', 'rqinfo'],
    entry_points={
        'console_scripts': [
            'rq=rq_cli:main',
            ]
        },
    url='https://github.com/zhangliyong/rq-cli',
    license='BSD',
    author='Lyon Zhang',
    author_email='lyzhang87@gmail.com',
    description='A RQ CLI',
    long_description=open('README.rst').read(),
    install_requires=open('requirements.txt').read(),
)
