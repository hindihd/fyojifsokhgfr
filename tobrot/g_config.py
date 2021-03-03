from tobrot.sample_config import Config

#Fill your all data, read readme for reference

#FOR CUSTOM COMMANDS READ REAME AND FILL THEM...

class Config(Config):
    TG_BOT_TOKEN= "1619230023:AAHq0gQi5ZtHOhDkuEwu1uGPBpKBadWEL7w"
    APP_ID = 1858153
    API_HASH = "5fb9328cdf9a7aaad5fed030484d6022"
    OWNER_ID = 1196519780
    AUTH_CHANNEL = [-1001277862770]
    DESTINATION_FOLDER = "TorrentLeech-Gdrive" #Name of your folder read readme(not id of the folder)
    #Just don't fill RCLONE_CONFIG vars, insted copy your rclone.conf file in root directory
    #if your wanted to fill -- fill your rclone config like this(Your config may have some extra value or less. so Don't worry)
    RCLONE_CONFIG = """
[DRIVE]
type = drive
client_id = 300413440647-mlrj042kekb7jdh74rkce4c7m1e4j055.apps.googleusercontent.com
client_secret = 5YIaUbk5IQ6jGHNU-xDMBhKF
scope = drive
root_folder_id = 1P5fDOtKmpazBN8bFz86_QOiSdQO0cmhr
token = {"access_token":"ya29.A0AfH6SMAoEU8Yxu-MGNgVkmvlAY4MctagrkGzYekIDpRIUE-S-yByaxb1LO8pYvrD95l4EantF4ppbOizOMmaFMEh9DuJ88L0dWT5DdTIrle2186bY52vbPA_VmSXe5mqf41qauNI290lKJ8IM6tIqWpJnQ47","refresh_token":"1//07wraeKRtD59PCgYIARAAGAcSNwF-L9Iru0elpfg6wZwxvdj-VqDUIEGFWWM4IbudGQvv_BtEL9qYUWRn6qH29t0wTWXstRB-hi8","scope":"https://www.googleapis.com/auth/drive.file https://www.googleapis.com/auth/drive.metadata.readonly","token_type":"Bearer","expiry_date":1614793995919}
team_drive = 0AB0q-fill-your-details-sdrgsgsdUk9PVA
"""
