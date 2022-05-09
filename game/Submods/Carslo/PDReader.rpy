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

init -5 python:
    class PDReader(object):
        def __init__(
            self,
            affection,
            nicknames,
            fisrstKiss
        ):
            self.affection = 0
            self.nicknames = ["my Love","my Dear"]
            self.fisrstKiss = false
init -5:
    screen PDReaderSettingsPanel():
        vbox:
            xmaxinum 800
            xfill True

            text "Settings Panel Test."

init 100 python:
    # PDReader.KEYVALUE = persistent.VALUE