[app]

title = Flappy Bird

package.name = flappybird

package.domain = org.amogh

source.dir = .

source.include_exts = py,png,jpg,jpeg,mp3,wav,ogg,ttf

version = 1.0

requirements = python3,pygame

orientation = portrait

fullscreen = 0


[buildozer]

log_level = 2


[android]

android.api = 33

android.minapi = 24

android.archs = arm64-v8a,armeabi-v7a

android.ndk = 28c

android.accept_sdk_license = True


[p4a]

p4a.bootstrap = sdl2
