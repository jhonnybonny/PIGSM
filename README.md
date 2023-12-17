# GSM Base Station on Raspberry Pi
Welcome to the GSM Base Station project! 📡📱

<img src="https://github.com/jhonnybonny/PIGSM/assets/87495218/10e2c7a7-5559-4a7c-aa8e-4ca5f3c479a6" width="50%" height="50%" alt="IMG_1153">

## Overview

This project allows you to turn your Raspberry Pi into a GSM base station using [DragonOS PI](https://sourceforge.net/projects/dragonos-pi64), CalypsoBTS, and osmo-nitb-scripts-calypsobts.

## Requirements

- Raspberry Pi 3+/0
- [DragonOS PI](https://sourceforge.net/projects/dragonos-pi64)
- [OsmocomBB phones (MotorolaC123/C121/C118) ](https://osmocom.org/projects/baseband/wiki/Phones) 
- [USB TTL](https://www.aliexpress.com/w/wholesale-cp2102-usb-to-ttl-converter.html)
- [Solder a large circle on the button to GPIO21 (not necessary)]


## Installation

1. Install [DragonOS PI](https://sourceforge.net/projects/dragonos-pi64) on your Raspberry Pi 3+.
2. Clone the CalypsoBTS repository:

    ```bash
    git clone https://github.com/jhonnybonny/PIGSM
    ```

3. Run install script:

    ```bash
    cd PIGSM && sudo bash install.sh
    ```

4. Start osmo-nitb-scripts-calypsobts:

    ```bash
    cd /usr/src/osmo-nitb-scripts-calypsobts
    sudo bash trx.sh
    ```
    EDIT ARFCN IN CLOCK !!! ( transceiver -e 1 -a NEARBY_ARFCN -r99 )
    ```bash
    sudo nano /usr/src/osmo-nitb-scripts-calypsobts/services/osmo-trx-lms.service
    ```
    ```bash
    sudo bash install_services.sh
    sudo python3 main.py -u
    ```

5. Your GSM base station is UPed!

## License

This project is licensed under the [MIT License](LICENSE).
