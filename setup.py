from setuptools import setup, find_packages
#this is a test
setup(name = 'django_ckeditor_improved',
      description = 'CKEditor bundled as a django staticfiles app.',
      version = '1.5',
      url = 'https://github.com/ninapavlich/django_ckeditor_improved',
      author = 'Nina Pavlich',
      author_email='nina@ninalp.com',
      license = 'BSD',
      packages=find_packages(exclude=['ez_setup']),
      zip_safe = False,
      include_package_data=True,
      classifiers=[
                   'Development Status :: 5 - Production/Stable',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python'
                  ]
)
