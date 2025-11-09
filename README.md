# MCP_DiscordBot

# Discord

## Step 1: Find or create a Discord Server
  Regarding discord I first created a new server in order to experiement there first.
  Open Discord. <br>
  
  Log in to your account (or create one if you don’t have one).
  Click the “+” icon on the left sidebar.
  It’s usually labeled “Add a Server.”
  Choose “Create My Own.”
  Enter a server name of your choice.
  Click Create.

## Step2: Create a Discord bot

  Go to the [Discord Developer Portal]([https://github.com/EleniChristopoulou/DVWA_Initial_Setup-/tree/main](https://discord.com/developers/applications])
  
  Click “New Application.”
  
  Give it a name of your choice and click Create
  In the left sidebar, click “Bot.”
  Click “Add Bot.”
  You’ll see a section with your bot’s name, icon, and token (important!).
  ⚠️ Never share your bot token — it’s like a password. <br>

  Click “Reset Token” (if needed), then Copy Token. Paste it temporarily in a txt local file.
  In the left sidebar, go to “OAuth2 → URL Generator.”
  Under Scopes, check ✅ bot.
  Lastly do not forget to activate the following.

  <p align="center"> <img width="750" height="255" alt="image" src="https://github.com/user-attachments/assets/d207bf2a-030c-4c72-87bc-6027e2a7c7e3" /></p>
  Finally do not forget to save the changes!
  
## Step3: 
  
  Under Bot Permissions, choose what your bot should be allowed to do (e.g., Send Messages, Manage Roles, etc.). I personally gave permissions of an admin, not the best practice, it is just to make sure it's working.
  
  Copy the generated URL, paste it into your browser, and choose the server to invite your bot to.
  You’ll need this to connect your bot’s code to Discord.

  Finally we need to more IDs for our script to work, GUILD ID and CHANNEL ID, to get them first we: <br>
  Click the ⚙️ gear icon (bottom-left corner) — that’s User Settings.
  Scroll down the left sidebar to the “App Settings” section.
  Click “Advanced.”
  Turn on the switch for Developer Mode. ✅ <br>

  Go to your server in Discord.
  Right-click on the server name or icon (in the left sidebar).
  Select “Copy Server ID.” Paste it in the txt where our token is.

  Lastly:
  Open your server.
  Right-click on the channel name (in the sidebar).
  Click “Copy Channel ID.” Paste it in the txt as well.
  
# Visual Studio Code  
  
## Script
  Now it the part where we 'll download the script locally
  Right-click on the server name or icon (in the left sidebar).
  Select “Copy Server ID.” Paste it temporarily in the smae txt file, our token is.

    When opening the Visual Studio Code
  we 'll now make a directory just for our project.

  ```mkdir 'NameOfMyDir'``` <br>
  ```cd 'NameOfMyDir'```

  Now we copy the script into the directory.
  It's time to paste our vaules in! 
  Do not forget to get rid ofthe txt file now.

  <p align="center"> <img width="660" height="335" alt="image" src="https://github.com/user-attachments/assets/48d2d8a6-8c3a-4bee-ad8a-3951402e0096" /> </p>

  ```python -m venv devenv``` <br>
  ```Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned``` <br>
  ```./devenv/Scripts/activate``` <br>
  ```pip install mcp mcp[cli]``` <br>
  ```mcp dev server.py``` (Server.py is the name of my scirpt btw.

  A page opens after that: We input the following parameters and click  `Connect` <br>
  <p align="center"> <img width="265" height="305" alt="image" src="https://github.com/user-attachments/assets/0e30c752-eaba-49f7-94cf-2c940db88273" /> </p>

  Now our server is up and running!
  Lastly we need to integrate with our LLM, I'll be using Claude Desktop.

  # Claude Desktop
