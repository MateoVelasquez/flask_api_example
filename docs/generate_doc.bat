call make.bat clean
RD /S /Q source\api
SET SPHINX_APIDOC_OPTIONS=members,show-inheritance
sphinx-apidoc -f -M -o source/api/ ../../flask_api_example
make.bat latexpdf