#NoEnv
SendMode Input
SetWorkingDir %A_ScriptDir%

^!]::
	Gui, Font, s10	Gui, Add, Text, , select symbol
	Gui, Add, Button,xm  W20 H20, °
	Gui, Add, Button,x+0 W20 H20, ±
	Gui, Add, Button,x+0 W20 H20, ≈
	Gui, Add, Button,x+0 W20 H20, ≠
	Gui, Add, Button,xm  W20 H20, √
	Gui, Add, Button,x+0 W20 H20, ∞
	Gui, Add, Button,x+0 W20 H20, ∆
	Gui, Add, Button,x+0 W20 H20, π
	Gui, Add, Button,xm  W20 H20, ∑

	Gui, Show, , SymbolGUI
	Return
	Button°:
		WinClose
		Send, °
		Return
	Button±:
		WinClose
		Send, ±
		Return
	Button≈:
		WinClose
		Send, ≈
		Return
	Button≠:
		WinClose
		Send, ≠
		Return
	Button√:
		WinClose
		Send, √
		Return
	Button∞:
		WinClose
		Send, ∞
		Return
	Button∆:
		WinClose
		Send, ∆
		Return
	Buttonπ:
		WinClose
		Send, π
		Return
	Button∑:
		WinClose
		Send, ∑
		Return


#IfWinActive, SymbolGUI

Down::
	Send, {Right 4}
	return
Up::
	Send, {Left 4}
	return