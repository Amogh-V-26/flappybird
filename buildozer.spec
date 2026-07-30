[app]

# (str) Title of your application
title = Flappy Bird

# (str) Package name
package.name = flappybird

# (str) Package domain
package.domain = org.amogh

# (str) Source code where main.py lives
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,jpeg,gif,bmp,ttf,otf,wav,ogg,mp3,json,txt

# (str) Application version
version = 1.0

# (list) Requirements
requirements = python3,pygame

# (str) Supported orientations
orientation = portrait

# (bool) Fullscreen mode
fullscreen = 0


[buildozer]

# (int) Log level
log_level = 2


[android]

# (bool) Indicate if the application should be fullscreen
fullscreen = 0

# (str) Android API
android.api = 35

# (str) Minimum API
android.minapi = 23

# (str) NDK version
android.ndk = 25b

# (bool) Enable Android permissions
android.accept_sdk_license = True

# (list) Permissions
# android.permissions = INTERNET

# (str) Android architecture
android.archs = arm64-v8a

# (str) Entry point
android.entrypoint = org.kivy.android.PythonActivity
