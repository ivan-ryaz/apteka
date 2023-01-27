import sys
from Samples.business import find_business
from Samples.dist import lonlat_distance
from Samples.geocoder import get_coordinates
from Samples.mapapi_PG import show_map


def main():
    top = ' '.join(sys.argv[1:])
    l1, l2 = get_coordinates(top)
    adr = f'{l1},{l2}'
    delta = '0.005,0.005'
    orgn = find_business(adr, delta, 'аптека')
    org_lat, = orgn['geometry']['coordinates']
    org_lat = float(point[0])
    org_lon = float(point[1])
    point_param = f'pt={org_lat},{org_lon},pm2dgl'
    show_map(f'll={adr}&spn={delta}', 'map', add_params=point_param)
    popar = point_param + f'~{adr},pm2rdl'
    show_map('ll={0}&spn={1}'.format(adr, delta), 'map', add_params=popar)
    show_map(map_type='map', add_params=popar)
    name = orgn["properties"]["CompanyMetaData"]["name"]
    address = orgn["properties"]["CompanyMetaData"]["address"]
    time = orgn["properties"]['CompanyMetaData']['Hours']['text']
    dist = round(lonlat_distance((l2, l1), (org_lon, org_lat)))
    snippet = f'Название:\t{name}\nАдрес:\t{address}\nВремя работы:\t{time}\n' \
              f'Расстояние:\t{dist}м.'
    print(snippet)


if __name__ == "__main__":
    main()