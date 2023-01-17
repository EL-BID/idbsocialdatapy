import setuptools

with open("README.md", "r", encoding="utf-8") as description:
    long_description = description.read()

setuptools.setup(
    name="idbsocialdatapy",
    version="0.0.1",
    author="TU NOMBRE DE AUTORÍA",
    author_email="code.iadb.org",
    description="UNA CORTA DESCRIPCIÓN DE LO QUE HACE TU LIB",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    url="https://github.com/EL-BID/idbsocialdatapy",
    project_urls={
        "Bug Tracker": "https://github.com/EL-BID/idbsocialdatapy/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: AM-331-A3",
        "Operating System :: OS Independent",
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
    ],
    keywords=["demo", "hello-world", "development", "practice", "pypi"],
    packages=["nombre_de_tu_lib"],
    package_data={
        'nombre_de_tu_lib': [
            'carpeta_con_datos_extra/*.json',
        ]
    },
    install_requires=[
        "requests",
        "multipledispatch"
    ],
    python_requires=">=3.6",
)
