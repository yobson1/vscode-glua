-- Functions
local function func(arg)

end

function test.test(hello, world)

end

function test:test(hello, world)

end

local function vargtest(...)
	local test = {...}
end

func "Hello World!"
func 'Hello World!'
func [[Hello World!]]
func [==[  ]==]
func {"Hello World!"}

-- Consts
true
false
nil
NULL
_G
_VERSION
math.pi
math.huge
jit.arch
jit.os
jit.version
jit.version_num
SERVER
CLIENT
...

-- Numbers
123
.123
0.123
0x3F
0xFF.03

-- Strings
"Hello world"
'Hello world'
[[Hello world]]
"Newline \n"
"Backslash \\"
"Decimal \100"
"Hex \xff"
"Invalid escape \i \e"
[=[
	[[]]
]=]

-- Keywords
break do else elseif
end for goto
if in local repeat
return then until while

+ - * / ^
.. == ~= < > <= >=
and or not

goto done
::done::

self
self.self.self

-- Variable names
test
TEST
t3st
_test__fewf4f
3invalid

-- Comments
--[[
	Hello World
]]
/*
	Hello World
*/
-- Hello World
// Hello World
