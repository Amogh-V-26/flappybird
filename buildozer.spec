[app]

title = Flappy Bird

package.name = flappybird

package.domain = org.amogh

source.dir = .

source.include_exts = py,png,jpg,jpeg,gif,bmp,ttf,otf,wav,ogg,mp3,json,txt

version = 1.0

requirements = python3,pygame

orientation = portrait

fullscreen = 0


[buildozer]

log_level = 2


[android]

android.api = 35

android.minapi = 23

android.ndk = 25b

android.build_tools_version = 35.0.0

android.archs = arm64-v8a

android.accept_sdk_license = True
