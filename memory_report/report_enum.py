# -*- coding:utf-8 -*-

from enum import Enum

class ResType(Enum):
    none = 0
    Texture2D = 1
    Cubemap = 2
    RenderTexture = 3
    Mesh = 4
    Material=5
    AnimationClip=6
    Animator=7
    AnimatorController=8
    ParticleSystemRenderer=9
    ParticleSystem=10
    AssetBundle=11
    MonoBehaviour=12
    Transform=13
    GameObject=14
    MonoScript=15
    AudioClip=16
    AudioManager=17
    Font=18


class ModuleType(Enum):
    none=0
    scene=1
    char=2
    effect=3
    ui=4
    misc=5
    audio=6
    cutscene=7
    render_tex=8
    asset_bundle=9

class SGType(Enum):
    Character=0
    Scene=1
    UI=2
    building=3
    Effect=4
    NotFound=5
    ImageEffect=6
    Other=7
    water=8


class LineType(Enum):
    none=0
    total_size=1
    group=2
    split_group=3
    data=4
