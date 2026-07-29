[app]

title = flappybird

package.name = flappybird
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,jpeg,wav,mp3,ttf

version = 1.0

requirements = python3,pygame

orientation = portrait

fullscreen = 0

android.archs = arm64-v8a,armeabi-v7a

android.api = 33
android.minapi = 24

android.permissions = INTERNET

[buildozer]

log_level = 2
warn_on_root = 0
