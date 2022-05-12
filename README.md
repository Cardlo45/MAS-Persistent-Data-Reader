# Persistent Data Reader for Monika After Story
## **``BACKUP YOUR PERSISTENT FILE!!``**
`I don't know what could happen and nothing should happen but better safe than sorry.`

This Submod allows you to read the Persistent Data for [MAS](https://www.monikaafterstory.com/).
If you get an Error please create an Issue


This Submod was primarily created for 
[Monika on Desktop](https://github.com/SAn4Es-TV/MonikaOnDesktop) made by [SAn4Es-TV](https://github.com/SAn4Es-TV)
and the 
[MAS-Desktop Background](#) (WIP) made by [Me (Carslo_45)](https://github.com/Cardlo45)

## How to Use:
To access the Persistent Data the file is located here:
- Windows:
	`%APPDATA%\RenPy\Monika After Story\pdread.json`
- MacOS:
	`~/Library/RenPy/Monika After Story/pdread.json`
- Linux:
	`~/.renpy/Monika After Story/pdread.json`

## Known Issues:
### Some Variables can't be exported yet.
- event_database
- farewell_database
- greeting_database
- _mas_apology_database
- _mas_undo_action_rules
- _mas_strip_dates_rules
- persistent.sessions
- _mas_affection['freeze_date']
- _mas_pong_difficulty_change_next_game_date
- _mas_xp_rst
- _mas_apology_time_db
- _mas_apology_reason_use_db
- _mas_fun_facts_database
- _mas_songs_database
- _mas_first_kiss 
	`(added pd_masFirstKissBool as workaround)`
- _mas_last_kiss 
	`(added pd_masLastKissBool as workaround)`
- _mas_dockstat_checkout_log
- _mas_dockstat_checkin_log
- _mas_dockstat_moni_log
- _mas_game_database
- _mas_poems_seen
- _mas_selspr_acs_db
- _mas_selspr_hair_db
- _mas_selspr_clothes_db
- _mas_sprites_json_gifted_sprites
- _mas_submod_version_data
- _mas_date_last_checked_rain
- _mas_windowreacts_database
- _mas_windowreacts_notif_filters
### Some Scripts are  not implemented yet
- script-holidays.rpy
- sprite-chart.rpy