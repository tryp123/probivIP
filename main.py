import requests
import folium
from pyfiglet import Figlet

def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

        data = {
            '[IP]': response.get('query'),
            '[Int prov]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Country]': response.get('country'),
            '[Region Name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon'),
        }

        for k, v in data.items():
            print(f'{k} : {v}')

        # Створення мапи
        area_map = folium.Map(location=[response.get('lat'), response.get('lon')])

        # Додавання маркера
        folium.Marker([response.get('lat'), response.get('lon')],
                      icon=folium.CustomIcon('location.png', icon_size=(32, 32)),
                      popup='Your Location').add_to(area_map)

        # Збереження мапи в HTML файл
        area_map.save(f'{response.get("query")}_{response.get("city")}.html')

    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')

def main():
    preview_text = Figlet(font='slant')
    print(preview_text.renderText('IP checker'))
    ip = input('Enter IP: ')

    get_info_by_ip(ip=ip)

if __name__ == '__main__':
    main()
