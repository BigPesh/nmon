# Nmon
Python Network Monitor

[![CleanShot 2022-12-30 at 18.49.06@2x](https://i.im.ge/2022/12/31/qZ6UPS.CleanShot-2022-12-30-at-18-49-062x.md.png)](https://im.ge/i/qZ6UPS)

So not so long back my sister's husband asked me to write a little app to monitor his Internet connection to prove to his ISP that he actually had an issue with his line. He used the app to produce logs to the engineer, which they could not argue with and had to act on.

The app which I wrote about in another post here, was a CLI application which was ok as I wrote it in a night and he needed it quick so there was no time to knock up a nice GUI.

I have now spent a little time on this little app and re-wrote it from the ground up including a nice little GUI.

[![CleanShot 2022-12-30 at 18.49.20@2x](https://i.im.ge/2022/12/31/qZ6DJJ.CleanShot-2022-12-30-at-18-49-202x.md.png)](https://im.ge/i/qZ6DJJ)

So what does this new `Nmon` application actually do? (the below are all real-time)

- Total MBs sent (current session)
- Total MBs recieved (current session)
- Current DL Speed (MB/s)
- Current UL Speed (MB/s)
- Monitors connection 
- Logs all speeds
- Logs all connection errors (with date and time stamps)

`Nmon` (when running) will always keep checking the state of your connection the second there is an issue like a disconnect it will be logged in the data sheet, `Nmon` will also visually alert you with a bright red background.

[![CleanShot 2022-12-30 at 18.50.16@2x](https://i.im.ge/2022/12/31/qZ6hfz.CleanShot-2022-12-30-at-18-50-162x.md.png)](https://im.ge/i/qZ6hfz)

The idea behind `Nmon` is to leave it running on the machine you are having issue with Internet connection and be able to pick up the patterns of your issues and provide them to your ISP. `Nmon` logs each check it does (this will keep going the whole time `Nmon` is running) you can then load the Data Sheet to see your data.

[![CleanShot 2022-12-30 at 18.51.53@2x](https://i.im.ge/2022/12/31/qZ6Ldy.CleanShot-2022-12-30-at-18-51-532x.png)](https://im.ge/i/qZ6Ldy)
