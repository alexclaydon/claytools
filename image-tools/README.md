## Scheduling with `launchctl`

The directory includes a working `.plist` file, `com.autoshoot.agent.plist`.  You can customize the `StartInterval` key to set screenshotting interval.

Note that despite reading that it was possible to pass environment variables to `launchctl` using the `LSEnvironment` key in a `.plist` file, I was unable to get this to work and read conflicting things about whether it was still possible at all.  As a workaround I'll just be passing any environment variables I need to the script itself as arguments.  This will apply for any other script that I want to schedule with `launchctl` in future.

There seems to be no need to copy or symlink this file to `~/Library/LaunchAgents` - it can be loaded directly from the repo directory as follows: `launchctl load com.autoshoot.agent.plist`, which for legibility reasons is my currnet preference.

However, due to MacOS security settings, `/bin/zsh` needs to be added to the `Screen Recording` permissions in order for the script to capture anything other than the desktop background.  This is a security risk and one that I'll need to address in due course.
