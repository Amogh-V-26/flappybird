[app]

title = Flappy Bird
package.name = flappybird
package.domain = org.amogh

source.dir = .
source.include_exts = py,png,jpg,jpeg,gif,bmp,ttf,otf,wav,ogg,mp3,json,txt

version = 1.0

requirements = python3,pygame

orientation = portrait

fullscreen = 1

android.api = 33
android.minapi = 24
android.ndk = 28c

android.archs = arm64-v8a, armeabi-v7a

android.accept_sdk_license = True
android.skip_update = True

android.permissions = INTERNET

log_level = 2

# Leave blank unless you have Java/Kotlin code
android.add_src =

# Icons (optional)
# icon.filename = icon.png
# presplash.filename = presplash.png


[buildozer]

log_level = 2
warn_on_root = 1
