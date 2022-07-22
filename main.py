from driver import protocols

for protocol in protocols.PROTOCOLS:
    print('Protocol name: %s' %protocol['name'])
    print('\tuuid: %s' % protocol['uuid'])
    print('\tdescr: %s' % protocol['description'])
    print('\tclass: %s' % protocol['class'])
    # Создем экземпляр класса
    obj = protocol['class']()
    obj.method()