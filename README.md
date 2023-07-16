# adsb-hassio-sensors

  Aircraft sensors for Home Assistant [adsb-multi-portal-feeder [from 1.26.1] ](https://github.com/MaxWinterstein/homeassistant-addons/tree/main/adsb-multi-portal-feeder) add-on by [MaxWinterstein](https://github.com/MaxWinterstein)
  
  

## Supported feeders

  adsb.fi

  adsbexchange.com

  flightradar24.com

  opensky-network.org

  planefinder.net


## Available sensors

| Feeder                | Friendly name                    | Sensor                          | Unit           |
| --------------------- | -------------------------------- | ------------------------------- | -------------- |
| `adsb.fi`             | `Adsb.fi Uptime`                 | sensor.adsbfi_uptime            |                |
| `adsb.fi`             | `Adsb.fi Status`                 | sensor.adsbfi_status            | aircraft       |
| `adsb.fi`             | `Adsb.fi ADS-B`                  | sensor.adsbfi_adsb              | aircraft       |
| `adsb.fi`             | `Adsb.fi Mode-S`                 | sensor.adsbfi_mode_s            | aircraft       |
| `adsb.fi`             | `Adsb.fi MLAT`                   | sensor.adsbfi_mlat              | aircraft       |
| `adsb.fi`             | `Adsb.fi Tracks`                 | sensor.adsbfi_tracks_all        | track          |

| Feeder                | Friendly name                    | Sensor                          | Unit           |
| --------------------- | -------------------------------- | ------------------------------- | -------------- |
| `adsbexchange.com`    | `Adsb Exchange Uptime`           | sensor.adsbx_uptime             |                |
| `adsbexchange.com`    | `Adsb Exchange Status`           | sensor.adsbx_status             | aircraft       |
| `adsbexchange.com`    | `Adsb Exchange ADS-B`            | sensor.adsbx_adsb               | aircraft       |
| `adsbexchange.com`    | `Adsb Exchange Mode-S`           | sensor.adsbx_mode_s             | aircraft       |
| `adsbexchange.com`    | `Adsb Exchange MLAT`             | sensor.adsbx_mlat               | aircraft       |
| `adsbexchange.com`    | `Adsb Exchange Tracks`           | sensor.adsbx_tracks_all         | track          |

| Feeder                | Friendly name                    | Sensor                          | Unit           |
| --------------------- | -------------------------------- | ------------------------------- | -------------- |
| `flightradar24.com`   | `Flightradar24 Feeder Status`    | sensor.flightradar_feed         |                |
| `flightradar24.com`   | `Flightradar24 Status`           | sensor.flightradar_status       | aircraft       |
| `flightradar24.com`   | `Flightradar24 ADS-B`            | sensor.flightradar_adsb         | aircraft       |
| `flightradar24.com`   | `Flightradar24 Non ADS-B`        | sensor.flightradar_non_adsb     | aircraft       |
| `flightradar24.com`   | `Flightradar24 MAX Range`        | sensor.flightradar_max_range    | nm             |

| Feeder                | Friendly name                    | Sensor                          | Unit           |
| --------------------- | -------------------------------- | ------------------------------- | -------------- |
| `opensky-network.org` | `Opensky Status`                 | sensor.opensky_status           | aircraft       | 
| `opensky-network.org` | `Opensky ADS-B`                  | sensor.opensky_adsb             | aircraft       | 
| `opensky-network.org` | `Opensky MLAT`                   | sensor.opensky_mlat             | aircraft       |
| `opensky-network.org` | `Opensky Mode-S Rate`            | sensor.opensky_mode_s_rate      | aircraft / min | 
| `opensky-network.org` | `Opensky Mode-AC Rate`           | sensor.opensky_mode_ac_rate     | aircraft / min | 

| Feeder                | Friendly name                    | Sensor                          | Unit           |
| --------------------- | -------------------------------- | ------------------------------- | -------------- |
| `planefinder.net`     | `Planefinder Status`             | sensor.planefinder_status       | aircraft       |
| `planefinder.net`     | `Planefinder ADS-B`              | sensor.planefinder_adsb         | aircraft       |
| `planefinder.net`     | `Planefinder MLAT`               | sensor.planefinder_mlat         | aircraft       |
| `planefinder.net`     | `Planefinder Mode-S Rate`        | sensor.planefinder_mode_s_rate  | packet / s     |
| `planefinder.net`     | `Planefinder Mode-AC Rate`       | sensor.planefinder_mode_ac_rate | packet / s     |
| `planefinder.net`     | `Planefinder Receiver Bandwidth` | sensor.planefinder_bandwidth    | Kb / s         |


##

![sensor aircraft tracked](https://github.com/plo53/adsb-hassio-sensors/blob/master/media/Home%20Assistant%20ADS-B%20sensors.png)

