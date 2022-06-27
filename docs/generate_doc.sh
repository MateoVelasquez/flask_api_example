./make.bat clean
rm -r source/api
export SPHINX_APIDOC_OPTIONS=members,show-inheritance
sphinx-apidoc.exe -f -M -o source/api/ ../flask_api_example
./make.bat latexpdf