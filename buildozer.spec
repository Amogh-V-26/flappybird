[app]

title = Flappy Bird

package.name = flappybird
package.domain = org.amogh

source.dir = .

source.include_exts = py,png,jpg,jpeg,wav,mp3,ttf,ogg

version = 1.0

requirements = python3==3.11,pygame==2.6.1

orientation = portrait

fullscreen = 0

android.api = 33
android.minapi = 24
android.ndk = 28c

android.archs = arm64-v8a, armeabi-v7a

android.private_storage = True

p4a.branch = master

android.accept_sdk_license = True

android.permissions = INTERNET


[buildozer]

log_level = 2
warn_on_root = 1
