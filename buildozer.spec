[app]
title = El Cubo Que Salta
package.name = cuboquesalta
package.domain = org.cuboquesalta
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,pygame==2.5.2
orientation = portrait
fullscreen = 0
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
p4a.bootstrap = sdl2
android.accept_sdk_lisense = True
icon.filename = icon.png

[buildozer]
log_level = 2
warn_on_root = 1
