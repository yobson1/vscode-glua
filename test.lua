nil false true ...
var = "\a\b\f\n\r\t\v\\\"\'"
var = 'alo\n123"'
var = "alo\n123\""
var = '\97lo\10\04923"'
var = [[alo
123"]]
var = [==[
alo
123"]==]
var3 = "test"
v4r3r333333 = "test"
1+1<1-1<=1*1>1/1>=1^1==1%1~=1..1!=1#1
3   3.0   3.1416   314.16e-2   0.31416E1   0xff   0x56

var = { [f(1)] = g; "x", "y"; x = 1, f(x), [30] = 23; 45 }

1 + 1 < 1 - 1 <= 1 * 1 > 1 / 1 >= 1 ^ 1 == 1 % 1 ~= 1 .. 1 != (#1 and -1 or not 1)
&& ||
and
or
break
not
return
continue
goto Name
::Name::
do block end
while exp do block end
repeat block until exp
if exp then block elseif exp then block else block end
for Name = exp, exp, exp do block end
for namelist in explist do block end
function funcname(parlist, ...) block end
function obj:funcname(parlist, ...) self:method() end
function tbl.funcname(parlist, ...) block end
function tbl.tbl.funcname(parlist, ...) block end
function chat.AddText(parlist, ...) block end
function tbl.tbl.tbl.tbl() end
local function Name(parlist, ...) block end
local namelist = explist;
funcname(parlist, ...)
obj:funcname(parlist, ...)
tbl.funcname(parlist, ...)
chat.AddText(parlist, ...)
tbl.tbl.funcname(parlist, ...)
tbl[1]["foo"].bar(...)
tbl[foo].foo.bar(...)
tbl.tbl.tbl.tbl()
-- Single comment
code() -- Single comment

--[[Multilined
comment
]]--

--[[Multilined comment
]]

--[===[
Multilined comment
]===]--
