# Autopush VAPID tests

This repository contains an automated test for verifying VAPID functionality
works correctly on Android devices.

## Prerequisites

You need to having the following things installed:

* Android Studio for your platform
* The Android SDK installed
* Python 2.7.15
* an APK of a version of Firefox that supports Marionette

## Pre-test Configuration

Once you have Android Studio installed, you will need to use
the AVD Manager to install an Android emulator for the purposes
of testing.

During development of these tests a "Pixel API 22" virtual device
was used.

With the emulator running you then need to use the `adb` CLI tool
from the Android SDK to load your Firefox APK into the system. You
can use the following command:

`/path/to/adb install /path/to/Firefox.apk`

This will add the APK to your virtual device.

You then need to use `adb` to forward your local TCP port of 2828
to the virtual device so that Marionette can control the browser.

`/path/to/adb forward tcp:2828 tcp:2828`

## Running the tests

To run the tests use the following command:

`pytest tests/`
