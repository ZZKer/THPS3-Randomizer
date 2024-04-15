console.log('Start.')
gui.text(100,50,"Loading...")

local stateadd = 0x0BF454
local pauseadd = 0x0D56A8
local menuon = false
local menuID = -1
local optionID = 0

local leveladd1 = 0x0D6360
local leveladd2 = 0x0D856C
local levelchoice = 0
local levels = {}
levels[0] = "Foundry"
levels[1] = "Los Angeles"
levels[2] = "Rio de Janeiro"
levels[3] = "Suburbia"
levels[4] = "Airport"
levels[5] = "Skater Island"
levels[6] = "Canada"
levels[7] = "Tokyo"
levels[8] = "Downhill"
levels[9] = "Disabled"
local maxLevel = 9

local cheatadd = {}
cheatadd["Perfect Balance"] = 0xBCA2A
cheatadd["Infinite Special Bar"] = 0xBCA2E
cheatadd["Wireframe"] = 0xBCA3A
cheatadd["Slow Motion"] = 0xBCA3E
cheatadd["Smooth Mode"] = 0xBCA4A
cheatadd["Moon Physics"] = 0xBCA52
cheatadd["Turbo"] = 0xD64D8
cheatadd["Disco"] = 0xD74F4
local maxCheat = 7

local FRAMES_PER_SECOND = 60
local select = "P1 Select"
local L1 = "P1 L1"
local L2 = "P1 L2"
local R1 = "P1 R1"
local R2 = "P1 R2"
local framecount = {}
framecount[select] = 0
framecount[L1] = 0
framecount[L2] = 0
framecount[R1] = 0
framecount[R2] = 0
framecount["Startup"] = FRAMES_PER_SECOND * 5
framecount["Debug"] = FRAMES_PER_SECOND

