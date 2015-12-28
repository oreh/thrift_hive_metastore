__all__ = ['ttypes', 'constants', 'ThriftHiveMetastore']

def main():
    import sys

    if len(sys.argv) >= 3:
        host = sys.argv[1]
        port = sys.argv[2]
        if len(sys.argv) >= 4:
            database_pattern = sys.argv[3]
        else:
            database_pattern = '*'
        if len(sys.argv) >= 5:
            table_pattern = sys.argv[4]
        else:
            table_pattern = '*'
    else:
        host = 'localhost'
        port = 9083
    print 'host: ', host
    print 'port: ', port

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
            print ' '*4, "{name}:    {location}".format(name=t, location=table.sd.location)
            for c in table.sd.cols:
                print ' '*8, c
