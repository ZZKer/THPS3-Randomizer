console.log('Start.')

local stateadd = 0x0BF454
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
local maxLevel = 8

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
local maxOption = 1

x = 50
function gameloop()
	-- If not in a session
	if memory.readbyte(stateadd) == 0 then
		-- Set level correctly (need to fix up in future)
		if not (memory.readbyte(leveladd2) == levelchoice) then
			memory.writebyte(leveladd1, levelchoice)
			memory.writebyte(leveladd2, levelchoice)
		end
		
		-- Get input data
		local pad = joypad.getimmediate()
		
		if menuon then
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
					framecount[select] = 61
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
					framecount[select] = 61
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
			else
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
					framecount[select] = 61
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
			end
		elseif pad[select] and framecount[select] == 0 then
			-- Turn on menu
			menuon = true
			framecount[select] = 61
		end
	else
		menuon = false
	end
	
	-- Decrement framecount
	for key,val in pairs(framecount) do
		if val > 0 then
			framecount[key] = val - 1
		end
	end
end

event.onframestart(gameloop)