from distutils.core import setup
# import sparsile


readme = open('README.md').read()
reqs = [line.strip() for line in open('requirements.txt')]

setup(
    name='sparsile-museums',
    version='0.1',
    description='Widget for providing a bit of art through sentiment analysis',
    long_description=readme,
    keywords='art color sentiment-analysis',
    author='Soren Scott',
    author_email='sorenscott@gmail.com',
    maintainer='Soren Scott',
    maintainer_email='sorenscott@gmail.com',
    url='http://github.com/roomthily/sparsile-museums',
    install_requires=reqs,
    # cmdclass={'test': PyTest},
    packages=['sparsile']
)
