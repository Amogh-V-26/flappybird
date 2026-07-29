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

android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/27.3.13750724

android.api = 33
android.minapi = 24

android.archs = arm64-v8a,armeabi-v7a

android.permissions = INTERNET

[buildozer]

log_level = 2
warn_on_root = 0
