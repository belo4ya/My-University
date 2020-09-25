chcp 65001
@echo off

set HEADER1=День,Поставка
set HEADER2=День,Продажа

for /l %%i in (1,1,10) do (
	md "Магазин%%i"
	cd "./Магазин%%i"
	echo %HEADER1% > "in.txt"
	setlocal EnableDelayedExpansion
	for /l %%d in (1,1,7) do (
		set /a par1=%random% %%100 +1
		echo %%d,!par1! >> "in.txt"
	)
	echo %HEADER2% > "out.txt"
		for /l %%d in (1,1,7) do (
		set /a par2=%random% %%100 +1
		echo %%d,!par2! >> "out.txt"
	)
	cd ".."
)
