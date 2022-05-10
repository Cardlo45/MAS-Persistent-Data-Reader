# Register the submod
init -990 python:
    store.mas_submod_utils.Submod(
        author="Carslo_45",
        name="Persistent Data Reader",
        description="A Submod to access the Persistent Data (READ-ONLY)",
        version="0.0.1",
        settings_pane="PDReaderSettingsPanel"
    )

# Register the updater
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Persistent Data Reader",
            user_name="Cardlo45",
            repository_name="MAS-Persistent-Data-Reader"
        )

# # Add Placeholder Setting Screen
# init -5:
#     screen PDReaderSettingsPanel():
#         vbox:
#             #xmaxinum 800
#             xfill True

#             # Toggle File Generation, Default = False
#             text "Settings Panel Test."

# Get Persistent Data
init 100:
    python:
        getPersistentData()
        store.mas_submod_utils.registerFunction("quit",getPersistentData)

init python:
    def getPersistentData():
        import os
        import json
        # PDReader.KEYVALUE = persistent.VALUE
        
        allData = {
        # chess.rpy - 10th of May 2022
        'pd_masChessStats': persistent._mas_chess_stats,
        'pd_masChessDifficulty': persistent._mas_chess_difficulty,
        'pd_masChessQuicksave': persistent._mas_chess_quicksave,
        'pd_masChessDlgAction': persistent._mas_chess_dlg_action,
        'pd_masChessTimedDisable': persistent._mas_chess_timed_disable,
        'pd_masChess3EditSorry': persistent._mas_chess_3_edit_sorry,
        'pd_masChessMangleAll': persistent._mas_chess_mangle_all,
        'pd_masChessSkipFileChecks': persistent._mas_chess_skip_file_checks,

        # definitions.rpy - 10th of May 2022
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
        #'pd_eventDatabase': persistent.event_database,
        #'pd_farewellDatabase': persistent.farewell_database,
        #'pd_greetingDatabase': persistent.greeting_database,
        #'pd_masApologyDatabase': persistent._mas_apology_database,
        #'pd_masUndoActionRules': persistent._mas_undo_action_rules,
        #'pd_masStripDatesRules': persistent._mas_strip_dates_rules,
        'pd_gender': persistent.gender,
        'pd_closedSelf': persistent.closed_self,
        'pd_masGameCrashed': persistent._mas_game_crashed,
        'pd_seenMonikaInRoom': persistent.seen_monika_in_room,
        'pd_masEverWon': persistent._mas_ever_won # definitions.rpy:7900
        }

        write = json.dumps(allData,
                            indent = 4,
                            separators = (", ", ": "),
                            sort_keys = True)

        with open(os.getenv('APPDATA') + "/RenPy/Monika After Story/pdreader.json","w+") as file:
            file.write(write)