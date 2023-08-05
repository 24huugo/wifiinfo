import time
import pywifi
from pywifi import const

def get_wifi_info(interface):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[interface]

    iface.scan()  # Escanea las redes Wi-Fi disponibles
    time.sleep(2)  # Espera un poco para que el escaneo se complete

    networks = iface.scan_results()
    wifi_list = {}
    for i, network in enumerate(networks):
        wifi_list[i + 1] = {
            "SSID": network.ssid,
            "BSSID": network.bssid,
            "Signal Strength (dBm)": network.signal,
            "Frequency (MHz)": network.freq,
            "Encryption": network.akm[0],
            "Channel": network.channel,
        }

    return wifi_list

def main():
    print("Escaneando redes Wi-Fi disponibles...\n")
    wifi_list = get_wifi_info(interface=0)

    for num, wifi_info in wifi_list.items():
        print(f"Red {num}:")
        for key, value in wifi_info.items():
            print(f"{key}: {value}")
        print()

    selected_wifi_num = int(input("Ingrese el número de la red Wi-Fi de la que desea obtener información: "))

    if selected_wifi_num in wifi_list:
        selected_wifi = wifi_list[selected_wifi_num]
        print(f"\nInformación de la Red Wi-Fi {selected_wifi_num}:")
        for key, value in selected_wifi.items():
            print(f"{key}: {value}")
    else:
        print("¡Número de red Wi-Fi no válido!")

if __name__ == "__main__":
    main()
