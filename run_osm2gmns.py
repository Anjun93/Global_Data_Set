import osm2gmns as og
net = og.getNetFromFile('map.osm', POI=True, network_types=('railway','auto','aeroway','walk','bike'), link_types='all')
og.consolidateComplexIntersections(net, auto_identify=True)
og.generateNodeActivityInfo(net)
# og.buildMultiResolutionNets(net)
# og.connectPOIWithNet(net)
og.outputNetToCSV(net)