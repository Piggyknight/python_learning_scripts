# -*- coding:utf-8 -*-

from report_enum import *
import re



class ModuelParserSimple:
    def __init__(self):
        self._default = ModuleType.none

    def Parse(self, name, module_type):
        return self._default

class ModuleParser(ModuelParserSimple):
    '''
        1. _db is key string map to ResType
    '''
    def __init__(self):
        super().__init__()
        self._db ={}
    
    def Parse(self, name, module_type):
        for key, res_type in self._db.items():
            if key in name:
                return res_type

        return self._default

class ModuleParserReg(ModuleParser):
    def __init__(self):
        super().__init__()
        self._db = {}
        self._default = ModuleType.none
        self._re_str='*'
        self._re_type = ModuleType.none

    def Parse(self, name, module_type):
        # 1. first using key word to remove simple case
        for key, res_type in self._db.items():
            if key in name:
                return res_type

        # 2. use re to find monster char res
        ret = re.match(self._re_str, name)
        if None != ret:
            return self._re_type
            
        # 3. then all the left posbility is scene
        return self._default

class ModuleParseTex(ModuelParserSimple):
    def Parse(self, name, module_type):
        return module_type
  
'''
 Used to parse mesh res and decide which module it belongs to
'''
class ModuleParserMesh(ModuleParserReg):
    def __init__(self):
        super().__init__()
        self._db = {"avatar":ModuleType.char
                       ,"[NGUI]":ModuleType.ui
                       ,"fx_":ModuleType.effect}
        self._default = ModuleType.scene
        # math pattern: m00800 
        self._re_str='^m\d{5}'
        self._re_type = ModuleType.char

    

class ModuleParseTransform(ModuleParserReg):
    def __init__(self):
        super().__init__()
        self._db = {"avatar":ModuleType.char
                    ,"empty_actor":ModuleType.char
                    ,"SoundDummy":ModuleType.audio
                    ,"fx_":ModuleType.effect
                    ,"UI Root":ModuleType.ui
                    ,"ingame_":ModuleType.ui
                    ,"story":ModuleType.ui
                    ,"dialog_":ModuleType.ui
                    ,"home_npc_name_new":ModuleType.ui}
        self._default = ModuleType.scene

        # match pattern: m00080 or pc0020
        self._re_str='(^m\d{5})|(^pc\d{4})'
        self._re_type = ModuleType.char
    
class ModuleParseMaterial(ModuleParserReg):
    def __init__(self):
        super().__init__()
        self._db = {"avatar":ModuleType.char
                    ,"fx_":ModuleType.effect
                    ,"Particle":ModuleType.effect
                    ,"ui_":ModuleType.ui
                    ,"[NGUI]":ModuleType.ui
                    ,"Font":ModuleType.ui}
        self._default = ModuleType.scene

        # math pattern: m00800 
        self._re_str='^m\d{5}'
        self._re_type = ModuleType.char

    
class ModuleParseAnimator(ModuleParserReg):
    def __init__(self):
        super().__init__()
        self._db = {"fx_ui_":ModuleType.ui
                    ,"fx_":ModuleType.effect
                    ,"ingame_":ModuleType.ui}
        self._default = ModuleType.scene

        # match pattern: m00080 or pc0020
        self._re_str='(^m\d{5})|(^pc\d{4})'
        self._re_type = ModuleType.char

class ModuleParseAnimCtrl(ModuleParserReg):
    def __init__(self):
        super().__init__()
        self._db = {"fx_ui_":ModuleType.ui
                    ,"ingame_":ModuleType.ui
                    ,"fx_":ModuleType.effect
                    ,"cp_":ModuleType.cutscene}
        self._default = ModuleType.scene

        # match pattern: m00080 or pc0020
        self._re_str='(^m\d{5})|(^pc\d{4})'
        self._re_type = ModuleType.char


class NameAnalyzers:
    def __init__(self):
        self._db={}
        
        # Texture2D
        self._db[ResType.Texture2D] = ModuleParseTex()

        # animation clip 
        mp_anim_clip = ModuleParser()
        mp_anim_clip._db = {"fx_":ModuleType.effect
                            ,"ingame_":ModuleType.effect
                            ,"ui_":ModuleType.ui}
        mp_anim_clip._default = ModuleType.char
        self._db[ResType.AnimationClip] = mp_anim_clip

        # AnimatorController
        mp_anim_ctrl = ModuleParser()
        mp_anim_ctrl._db = {"fx_":ModuleType.effect
                            ,"ingame_":ModuleType.ui
                            ,"cp_":ModuleType.cutscene}
        mp_anim_clip._default = ModuleType.char
        self._db[ResType.AnimatorController] = mp_anim_clip

        # mesh
        self._db[ResType.Mesh] = ModuleParserMesh()

        # transform
        self._db[ResType.Transform] = ModuleParseTransform()

        # Material
        self._db[ResType.Material]=ModuleParseMaterial()

        # MonoBehaviour
        mp_mb = ModuleParser()
        mp_mb._db = {"hud":ModuleType.ui}
        mp_mb._default = ModuleType.scene
        self._db[ResType.MonoBehaviour] = mp_mb
                
        #Animator
        self._db[ResType.Animator] = ModuleParseAnimator()

        #AnimatorCtrl
        self._db[ResType.AnimatorController]=ModuleParseAnimCtrl()

        # simple res to module map
        self._create_simple_parser(ResType.ParticleSystem, ModuleType.effect)
        self._create_simple_parser(ResType.ParticleSystemRenderer, ModuleType.effect)
        self._create_simple_parser(ResType.Cubemap, ModuleType.scene)
        self._create_simple_parser(ResType.RenderTexture, ModuleType.render_tex)
        self._create_simple_parser(ResType.AssetBundle, ModuleType.asset_bundle)
        self._create_simple_parser(ResType.Font, ModuleType.ui)
        self._create_simple_parser(ResType.AudioManager, ModuleType.audio)
        self._create_simple_parser(ResType.AudioClip, ModuleType.audio)

    def GetModuleType(self, name, res_type, module_type):
        if res_type not in self._db:
            print("[error]ResType not reg into the db, name:%s,res_type:%s,module type:%s" % (name, res_type, module_type))
            return module_type

        return self._db[res_type].Parse(name, module_type)
        

    def _create_simple_parser(self, res_type, model_type):
        mp_simple = ModuelParserSimple()
        mp_simple._default = model_type
        self._db[res_type] = mp_simple
