Thrift Hive Metastore Client
============================

A simple python thrift client of hive metastore, which is used to 
fetch table and schema information.

The class files are generated from Hive source using thrift. This 
project just makes a nice package of the generated code.

Usage
=====

```bash
>> tox -r -e py27

>> # install
>> .tox/py27/bin/python setup.py sdist upload

>> # browse tables
>> # get all tables
>> .tox/py27/bin/thrift_hive_metastore localhost 9083

>> # get all tables and show their field definitions
>> .tox/py27/bin/thrift_hive_metastore localhost 9083 -s

>> # get tables from a namespace
>> .tox/py27/bin/thrift_hive_metastore localhost 9083 mynamesapce

>> # get tables from namesapces matching given pattern
>> .tox/py27/bin/thrift_hive_metastore localhost 9083 my*

>> # get tables whose names matche a given pattern,  from namesapces matching given pattern 
>> .tox/py27/bin/thrift_hive_metastore localhost 9083 my* *mytable*

```

