__all__ = ['ttypes', 'constants', 'ThriftHiveMetastore']

def main():
    from optparse import OptionParser

    parser = OptionParser()
    parser.add_option("-s", "--show-fields", dest="show_fields",
                  help="show fields of table", action="store_true", default=False)
    (options, args) = parser.parse_args()
    print options
    print args

    if len(args) >= 2:
        host = args[0]
        port = args[1]
        if len(args) >= 3:
            database_pattern = args[2]
        else:
            database_pattern = '*'
        if len(args) >= 4:
            table_pattern = args[3]
        else:
            table_pattern = '*'
    else:
        host = 'localhost'
        port = 9083
    print 'host: ', host
    print 'port: ', port
    print 'database_pattern: ', database_pattern
    print 'table_pattern: ', table_pattern

    from thrift_hive_metastore import ThriftHiveMetastore
    from thrift_hive_metastore.ttypes import *

    from thrift import Thrift
    from thrift.transport import TSocket
    from thrift.transport import TTransport
    from thrift.protocol import TBinaryProtocol

    # Make socket
    transport = TSocket.TSocket(host, int(port))

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = ThriftHiveMetastore.Client(protocol)

    # Connect!
    transport.open()
    for d in client.get_databases(database_pattern):
        print '[%s]' % d
        for t in client.get_tables(d, table_pattern):
            table = client.get_table(d, t)
            print ' '*4, "{namespace}.{name}:    {location}".format(namespace=d, name=t, location=table.sd.location)
            if options.show_fields:
                for c in table.sd.cols:
                    print ' '*8, c
