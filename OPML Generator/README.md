# Podcast OPML Generator

A local OPML generator meant for podcasts. Simply input a text file with the links to the RSS feeds for the podcasts and it will generate the OPML file for you, which can be read by your podcast reader of choice.


## Usage/Examples

Create a file including the RSS links. For this example, we will use the following:

```text
https://feeds.transistor.fm/breadcrumbs-by-trace-labs
https://feeds.megaphone.fm/cyberwire-daily-podcast
https://feeds.megaphone.fm/darknetdiaries
https://feeds.megaphone.fm/hackedpodcast
https://feeds.soundcloud.com/users/soundcloud:users:261098918/sounds.rss
https://feeds.fireside.fm/selfhosted/rss
```

From there, you just run the script:

```bash
python3 script.py input.txt
```
There should be a new file created called `output.xml`. The following is "beautified" by running `cat output.xml | xmllint --format -`.

```xml
<?xml version="1.0"?>
<opml xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>Podcast Feed</title>
  </head>
  <body>
    <outline text="feeds">
      <outline type="rss" text="Breadcrumbs by Trace Labs" description="Trace Labs is a Canadian based non profit specializing in the crowd sourcing of open source intelligence collection. &#10;&#10;In this series, we explore the topics, techniques and tools that relate to OSINT collection. " xmlUrl="https://feeds.transistor.fm/breadcrumbs-by-trace-labs"/>
      <outline type="rss" text="CyberWire Daily" description="The daily cybersecurity news and analysis industry leaders depend on. Published each weekday, the program also includes interviews with a wide spectrum of experts from industry, academia, and research organizations all over the world." xmlUrl="https://feeds.megaphone.fm/cyberwire-daily-podcast"/>
      <outline type="rss" text="Darknet Diaries" description="Explore true stories of the dark side of the Internet with host Jack Rhysider as he takes you on a journey through the chilling world of hacking, data breaches, and cyber crime." xmlUrl="https://feeds.megaphone.fm/darknetdiaries"/>
      <outline type="rss" text="Hacked" description="Strange tales of hacking, tech, internet grifters, AI, and security with Jordan &amp; Scott.&#xA0;Are internet hitmen really a thing?&#xA0;What does someone do with a crypto wallet full of millions and a lost password?&#xA0;Did a Minecraft scammer really hack the president?&#xA0;Hacked is a technology show about people hacking things together and apart, with your old pals Jordan Bloemen and Scott Francis Winder." xmlUrl="https://feeds.megaphone.fm/hackedpodcast"/>
      <outline type="rss" text="The Privacy, Security, &amp; OSINT Show" description="Show status update: https://inteltechniques.com/blog/2023/11/20/my-irish-exit/" xmlUrl="https://feeds.soundcloud.com/users/soundcloud:users:261098918/sounds.rss"/>
      <outline type="rss" text="Self-Hosted" description="Discover new software and hardware to get the best out of your network, control smart devices, and secure your data on cloud services. Self-Hosted is a chat show between Chris and Alex two long-time &quot;self-hosters&quot; who share their lessons and take you along for the journey as they learn new ones.&#10; A Jupiter Broadcasting podcast showcasing free and open source technologies you can host yourself.&#10;" xmlUrl="https://feeds.fireside.fm/selfhosted/rss"/>
    </outline>
  </body>
</opml>

```

From here you can import into your favorite podcast reader that allows for importing subscriptions in OPML format.
