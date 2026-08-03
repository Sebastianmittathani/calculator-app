[app]

title = Calculator
package.name = calculator
package.domain = org.sebastian

source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,ttf

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a

[buildozer]

log_level = 2
warn_on_root = 1