local check = {}
check[0] = {}
check[0][-1] = "Foundry"
check[0][0] = {"High Score",0xBB720,0x01,false}
check[0][1] = {"Pro Score",0xBB720,0x02,false}
check[0][2] = {"Sick Score!",0xBB720,0x04,false}
check[0][3] = {"Collect SKATE",0xBB720,0x08,false}
check[0][4] = {"Valves Unjammed",0xBB720,0x10,false}
check[0][5] = {"Activate Press",0xBB720,0x20,false}
check[0][6] = {"Cannonball Over The Halfpipe",0xBB720,0x40,false}
check[0][7] = {"Grind The Control Booth",0xBB720,0x80,false}
check[0][8] = {"Find The Secret Tape",0xBB721,0x01,false}
check[0][9] = {"100% Goals, Stats, And Deck",0xBB721,0x02,false}
check[0][10] = {"SP Press",0xBB74C,0x01,false}
check[0][11] = {"SP Catwalk",0xBB74C,0x02,false}
check[0][12] = {"SP Left Control Booth Balcony",0xBB74C,0x04,false}
check[0][13] = {"SP Right Pipe",0xBB74C,0x08,false}
check[0][14] = {"SP Back Door",0xBB74C,0x10,false}
check[0][15] = {"Deck",0xBB750,0x20,false}
check[1] = {}
check[1][-1] = "Los Angeles"
check[1][0] = {"High Score",0xBB722,0x01,false}
check[1][1] = {"Pro Score",0xBB722,0x02,false}
check[1][2] = {"Sick Score!",0xBB722,0x04,false}
check[1][3] = {"Collect SKATE",0xBB722,0x08,false}
check[1][4] = {"Transformers Shutdown",0xBB722,0x10,false}
check[1][5] = {"Grind The Electric Rail",0xBB722,0x20,false}
check[1][6] = {"Elevator Grind",0xBB722,0x40,false}
check[1][7] = {"Kickflip Over Elevator Lobby",0xBB722,0x80,false}
check[1][8] = {"Find The Secret Tape",0xBB723,0x01,false}
check[1][9] = {"100% Goals, Stats, And Deck",0xBB723,0x02,false}
check[1][10] = {"SP Quarterpipe Powerline",0xBB754,0x01,false}
check[1][11] = {"SP Rooftop",0xBB754,0x02,false}
check[1][12] = {"SP Theater Quarterpipe",0xBB754,0x04,false}
check[1][13] = {"SP Building Powerline",0xBB754,0x08,false}
check[1][14] = {"SP Graffiti Wall Powerline",0xBB754,0x10,false}
check[1][15] = {"Deck",0xBB758,0x20,false}
check[2] = {}
check[2][-1] = "Rio de Janeiro"
check[2][0] = {"Bronze Medal",0xBB725,0x1C,false}
check[2][1] = {"Silver Medal",0xBB725,0x0C,false}
check[2][2] = {"Gold Medal",0xBB725,0x04,false}
check[2][10] = {"SP Powerline Behind Quicksilver",0xBB75C,0x01,false}
check[2][11] = {"SP Quicksilver Quarterpipe",0xBB75C,0x02,false}
check[2][12] = {"SP Wood Quarterpipe Powerline",0xBB75C,0x04,false}
check[2][13] = {"SP Alley",0xBB75C,0x08,false}
check[2][14] = {"SP Balcony",0xBB75C,0x10,false}
check[2][15] = {"Deck",0xBB760,0x20,false}
check[3] = {}
check[3][-1] = "Suburbia"
check[3][0] = {"High Score",0xBB726,0x01,false}
check[3][1] = {"Pro Score",0xBB726,0x02,false}
check[3][2] = {"Sick Score!",0xBB726,0x04,false}
check[3][3] = {"Collect SKATE",0xBB726,0x08,false}
check[3][4] = {"Appall The Appliances",0xBB726,0x10,false}
check[3][5] = {"Disrespect The Dishes",0xBB726,0x20,false}
check[3][6] = {"Ice The Ice Cream Man",0xBB726,0x40,false}
check[3][7] = {"360 Flip The Weathervane",0xBB726,0x80,false}
check[3][8] = {"Find The Secret Tape",0xBB727,0x01,false}
check[3][9] = {"100% Goals, Stats, And Deck",0xBB727,0x02,false}
check[3][10] = {"SP Flat Rooftop",0xBB764,0x01,false}
check[3][11] = {"SP Powerline",0xBB764,0x02,false}
check[3][12] = {"SP Above Mobile Home",0xBB764,0x04,false}
check[3][13] = {"SP Rooftop",0xBB764,0x08,false}
check[3][14] = {"SP Mobile Home Grind",0xBB764,0x20,false}
check[3][15] = {"Deck",0xBB768,0x10,false}
check[4] = {}
check[4][-1] = "Airport"
check[4][0] = {"High Score",0xBB728,0x01,false}
check[4][1] = {"Pro Score",0xBB728,0x02,false}
check[4][2] = {"Sick Score!",0xBB728,0x04,false}
check[4][3] = {"Collect SKATE",0xBB728,0x08,false}
check[4][4] = {"Snag The Flags",0xBB728,0x10,false}
check[4][5] = {"Lost Luggage Found!",0xBB728,0x20,false}
check[4][6] = {"Nosebluntslide The Airport Sign",0xBB728,0x40,false}
check[4][7] = {"Grind The Plane",0xBB728,0x80,false}
check[4][8] = {"Find The Secret Tape",0xBB729,0x01,false}
check[4][9] = {"100% Goals, Stats, And Deck",0xBB729,0x02,false}
check[4][10] = {"SP Light",0xBB76C,0x01,false}
check[4][11] = {"SP First Drop",0xBB76C,0x02,false}
check[4][12] = {"SP Security Checkpoint",0xBB76C,0x08,false}
check[4][13] = {"SP Sign",0xBB76C,0x10,false}
check[4][14] = {"SP Rail",0xBB76C,0x20,false}
check[4][15] = {"Deck",0xBB770,0x04,false}
check[5] = {}
check[5][-1] = "Skater Island"
check[5][0] = {"Bronze Medal",0xBB72B,0x1C,false}
check[5][1] = {"Silver Medal",0xBB72B,0x0C,false}
check[5][2] = {"Gold Medal",0xBB72B,0x04,false}
check[5][10] = {"SP Doorway Gap",0xBB774,0x01,false}
check[5][11] = {"SP Halfpipe",0xBB774,0x02,false}
check[5][12] = {"SP Doorway Rail",0xBB774,0x04,false}
check[5][13] = {"SP THPS3 Sign",0xBB774,0x08,false}
check[5][14] = {"SP Pool",0xBB774,0x10,false}
check[5][15] = {"Deck",0xBB778,0x20,false}
check[6] = {}
check[6][-1] = "Canada"
check[6][0] = {"High Score",0xBB72C,0x01,false}
check[6][1] = {"Pro Score",0xBB72C,0x02,false}
check[6][2] = {"Sick Score!",0xBB72C,0x04,false}
check[6][3] = {"Collect SKATE",0xBB72C,0x08,false}
check[6][4] = {"Totem Poles",0xBB72C,0x10,false}
check[6][5] = {"Blow Up The Tree",0xBB72C,0x20,false}
check[6][6] = {"Nosegrind Over The Tree",0xBB72C,0x40,false}
check[6][7] = {"Ollie Over The Pool",0xBB72C,0x80,false}
check[6][8] = {"Find The Secret Tape",0xBB72D,0x01,false}
check[6][9] = {"100% Goals, Stats, And Deck",0xBB72D,0x02,false}
check[6][10] = {"SP Rooftop",0xBB77C,0x01,false}
check[6][11] = {"SP Banner",0xBB77C,0x02,false}
check[6][12] = {"SP Train Tracks",0xBB77C,0x04,false}
check[6][13] = {"SP Park Rail",0xBB77C,0x08,false}
check[6][14] = {"SP Ramp",0xBB77C,0x20,false}
check[6][15] = {"Deck",0xBB780,0x10,false}
check[7] = {}
check[7][-1] = "Tokyo"
check[7][0] = {"Bronze Medal",0xBB72F,0x1C,false}
check[7][1] = {"Silver Medal",0xBB72F,0x0C,false}
check[7][2] = {"Gold Medal",0xBB72F,0x04,false}
check[7][10] = {"SP Breakable Glass",0xBB784,0x01,false}
check[7][11] = {"SP Left Quarterpipe",0xBB784,0x02,false}
check[7][12] = {"SP Bridge",0xBB784,0x04,false}
check[7][13] = {"SP Hologram Jump",0xBB784,0x08,false}
check[7][14] = {"SP Right Rail",0xBB784,0x10,false}
check[8] = {}
check[8][-1] = "Downhill"
check[8][0] = {"SP Trees",0xBB78C,0x01,false}
check[8][1] = {"SP Grind 1",0xBB78D,0x02,false}
check[8][2] = {"SP Grind 2",0xBB78D,0x01,false}
check[8][3] = {"SP Grind 3",0xBB78C,0x80,false}
check[8][4] = {"SP Grind 4",0xBB78C,0x10,false}
check[8][5] = {"SP Grind 5",0xBB78C,0x20,false}
check[8][6] = {"SP Grind 6",0xBB78C,0x40,false}
check[8][7] = {"SP Grind 7",0xBB78C,0x02,false}
check[8][8] = {"SP Grind 8",0xBB78C,0x04,false}
check[8][9] = {"SP Grind 9",0xBB78C,0x08,false}
local maxCheck = 8

