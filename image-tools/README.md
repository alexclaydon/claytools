# Image Tools Readme

## im-convert-exr-png.sh

Converts all `.exr` files in the target directory to `.png` files using ImageMagick's `convert` command.  Also performs correct colorspace conversion.  Designed for convenient usage with `.exr` files output by Unreal Engine 5.1's Movie Render Queue.

### Setup

- Install additional dependencies: `brew install imagemagick ghostscript`
- Ensure that the script is executable: `chmod +x im-convert-exr-png.sh`

### Usage

Before using, ensure there are no illegal characters in your filenames, else `convert` will fail with a cryptic message.

`./im-convert-exr-png.sh <IMAGE_WORKING_DIR>`

If no argument is passed, the script will first look for an environment variable called `IMAGE_WORKING_DIR` and if that is not set, it will default to my usual render output directory, `~/ShareDir/Renders`.

## autoshoot-desktop.sh

### Setup

- Ensure that the script is executable: `chmod +x autoshoot-desktop.sh`

### Scheduling with `launchctl`

The directory includes a working `.plist` file, `com.autoshoot.agent.plist`.  You can customize the `StartInterval` key to set screenshotting interval.

Note that despite reading that it was possible to pass environment variables to `launchctl` using the `LSEnvironment` key in a `.plist` file, I was unable to get this to work and read conflicting things about whether it was still possible at all.  As a workaround I'll just be passing any environment variables I need to the script itself as arguments.  This will apply for any other script that I want to schedule with `launchctl` in future.

There seems to be no need to copy or symlink this file to `~/Library/LaunchAgents` - it can be loaded directly from the repo directory as follows: `launchctl load com.autoshoot.agent.plist`, which for legibility reasons is my current preference during local development.  To unload, `launchctl load com.autoshoot.agent.plist`.

However, due to MacOS security settings, `/bin/zsh` needs to be added to the `Screen Recording` permissions in order for the script to capture anything other than the desktop background.  This is a security risk and one that I'll need to address in due course.
