from setuptools import setup, find_packages

setup(
    name='assistant_bot',
    version='1.0.0',
    description='Helps to organize and plan your daily routine',
    url='https://github.com/Dmytrii-Shypilov/Personal-Assistant',
    author='Dmytrii Shypilov, Anton Akulenko, KostiantynLiapkalo, Artur Mistiuk',
    author_email='dmytriishypilov@gmail.com',
    license='MIT',
    include_package_data=True,
    packages=find_packages(),
    install_requires=['autopep8',  'beautifulsoup4', 'bs4', 'certifi', 'charset-normalizer', 'idna', 'prettytable', 'prompt-toolkit', 'pycodestyle',  'requests',
                      'soupsieve', 'urllib3', 'wcwidth'
                      ],
    entry_points={'console_scripts': [
        'call-assistant=personal_assistant.menu:main']}
)