for levelkey,innercheck in pairs(check) do
	for key,val in pairs(innercheck) do
		if key >= 0 and (memory.readbyte(val[2]) & val[3] > 0) then
			check[levelkey][key][4] = true
		end
	end
end

local mtable = {}
mtable[-1] = "Manual Menu"
mtable[0] = {}
mtable[0][-1] = "Level Menu"
for key,val in pairs(levels) do
	mtable[0][key] = val
end
mtable[1] = {}
mtable[1][-1] = "Cheat Toggle"
local x = 0
for key,val in pairs(cheatadd) do
	mtable[1][x] = key
	x = x + 1
end
mtable[2] = {}
mtable[2][-1] = "Location Tracker"
local maxOption = 2

x = 50
function gameloop()
	-- If not currently skating
	if memory.readbyte(stateadd) == 0 or memory.readbyte(pauseadd) == 1 then
		-- Set level correctly (need to fix up in future)
		if memory.readbyte(stateadd) == 0 and levelchoice < maxLevel and (memory.readbyte(leveladd1) ~= levelchoice or memory.readbyte(leveladd2) ~= levelchoice) then
			memory.writebyte(leveladd1, levelchoice)
			memory.writebyte(leveladd2, levelchoice)
		end
		
		-- Get input data
		local pad = joypad.getimmediate()
		
		if menuon then
			-- Display controls for menu
			gui.text(0,0,"Exit: [Select]")
			gui.text(400,0,"Cycle: L1/R1")
			gui.text(0,20,"Back: L2")
			gui.text(400,20,"Choose: R2")
			-- Main menu?
			if menuID < 0 then
				-- First display menu
				for key,val in pairs(mtable) do
					if key < 0 then
						gui.text(100,50,val)
					else
						local y = 20*(5+key)
						if key == optionID then
							gui.text(x,y,val[-1],"blue")
						else
							gui.text(x,y,val[-1])
						end
					end
				end
				-- Then take inputs
				-- Select turns off the menu but saves selection
				if pad[select] and framecount[select] == 0 then
					menuon = false
					framecount[select] = FRAMES_PER_SECOND + 1
				-- L2 backs out of the menu not saving selection
				elseif pad[L2] and framecount[L2] == 0 then
					menuon = false
					optionID = 0
					framecount[L2] = 31
				-- R2 selects option
				elseif pad[R2] and framecount[R2] == 0 then
					menuID = optionID
					if menuID == 0 then
						optionID = levelchoice
					elseif menuID == 2 then
						optionID = memory.readbyte(leveladd1)
					else
						optionID = 0
					end
					framecount[R2] = 31
				-- L1 goes back an option
				elseif pad[L1] and framecount[L1] < 2 then
					if optionID == 0 then
						optionID = maxOption
					else
						optionID = optionID - 1
					end
					if framecount[L1] < 1 then
						framecount[L1] = 31
					else
						framecount[L1] = 16
					end
				-- R1 goes forward an option
				elseif pad[R1] and framecount[R1] < 2 then
					if optionID == maxOption then
						optionID = 0
					else
						optionID = optionID + 1
					end
					if framecount[R1] < 1 then
						framecount[R1] = 31
					else
						framecount[R1] = 16
					end
				end
			-- Level Menu
			elseif menuID == 0 then
				-- First display Menu
				for key,val in pairs(mtable[menuID]) do
					if key < 0 then
						gui.text(100,50,val)
					else
						local y = 20*(5+key)
						if key == optionID then
							gui.text(x,y,val,"blue")
						else
							gui.text(x,y,val)
						end
					end
				end
				-- Then take inputs
				-- Select turns off the menu but saves selection
				if pad[select] and framecount[select] == 0 then
					menuon = false
					framecount[select] = FRAMES_PER_SECOND + 1
				-- L2 backs out to main menu
				elseif pad[L2] and framecount[L2] == 0 then
					optionID = menuID
					menuID = -1
					framecount[L2] = 31
				-- R2 does nothing
				-- L1 goes back an option
				elseif pad[L1] and framecount[L1] < 2 then
					if optionID == 0 then
						optionID = maxLevel
					else
						optionID = optionID - 1
					end
					levelchoice = optionID
					if framecount[L1] < 1 then
						framecount[L1] = 31
					else
						framecount[L1] = 16
					end
				-- R1 goes forward an option
				elseif pad[R1] and framecount[R1] < 2 then
					if optionID == maxLevel then
						optionID = 0
					else
						optionID = optionID + 1
					end
					levelchoice = optionID
					if framecount[R1] < 1 then
						framecount[R1] = 31
					else
						framecount[R1] = 16
					end
				end
			-- Cheat menu
			elseif menuID == 1 then
				-- First display Menu
				for key,val in pairs(mtable[menuID]) do
					if key < 0 then
						gui.text(100,50,val)
					else
						local y = 20*(5+key)
						if key == optionID then
							gui.text(x,y,val .. ": " .. memory.readbyte(cheatadd[val]),"blue")
						else
							gui.text(x,y,val .. ": " .. memory.readbyte(cheatadd[val]))
						end
					end
				end
				-- Then take inputs
				-- Select turns off the menu but saves selection
				if pad[select] and framecount[select] == 0 then
					menuon = false
					framecount[select] = FRAMES_PER_SECOND + 1
				-- L2 backs out to main menu
				elseif pad[L2] and framecount[L2] == 0 then
					optionID = menuID
					menuID = -1
					framecount[L2] = 31
				-- R2 flips bit on selected item
				elseif pad[R2] and framecount[R2] == 0 then
					local tempcheataddress = cheatadd[mtable[menuID][optionID]]
					if memory.readbyte(tempcheataddress) == 0 then
						memory.writebyte(tempcheataddress,1)
					else
						memory.writebyte(tempcheataddress,0)
					end
					framecount[R2] = 31
				-- L1 goes back an option
				elseif pad[L1] and framecount[L1] < 2 then
					if optionID == 0 then
						optionID = maxCheat
					else
						optionID = optionID - 1
					end
					if framecount[L1] < 1 then
						framecount[L1] = 31
					else
						framecount[L1] = 16
					end
				-- R1 goes forward an option
				elseif pad[R1] and framecount[R1] < 2 then
					if optionID == maxCheat then
						optionID = 0
					else
						optionID = optionID + 1
					end
					if framecount[R1] < 1 then
						framecount[R1] = 31
					else
						framecount[R1] = 16
					end
				end
			-- Location Tracker Menu
			else
				-- First display Menu
				if optionID < 0 then
					gui.text(100,50,"Totals","gold")
					gui.text(x,100,"Work in progress")
				else
					for key,val in pairs(check[optionID]) do
						if key < 0 then
							gui.text(100,50,val,"gold")
						else
							local y = 20*(5+key)
							x = 50 + (300*(key//20))
							if val[4] then
								gui.text(x,y,val[1],"blue")
							else
								gui.text(x,y,val[1])
							end
						end
					end
					x = 50
				end
				-- Then take inputs
				-- Select turns off the menu but saves selection
				if pad[select] and framecount[select] == 0 then
					menuon = false
					framecount[select] = FRAMES_PER_SECOND + 1
				-- L2 backs out to main menu
				elseif pad[L2] and framecount[L2] == 0 then
					optionID = menuID
					menuID = -1
					framecount[L2] = 31
				-- R2 does nothing
				-- L1 goes back an option
				elseif pad[L1] and framecount[L1] < 2 then
					if optionID == -1 then
						optionID = maxCheck
					else
						optionID = optionID - 1
					end
					if framecount[L1] < 1 then
						framecount[L1] = 31
					else
						framecount[L1] = 16
					end
				-- R1 goes forward an option
				elseif pad[R1] and framecount[R1] < 2 then
					if optionID == maxCheck then
						optionID = -1
					else
						optionID = optionID + 1
					end
					if framecount[R1] < 1 then
						framecount[R1] = 31
					else
						framecount[R1] = 16
					end
				end
			end
		elseif pad[select] and framecount[select] == 0 then
			-- Turn on menu
			menuon = true
			framecount[select] = FRAMES_PER_SECOND + 1
		elseif framecount["Startup"] > 0 then
			gui.text(0,0,"Press [Select] to bring up the menu.")
		end
	else
		menuon = false
		-- While playing, check locations
		local currentlevel = memory.readbyte(leveladd1)
		if currentlevel < 9 then
			--[[if framecount["Debug"] == 0 then
				console.log('Checking level memory.')
			end]]--
			for key,val in pairs(check[currentlevel]) do
				if key >= 0 and (not val[4]) and (memory.readbyte(val[2]) & val[3] > 0) then
					check[currentlevel][key][4] = true
				end
			end
		end
	end
	
	-- Decrement framecount
	for key,val in pairs(framecount) do
		if val > 0 then
			framecount[key] = val - 1
		elseif key == "Debug" then
			framecount[key] = FRAMES_PER_SECOND
		end
	end
end

event.onframestart(gameloop)

