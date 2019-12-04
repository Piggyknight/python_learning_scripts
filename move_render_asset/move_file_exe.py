from scene_file import Scene, SceneDb
import shutil,os


_root = 'd:\\perforce_art\\Client\\trunk\\Scenes\\raw\\'
_conf_root_folder = _root + 'art_map_conf\\'
_old_folder = _root + '%s\\%s\\%s_render_asset.txt'
_new_folder= _root + '%s\\%s\\%s_render_asset.txt'

def unittest_read_all_scene(scene_root):
    # unit test to read all the scene in the root folder
    # and print the resutl
    scene_db = SceneDb()
    scene_db.Load(scene_root)
    print(scene_db.__str__())

def _move_to(src, dst):
    if os.path.exists(src):
        shutil.move(src,dst)
        #print("Move %s to %s " %(src, dst))

def move_file_exe(scene_root):
    #1. read all scene file
    scene_db = SceneDb()
    scene_db.Load(scene_root)

    #2. loop all file to check if exist level/sub/main/main_render_asset.txt
    for s in scene_db._all_scenes:
        day_file = _old_folder % (s._level, s._sub, s._day)
        day_file_dst = _new_folder % (s._level, s._day, s._day)

        night_file = _old_folder % (s._level, s._sub, s._night)
        night_file_dst = _new_folder % (s._level, s._sub, s._night)

        # move both day & night file
        _move_to(day_file, day_file_dst)
        _move_to(night_file, night_file_dst)
            
    
move_file_exe(_conf_root_folder)


#unittest_read_all_scene(_conf_root_folder)