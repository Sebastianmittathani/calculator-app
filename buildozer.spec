[app]

# App Information
title = Calculator
package.name = calculator
package.domain = org.sebastian

# Source
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv

version = 1.0

# Requirements
requirements = python3,kivy

# Orientation
orientation = portrait

fullscreen = 0

# Android Settings
android.api = 34
android.minapi = 21
android.sdk = 33
android.ndk = 26b

# Architectures
android.archs = arm64-v8a, armeabi-v7a

# Permissions
android.permissions = INTERNET

# Entry Point
entrypoint = main.py

# Presplash/Icon (optional)
# presplash.filename = %(source.dir)s/data/presplash.png
# icon.filename = %(source.dir)s/data/icon.png


[buildozer]

log_level = 2
warn_on_root = 1
