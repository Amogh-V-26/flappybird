[app]

# (str) Title of your application
title = Flappy Bird

# (str) Package name
package.name = flappybird

# (str) Package domain
package.domain = org.amogh

# (str) Source code directory
source.dir = .

# (list) Source file extensions to include
source.include_exts = py,png,jpg,jpeg,mp3,wav,ttf,ogg

# (str) Application version
version = 1.0

# (list) Application requirements
requirements = python3,pygame==2.6.1

# (str) Supported orientations
orientation = portrait

# (bool) Fullscreen mode
fullscreen = 0


[buildozer]

# (int) Log level
log_level = 2


[android]

# (str) Android API target
android.api = 33

# (str) Minimum Android API
android.minapi = 24

# (list) Architectures
android.archs = arm64-v8a,armeabi-v7a

# (bool) Copy libraries
android.copy_libs = 1

# (str) NDK version
android.ndk = 28c

# (str) Enable backup
android.allow_backup = True


# (bool) Enable Android permissions
android.permissions = INTERNET


[p4a]

# Avoid Python version mismatch
p4a.bootstrap = sdl2
