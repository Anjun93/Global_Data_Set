import osm2rail as orl

net=orl.get_network_from_file('map.osm',POIs=True,check_boundary=True)

orl.save_network(net)

# subarea_name = '東京駅'
# download_dir = './osmfile'
# osm_file=orl.download_osm_data_from_overpass(subarea_names=subarea_name,download_dir = download_dir,ret_download_path=True)
# net=orl.get_network_from_file(filename=osm_file[0],POIs=True,check_boundary=True)
# orl.show_network(net)
