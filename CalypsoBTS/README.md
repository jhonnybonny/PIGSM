sudo ./osmocon -m c123xor -p /dev/ttyUSB0 -s /tmp/osmocom_l2 -c firmwares/compal_e88/trx.highram.bin
sudo ./transceiver -e 1 -a ARFCN -r99
sudo osmo-nitb --yes-i-really-want-to-run-prehistoric-software -c openbsc.cfg -l hlr.sqlite3 -P -C
sudo osmo-bts-trx -c osmo-bts-trx-calypso.cfg -d DRSL:DOML:DLAPDM
