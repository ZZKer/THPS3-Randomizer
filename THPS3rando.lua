console.log('Start.')

--- current values for items
local items = {}
-- progression
items["goals"] = 0x00
items["stats"] = 0x00
items["stats_used"] = 0x00

-- stats
items["air"] = 0x0A
items["hangtime"] = 0x09
items["ollie"] = 0x08
items["speed"] = 0x07
items["spin"] = 0x06
items["land"] = 0x00
items["switch"] = 0x05
items["rail"] = 0x04
items["lip"] = 0x02
items["manual"] = 0x03

-- junk
items["decks"] = 0x01

--- addresses
local addresses = {}
-- game states
--addresses["state"] = ???
addresses["pause"] = 0x0D56A8
addresses["skater"] = 0x0C2E48

-- items
addresses["goals"] = 0x0BB710
addresses["stats"] = 0x0BB711
addresses["decks"] = 0x0BB73C
addresses["air"] = 0x0BB740
addresses["hangtime"] = 0x0BB741
addresses["ollie"] = 0x0BB742
addresses["speed"] = 0x0BB743
addresses["spin"] = 0x0BB744
addresses["landing"] = 0x0BB745
addresses["switch"] = 0x0BB746
addresses["rail"] = 0x0BB747
addresses["lip"] = 0x0BB748
addresses["manual"] = 0x0BB749

-- checks
addresses["foundry_goals"] = 0x0BB720
addresses["foundry_stats"] = 0x0BB74C
addresses["foundry_deck"] = 0x0BB750


-- the gameloop plays every frame
function gameloop()
	-- first lock bytes
	--memory.writebyte(0x0)
	-- then check flags
	checkbytes()
	--memory.readbyte(0x0)
	-- if flag tripped, check table
	--  *if board, set bit
	--  *if move, set byte
	--  *if stat, add to byte
	--  *if progressive level, add specific to byte
	-- gui.text(50,50,'Thing got!')
end

-- Check bytes for changes and report checks
function checkbytes()
	--local current_state = memory.readbyte(astate)
end

event.onframestart(gameloop)