#### unable to access DataStore from Studio
1. Go to the Develop page
2. Click on the Games tab and find your game
3. Click on the gear drop down and click "Configure"
4. Check the box labeled "Enable Studio Access to API Services:"

#### GUI text won't change
The StarterGui is the gui setup that is copied into the playergui when you respawn.  
    `guiText = game.Players.LocalPlayer.PlayerGui.ScreenGui.TextLabel.Text`

#### PlayerGui is not a valid member of Player  
probably, the code was running before the PlayerGui loaded. Deed `WaitForChinld(name)`  
    `playerr:WaitForChild("PlayerGui").ScreenGui`

#### P4V A given file is missing from my Workspace, but present at the Perforce Depot.  
    use the "Get Revision..." item and in the subsequent dialog, you can check the "force operation" checkbox
