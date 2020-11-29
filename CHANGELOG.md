# Change Log

## 2.3.1
- Changed ENTITY to ENT and WEAPON to SWEP for hook snippets

## 2.3.0
- Added hooks to snippets

## 2.2.3
- Fixed numbers at the end of variable names being tokenized

## 2.2.2
- Added additional newlines to enum snippet descriptions

## 2.2.1
- Updated description

## 2.2.0
- Added enums to snippets

## 2.1.0
- Added libraries and meta methods to snippets

## 2.0.1
- Improved descriptions of several snippets

## 2.0.0
- Added snippets, currently only for global functions

## 1.1.10
- Fixed numbers being highlighted incorrectly with a negative exponent

## 1.1.9
- More regex improvements

## 1.1.8
- More regex improvements
- Fixed functions not being highlighted correctly when called with a single argument using a multilevel string
- Fixed ... not being highlighted as a const
- Fixed < and > not being highlighted as operators
- Fixed numbers in variable names being highlighted

## 1.1.7
- More regex improvements
- Fixed accessing a table with [] being recognised as a function call

## 1.1.6
- More regex improvements
- Fixed 'self' highlight
- Fixed function calls not being highlighted as such if they are also table members e.g. TestTable.TestMethod()

## 1.1.5
- Fixed many operators not being highlighted

## 1.1.4
- Added icon

## 1.1.3
- Fixed concatenation operator not being highlighted

## 1.1.2
- Fixed = operator not being highlighted

## 1.1.1
- Fixed operators not needing to match whole word

## 1.1.0
- Made several improvements to the regex expressions used

## 1.0.2
- Fixed a bug where if a table member with the word function anywhere within was indexed using . it would break the highlighting

## 1.0.1
- Updated standard library matches for latest Garry's Mod version

## 1.0.0
- Initial release
