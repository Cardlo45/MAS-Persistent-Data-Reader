init -990 python:
    store.mas_submod_utils.Submod(
        author="Carslo_45",
        name="Persistent Data Reader",
        description="A Submod to access the Persistent Data (READ-ONLY)",
        version="0.6.1"#,
        #settings_pane="PDReaderSettingsPanel"
    )
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Persistent Data Reader",
            user_name="Cardlo45",
            repository_name="MAS-Persistent-Data-Reader"
        )

# init -5:
#     screen PDReaderSettingsPanel():
#         vbox:
#             # xmaxinum 800
#             # xfill True

#             ## Toggle File Generation, Default = False
#             text "Settings Panel Test."

init 100:
    python:
        getPersistentData()
        store.mas_submod_utils.registerFunction("quit",getPersistentData)

init python:
    def getPersistentData():
        import os
        import time as pd_time
        import json
        
        pd_allData = {
        ## chess.rpy - 10th of May 2022
        'pd_masChessStats': persistent._mas_chess_stats,
        'pd_masChessDifficulty': persistent._mas_chess_difficulty,
        'pd_masChessQuicksave': persistent._mas_chess_quicksave,
        'pd_masChessDlgAction': persistent._mas_chess_dlg_action,
        'pd_masChessTimedDisable': persistent._mas_chess_timed_disable, # "NOT_AVAILABLE", # 
        'pd_masChess3EditSorry': persistent._mas_chess_3_edit_sorry,
        'pd_masChessMangleAll': persistent._mas_chess_mangle_all,
        'pd_masChessSkipFileChecks': persistent._mas_chess_skip_file_checks,

        ## definitions.rpy - 10th of May 2022 [1/2]
        'pd_playername': persistent.playername,
        'pd_playthrough': persistent.playthrough,
        'pd_yuriKill': persistent.yuri_kill,
        'pd_seenEyes': persistent.seen_eyes,
        'pd_seenSticker': persistent.seen_sticker,
        'pd_ghostMenu': persistent.ghost_menu,
        'pd_seenGhostMenu': persistent.seen_ghost_menu,
        'pd_anticheat': persistent.anticheat,
        'pd_clear': persistent.clear,
        'pd_specialPoems': persistent.special_poems,
        'pd_clearall': persistent.clearall,
        'pd_menuBgM': persistent.menu_bg_m,
        'pd_firstLoad': persistent.first_load,
        'pd_masImportedSaves': persistent._mas_imported_saves,
        'pd_masMonikaNickname': persistent._mas_monika_nickname,
        'pd_monikaTopic': persistent.monika_topic,
        'pd_monikaSaidTopics': persistent.monika_topic,
        'pd_eventList': persistent.event_list,
        'pd_eventDatabase': persistent.event_database, # "NOT_AVAILABLE", # 
        'pd_farewellDatabase': persistent.farewell_database, # "NOT_AVAILABLE", # 
        'pd_greetingDatabase': persistent.greeting_database, # "NOT_AVAILABLE", # 
        'pd_masApologyDatabase': persistent._mas_apology_database, # "NOT_AVAILABLE", # 
        'pd_masUndoActionRules': persistent._mas_undo_action_rules, # "NOT_AVAILABLE", # 
        'pd_masStripDatesRules':  persistent._mas_strip_dates_rules, # "NOT_AVAILABLE", #
        'pd_gender': persistent.gender,
        'pd_closedSelf': persistent.closed_self,
        'pd_masGameCrashed': persistent._mas_game_crashed,
        'pd_seenMonikaInRoom': persistent.seen_monika_in_room,
        'pd_masEverWon': persistent._mas_ever_won,
        ## definitions.rpy - 12th of May 2022 [2/2]
        'pd_session': persistent.sessions, # "NOT_AVAILABLE", # 
        'pd_randomSeen': persistent.random_seen,
        'pd_masAffection': persistent._mas_affection, # {
        # 'affection': persistent._mas_affection['affection'],
        # 'goodExp': persistent._mas_affection['goodexp'],
        # 'badExp': persistent._mas_affection['badexp'],
        # 'apologyFlag': persistent._mas_affection['apologyflag'],
        # 'todayExp': persistent._mas_affection['today_exp'],
        # },
        'pd_masEnableRandomRepeats': persistent._mas_enable_random_repeats,
        'pd_masFirstCalenderCheck': persistent._mas_first_calendar_check,
        'pd_masInIdleMode': persistent._mas_in_idle_mode,
        'pd_masIdelData': persistent._mas_idle_data,
        'pd_masMonikaClothes': persistent._mas_monika_clothes,
        'pd_masMonikaHair': persistent._mas_monika_hair,
        'pd_masLikesHairdown': persistent._mas_likes_hairdown,
        'pd_masHairChanged': persistent._mas_hair_changed,
        'pd_masSunrise': persistent._mas_sunrise,
        'pd_masSunset': persistent._mas_sunset,
        'pd_masSensitiveMode': persistent._mas_sensitive_mode,
        'pd_masDisableEggs': persistent._mas_disable_eggs,
        'pd_ddlcReloadCount': persistent._mas_ddlc_reload_count,
        'pd_randchatFreq': persistent._mas_randchat_freq,
        ## event-handler.rpy - 12th of May 2022
        'pd_poolUnlocks': persistent._mas_pool_unlocks,
        'pd_evYearsetBlacklist': persistent._mas_ev_yearset_blacklist,
        ## pong.rpy - 12th of May 2022
        'pd_pongDifficulty': persistent._mas_pong_difficulty,
        'pd_pongDifficultyChangeNextGame': persistent._mas_pong_difficulty_change_next_game,
        'pd_pmEverLetMonikaWinOnPurpose': persistent._mas_pm_ever_let_monika_win_on_purpose,
        'pd_pongDifficultyChangeNextGameDate': persistent._mas_pong_difficulty_change_next_game_date, # "NOT_AVAILABLE", # 
        ## progression.rpy - 12th of May 2022
        'pd_masXpRst': persistent._mas_xp_rst, # "NOT_AVAILABLE", # 
        'pd_masXpHrx': persistent._mas_xp_hrx,
        'pd_masXpTnl': persistent._mas_xp_tnl,
        'pd_masXpLvl': persistent._mas_xp_lvl,
        ## script-affection.rpy - 12th of May 2022
        'pd_masLongAbsence': persistent._mas_long_absence,
        'pd_masPctaieibe': persistent._mas_pctaieibe,
        'pd_masPctaneibe': persistent._mas_pctaneibe,
        'pd_masPctadeibe': persistent._mas_pctadeibe,
        'pd_masAffBackup': persistent._mas_aff_backup,
        'pd_masPmCalledMoniABadName': persistent._mas_pm_called_moni_a_bad_name,
        'pd_masOfferedNickname': persistent._mas_offered_nickname,
        'pd_masGrandfatheredNickname': persistent._mas_grandfathered_nickname,
        'pd_masPlayerNicknames': persistent._mas_player_nicknames,
        'pd_masLoadInFinalfarewellMode': persistent._mas_load_in_finalfarewell_mode,
        ## script-apologies.rpy - 12th of May 2022
        'pd_masApologyTimeDb': persistent._mas_apology_time_db, # "NOT_AVAILABLE", # 
        'pd_masApologyReasonUseDb': persistent._mas_apology_reason_use_db, # "NOT_AVAILABLE", # 
        ## script-ch30.rpy - 12th of May 2022
        'pd_monikaReload': persistent.monika_reload,
        'pd_triedSkip': persistent.tried_skip,
        'pd_monikaKill': persistent.monika_kill,
        'pd_firstRun': persistent.first_run,
        'pd_rejectedMonika': persistent.rejected_monika,
        'pd_masDisableAnimations': persistent._mas_disable_animations,
        ## script-fun-facts.rpy - 12th of May 2022
        'pd_masFunFactsDatabase': persistent._mas_fun_facts_database, # "NOT_AVAILABLE", # 
    ## script-holidays.rpy - COMING SOON
        ## script-islands-event.rpy - 12th of May 2022
        'pd_masIslandsStartLvl': persistent._mas_islands_start_lvl,
        'pd_masIslandsProgress': persistent._mas_islands_progress,
        'pd_masIslandsUnlocks': persistent._mas_islands_unlocks,
        ## script-songs.rpy - 12th of May 2022
        'pd_masSongDatabase': persistent._mas_songs_database, # "NOT_AVAILABLE", # 
        ## special-effects.rpy - 12th of May 2022
        'pd_masFirstKiss': persistent._mas_first_kiss, # "NOT_AVAILABLE", # 
        # 'pd_masFisrtKissBool': bool(persistent._mas_first_kiss),
        'pd_masLastKiss': persistent._mas_last_kiss, # "NOT_AVAILABLE", # 
        # 'pd_masLastKissBool': bool(persistent._mas_last_kiss),
    ## sprite-chart.rpy - COMING SOON
        ## styles.rpy - 12th of May 2022
        'pd_masDarkModeEnabled': persistent._mas_dark_mode_enabled,
        'pd_masAutoModeEnabled': persistent._mas_auto_mode_enabled,
        ## updater.rpy - 12th of May 2022
        'pd_masUnstableMode': persistent._mas_unstable_mode,
        'pd_masCanUpdate': persistent._mas_can_update,
        'pd_masJustUpdated': persistent._mas_just_updated,
        ## zz_backgrounds.rpy - 12th of May 2022
        'pd_masBackgroundMBGdata': persistent._mas_background_MBGdata,
        'pd_masCurrentBackground': persistent._mas_current_background,
        ## zz_backup.rpy - 12th of May 2022
        'pd_masIncompatPerForcedUpdate': persistent._mas_incompat_per_forced_update,
        'pd_masIncompatPerForceUpdateFailed': persistent._mas_incompat_per_forced_update_failed,
        'pd_masIncompatPerUserWillRestore': persistent._mas_incompat_per_user_will_restore,
        'pd_masIncompatPerRpyFilesFound': persistent._mas_incompat_per_rpy_files_found,
        'pd_masIncompatPerEntered': persistent._mas_incompat_per_entered,
        ## zz_consumables.rpy - 12th of May 2022
        'pd_masCurrenConsumable': persistent._mas_current_consumable,
        ## zz_dockingstation.rpy - 12th of May 2022
        'pd_masPmTakenMonikaOut': persistent._mas_pm_taken_monika_out,
        'pd_masMoniChksum': persistent._mas_moni_chksum,
        'pd_masDockstatCheckoutLog': persistent._mas_dockstat_checkout_log, # "NOT_AVAILABLE", # 
        'pd_masDockstatCheckinLog': persistent._mas_dockstat_checkin_log, # "NOT_AVAILABLE", # 
        'pd_masDockstatMoniLog': persistent._mas_dockstat_moni_log, # "NOT_AVAILABLE", # 
        'pd_masDockstatGoingToLeave': persistent._mas_dockstat_going_to_leave,
        'pd_masDockstatMoniSize': persistent._mas_dockstat_moni_size,
        'pd_masBdaySbpReacted': persistent._mas_bday_sbp_reacted,
        ## zz_extramenu.rpy - 12th of May 2022
        'pd_masOpenedExtraMenu': persistent._mas_opened_extra_menu,
        'pd_masPmZoomedOut': persistent._mas_pm_zoomed_out,
        'pd_masPmZoomedIn': persistent._mas_pm_zoomed_in,
        'pd_masPmZoomedInMax': persistent._mas_pm_zoomed_in_max,
        'pd_masPmBoopStats': persistent._mas_pm_boop_stats,
        ## zz_games.rpy - 12th of May 2022
        'pd_masGameDatabase': persistent._mas_game_database, # "NOT_AVAILABLE", # 
        ## zz_hangman.rpy - 12th of May 2022
        'pd_masHangmanPlayername': persistent._mas_hangman_playername,
        ## zz_history.rpy - 12th of May 2022
        'pd_masPmHasWentBackInTime': persistent._mas_pm_has_went_back_in_time,
        ## zz_music_selector.rpy - 12th of May 2022
        'pd_masPmAddedCustomBgm': persistent._mas_pm_added_custom_bgm,
        ## zz_pianokeys.rpy - 12th of May 2022
        'pd_masPnmlData': persistent._mas_pnml_data,
        'pd_masPianoKeymaps': persistent._mas_piano_keymaps,
        ## zz-poems.rpy - 12th of May 2022
        'pd_masPoemsSeen': persistent._mas_poems_seen, # "NOT_AVAILABLE", # 
        ## zz-seasons.rpy - 12th of May 2022
        'pd_masCurrentSeason': persistent._mas_current_season,
        ## zz_selector.rpy - 12th of May 2022
        'pd_masSelsprAcsDb': persistent._mas_selspr_acs_db, # "NOT_AVAILABLE", # 
        'pd_masSelsprHairDb': persistent._mas_selspr_hair_db, # "NOT_AVAILABLE", # 
        'pd_masSelsprClothesDb': persistent._mas_selspr_clothes_db, # "NOT_AVAILABLE", # 
        'pd_masSettingOcb': persistent._mas_setting_ocb,
        ## zz_spritejson.rpy - 12th of May 2022
        'pd_masSpritesJsonGiftedSprites': "Not Deserializeable.", # persistent._mas_sprites_json_gifted_sprites, # 
        ## zz_spriteobjects.rpy - 12th of May 2022
        'pd_masAcsEnableQuetzalplushie': persistent._mas_acs_enable_quetzalplushie,
        'pd_masAcsEnablePromisering': persistent._mas_acs_enable_promisering,
        ## zz_submods.rpy - 12th of May 2022
        'pd_masSubmodVersionData': persistent._mas_submod_version_data, # "NOT_AVAILABLE", # 
        ## zz_weather.rpy - 12th of May 2022
        'pd_masCurrentWeather': persistent._mas_current_weather,
        'pd_masWeatherMWdata': persistent._mas_weather_MWdata,
        'pd_masDateLastCheckedRain': persistent._mas_date_last_checked_rain, # "NOT_AVAILABLE", # 
        'pd_masShouldRainToday': persistent._mas_should_rain_today,
        ## zz-windowutils.rpy - 12th of May 2022
        'pd_masEnableNotifications': persistent._mas_enable_notifications,
        'pd_masNotificationSounds': persistent._mas_notification_sounds,
        'pd_masWindowReactsWindowReactsEnabled': persistent._mas_windowreacts_windowreacts_enabled,
        'pd_masWindowReactsDatabase': persistent._mas_windowreacts_database, # "NOT_AVAILABLE", # 
        'pd_masWindowReactsNoUnlockList': persistent._mas_windowreacts_no_unlock_list,
        'pd_masWindowsReactsNotifFilters': persistent._mas_windowreacts_notif_filters, # "NOT_AVAILABLE", # 
        ## custom.extension
        '0generatedAt': pd_time.time(),
        '0madeBy': "Carslo_45",
        '0submodVersion': "0.6.1",
        "1gamePath": config.basedir
        ## Submod Implementations: Maybe Soon.
        }

        pd_write = json.dumps(pd_allData,
                            indent = 4,
                            separators = (", ", ": "),
                            sort_keys = True,
                            default=str
                            )

        with open(os.getenv('APPDATA') + "/RenPy/Monika After Story/pdreader.json","w+") as pd_file:
            pd_file.write(pd_write)
